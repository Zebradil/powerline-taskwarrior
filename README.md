Powerline Taskwarrior
===================

[Powerline][1] segments for showing information from the [Taskwarrior][2] task manager.

By [German Lashevich][3].

It will show current context and the most urgent active task.

![screenshot][4]

Requirements
------------

The Taskwarrior segments require [task][2] of version 2.4.2 or higher.

Installation
------------

Installing the Taskwarrior segments can be done with pip:

```txt
pip install powerline-taskwarrior
```

On Debian (testing or unstable), installation can be performed with apt:

```txt
apt install python-powerline-taskwarrior
```

Then you can activate the Taskwarrior segments by adding it to your segment configuration,
for example in `~/.config/powerline/themes/shell/default.json`:

segment displays current context name
```json
{
    "function": "powerline_taskwarrior.context",
    "priority": 70
}
```

segment displays the most urgent active task
```json
{
    "function": "powerline_taskwarrior.active_task",
    "priority": 70
}
```

obsolete segment displays both of listed above
```json
{
    "function": "powerline_taskwarrior.taskwarrior",
    "priority": 70
}
```

License
-------

Licensed under [the MIT License][5].

[1]: https://powerline.readthedocs.org/en/master/
[2]: http://taskwarrior.org/
[3]: https://github.com/zebradil
[4]: https://github.com/zebradil/powerline-taskwarrior/blob/master/screenshot.png
[5]: https://github.com/zebradil/powerline-taskwarrior/blob/master/LICENSE
