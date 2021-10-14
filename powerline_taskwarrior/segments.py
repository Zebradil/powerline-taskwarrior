# vim:fileencoding=utf-8:noet
import string
import shutil
from subprocess import PIPE, Popen

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info


@requires_segment_info
class TaskwarriorBaseSegment(Segment):
    pl = None
    task_alias = "task"

    def validate_task_alias(self, task_alias):
        if not task_alias:
            self.pl.error("task_alias is empty")
            return False

        if shutil.which(task_alias) is None:
            self.pl.error("%s is not executable" % task_alias)
            return False

        return True

    def execute(self, command):
        self.pl.debug("Executing command: %s" % " ".join(command))

        proc = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        # Taskwarrior doesn't have non-interactive mode,
        # provide some input in case it asks for something
        proc.stdin.write(b"")
        out, err = [item.decode("utf-8") for item in proc.communicate()]

        if out:
            self.pl.debug("Command output: %s" % out.strip(string.whitespace))
        if err:
            self.pl.debug("Command errors: %s" % err.strip(string.whitespace))

        return out.splitlines(), proc.returncode != 0

    def build_segments(self):
        self.pl.debug("Nothing to do")
        return []

    def __call__(self, pl, segment_info, task_alias="task"):
        self.pl = pl
        self.task_alias = task_alias
        pl.debug("Taskwarrior alias: %s" % task_alias)

        if not self.validate_task_alias(task_alias):
            return

        return self.build_segments()


class ContextSegment(TaskwarriorBaseSegment):
    def build_segments(self):
        self.pl.debug("Build Context segment")

        context_name, err = self.execute(
            [self.task_alias, "rc.hooks:off", "_get", "rc.context"]
        )

        if not err and context_name:
            context_name = context_name.pop(0)
            if context_name:
                return [
                    {
                        "contents": context_name,
                        "highlight_groups": ["taskwarrior:context"],
                    }
                ]

        return []


class ActiveTaskSegment(TaskwarriorBaseSegment):
    description = None
    task_id = None

    def __call__(
        self, pl, segment_info, task_alias="task", description_length=40, state="active"
    ):
        self.description_length = description_length
        self.state = state

        return super(ActiveTaskSegment, self).__call__(pl, segment_info, task_alias)

    def build_segments(self):
        self.pl.debug("Build ActiveTask segment")

        task = self.get_task()

        if task:
            self.task_id, self.description = task

            return [
                {
                    "name": "active_task_id",
                    "contents": "#%s" % self.task_id,
                    "highlight_groups": [
                        "taskwarrior:{state}_id".format(state=self.state)
                    ],
                },
                {
                    "name": "active_task_description",
                    "contents": self.cut_description(
                        self.description, self.description_length
                    ),
                    "highlight_groups": [
                        "taskwarrior:{state}_desc".format(state=self.state)
                    ],
                },
            ]
        else:
            self.pl.debug("No tasks")
            return []

    def truncate(self, pl, amount, segment, description_length=0, **kwargs):
        if segment["name"] == "active_task_id":
            return segment["contents"]

        length = segment["_len"] - amount
        if description_length and description_length < length:
            length = description_length
        return self.cut_description(self.description, length)

    @staticmethod
    def cut_description(description, length):
        if length and len(description) > length:
            parts = []
            for part in description.split():
                if len(" ".join(parts + [part])) < length - 1:
                    parts.append(part)
                else:
                    return " ".join(parts) + "…"
        else:
            return description

    def get_task(self):
        id_and_description, err = self.execute(self.get_command_parts())

        if not err and id_and_description:
            self.pl.debug(id_and_description)
            return id_and_description.pop(0).split(" ", 1)

    def get_command_parts(self):
        return [
            self.task_alias,
            "rc.verbose:nothing",
            "rc.hooks:off",
            "rc.report.next.columns:id,description",
            "rc.report.next.labels:1,2",
            "limit:1",
            "+ACTIVE",
            "next",
        ]


class NextTaskSegment(ActiveTaskSegment):
    def __call__(
        self,
        pl,
        segment_info,
        task_alias="task",
        description_length=40,
        ignore_active=False,
    ):
        self.pl = pl

        if not self.validate_task_alias(task_alias):
            return

        if ignore_active or not self.exists_active_task():
            return super(NextTaskSegment, self).__call__(
                pl, segment_info, task_alias, description_length, state="next"
            )
        else:
            return []

    def exists_active_task(self):
        out, err = self.execute(super(NextTaskSegment, self).get_command_parts())
        return bool(not err and out)

    def get_command_parts(self):
        return [
            self.task_alias,
            "rc.verbose:nothing",
            "rc.hooks:off",
            "rc.report.next.columns:id,description",
            "rc.report.next.labels:1,2",
            "limit:1",
            "next",
        ]


class PendingTasksCountSegment(TaskwarriorBaseSegment):
    def build_segments(self):
        self.pl.debug("Build PendingTasksCount segment")

        pending_tasks_count, err = self.execute(
            [
                self.task_alias,
                "rc.verbose:nothing",
                "rc.hooks:off",
                "status:pending",
                "count",
            ]
        )

        if not err and pending_tasks_count:
            pending_tasks_count = pending_tasks_count.pop(0)
            if pending_tasks_count:
                return [
                    {
                        "contents": "[%s]" % pending_tasks_count,
                        "highlight_groups": ["taskwarrior:context"],
                    }
                ]

        return []


class TaskwarriorSegment(TaskwarriorBaseSegment):
    def build_segments(self):
        self.pl.debug("Build ActiveTask + Context segment")
        return ActiveTaskSegment()(self.pl, self.task_alias) + ContextSegment()(
            self.pl, self.task_alias
        )


taskwarrior = with_docstring(
    TaskwarriorSegment(),
    """Return information from Taskwarrior task manager.

    It will show current context and active task (first by urgency order).

    Highlight groups used: ``taskwarrior:active_id``, ``taskwarrior:active_desc``, ``taskwarrior:context``
    """,
)

context = with_docstring(
    ContextSegment(),
    """Return information from Taskwarrior task manager.

    It will show current context.

    Highlight groups used: ``information:regular``
    """,
)

active_task = with_docstring(
    ActiveTaskSegment(),
    """Return information from Taskwarrior task manager.

    It will show active task (first by urgency order).

    Highlight groups used: ``taskwarrior:active_id``, ``taskwarrior:active_desc``
    """,
)

next_task = with_docstring(
    NextTaskSegment(),
    """Return information from Taskwarrior task manager.

    It will show next task (first by urgency order).

    Highlight groups used: ``taskwarrior:next_id``, ``taskwarrior:next_desc``
    """,
)

pending_tasks_count = with_docstring(
    PendingTasksCountSegment(),
    """Return information from Taskwarrior task manager.

    It will show count of pending tasks.

    Highlight groups used: ``taskwarrior:next_id``, ``taskwarrior:next_desc``
    """,
)
