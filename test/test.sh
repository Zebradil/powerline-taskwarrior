#!/bin/sh

PTW_DIR=/opt/powerline-taskwarrior

cd $PTW_DIR
pip3 install .
TASK_TEXT=$(date | md5sum | head -c 16)
task add $TASK_TEXT
export XDG_CONFIG_DIRS=$PTW_DIR/test/.config
[[ "$(powerline shell right | fgrep -c $TASK_TEXT)" -eq 1 ]] || exit 1
