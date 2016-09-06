# vim:fileencoding=utf-8:noet

import string
from subprocess import PIPE, Popen

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info


@requires_segment_info
class TaskwarriorSegment(Segment):
    def execute(self, pl, command):
        pl.debug('Executing command: %s' % ' '.join(command))

        proc = Popen(command, stdout=PIPE, stderr=PIPE)
        out, err = [item.decode('utf-8') for item in proc.communicate()]

        if out:
            pl.debug('Command output: %s' % out.strip(string.whitespace))
        if err:
            pl.debug('Command errors: %s' % err.strip(string.whitespace))

        return out.splitlines(), err.splitlines()

    def build_segments(self, context, active_task):

        segments = []

        if context:
            segments.append({
                'contents': context,
                'highlight_groups': ['information:regular'],
            })

        if active_task:
            segments.append({
                'contents': active_task,
                'highlight_groups': ['information:priority'],
            })

        return segments

    def __call__(self, pl, segment_info, task_alias='task'):
        pl.debug('Running Taskwarrior: ' + task_alias)

        if not task_alias:
            return

        context, err = self.execute(pl, [task_alias, '_get', 'rc.context'])

        if err:
            return

        if context:
            context = context.pop(0)

        description, err = self.execute(pl, [task_alias, '+ACTIVE', '_unique', 'description'])

        if err:
            return

        if description:
            description = description.pop(0)

        return self.build_segments(context, description)


taskwarrior = with_docstring(TaskwarriorSegment(),
                             '''Return information from Taskwarrior task manager.

                             It will show current context and active task (first of alphabetical order).

                             Highlight groups used: ``information:priority``, ``information:regular``
                             ''')
