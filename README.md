# Powerline Taskwarrior

![CI](https://github.com/zebradil/powerline-taskwarrior/actions/workflows/ci.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/powerline-taskwarrior.svg)](https://pypi.python.org/pypi/powerline-taskwarrior)
[![PyPI](https://img.shields.io/pypi/l/powerline-taskwarrior.svg)](https://opensource.org/licenses/MIT)

A set of [Powerline][1] segments for showing information retrieved from [Taskwarrior][2] task manager.

It shows a current context and the most urgent active task.

![screenshot][4]

## Requirements

Taskwarrior segments require:
- [task][2] v2.4.2 or later,
- Python `^3.7` (support for Python 2.7 was dropped)

## Installation

### PIP

```sh
pip install --user -U powerline-taskwarrior
```

It can also be installed system-wide, but this is usually a bad idea.

### Debian

On Debian (testing or unstable), installation can be performed with apt:

```sh
apt install python-powerline-taskwarrior
```

## Usage

### Activate segments

To activate Taskwarrior segments add them to your segment configuration.
See more about powerline configuration in [the official documentation][7].
For example, I store powerline configuration in
`~/.config/powerline/themes/shell/default.json`.

These are available powerline-taskwarrior segments:

- display current context name
  ```json
  {
      "function": "powerline_taskwarrior.context",
      "priority": 70
  }
  ```

- display the count of pending tasks
  ```json
  {
      "function": "powerline_taskwarrior.pending_tasks_count",
      "priority": 70
  }
  ```

- display the most urgent active task
  ```json
  {
      "function": "powerline_taskwarrior.active_task",
      "priority": 70
  }
  ```

- display the most urgent next task
  ```json
  {
      "function": "powerline_taskwarrior.next_task",
      "priority": 70
  }
  ```

- *obsolete* segment displays both of listed above
  ```json
  {
      "function": "powerline_taskwarrior.taskwarrior",
      "priority": 70
  }
  ```

### Color scheme

Taskwarrior-powerline requires custom colorscheme to be configured.
Add the following to your colorschemes (`.config/powerline/colorschemes/default.json`):

```json
{
  "groups": {
    "taskwarrior:context": "information:regular",
    "taskwarrior:pending_tasks_count": "information:priority",
    "taskwarrior:active_id": { "bg": "mediumgreen", "fg": "black", "attrs": [] },
    "taskwarrior:active_desc": { "bg": "green", "fg": "black", "attrs": [] },
    "taskwarrior:next_id": { "bg": "brightyellow", "fg": "black", "attrs": [] },
    "taskwarrior:next_desc": { "bg": "yellow", "fg": "black", "attrs": [] }
  }
}

```

And here you can configure the colors.

See [powerline colorschemes docs][6] for more details.

### Further customization

If you have a custom name for `task` command, it should be specified via `task_alias` argument in the segment configuration.

`powerline_taskwarrior.active_task` and `powerline_taskwarrior.next_task` segments accept `description_length` parameter.
It is an integer which represents a maximum length of the description field.
If a description is longer than `description_length`, it is truncated by words.

`powerline_taskwarrior.next_task` segment accepts `ignore_active` parameter.
If it set to `true`, the segment will be shown always, regardless of existence of an active task.

```json
{
    "function": "powerline_taskwarrior.next_task",
    "priority": 70,
    "args": {
        "task_alias": "taskwarrior",
        "description_length": 40
    }
}
```


## License

Licensed under [the MIT License][5].

By [German Lashevich][3].

[1]: https://powerline.readthedocs.org/en/master/
[2]: http://taskwarrior.org/
[3]: https://github.com/zebradil
[4]: https://github.com/zebradil/powerline-taskwarrior/blob/master/screenshot.png
[5]: https://github.com/zebradil/powerline-taskwarrior/blob/master/LICENSE
[6]: http://powerline.readthedocs.io/en/master/configuration/reference.html#colorschemes
[7]: https://powerline.readthedocs.io/en/master/configuration.html#configuration-and-customization
