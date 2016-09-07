Powerline Taskwarrior
===================

A [Powerline][1] segment for showing information from [Taskwarrior][2] task manager.

By [German Lashevich][3].

It will show current context and active task (first of alphabetical order).

![screenshot][4]

Requirements
------------

The Taskwarrior segment requires [task][2] of version 2.4.2 or higher.

Installation
------------

Installing the Taskwarrior segment can be done with pip:

```txt
pip install powerline-taskwarrior
```

Then you can activate the Taskwarrior segment by adding it to your segment configuration,
for example in `~/.config/powerline/config_files/themes/shell/default.json`:

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
