#!/bin/sh

PTW_DIR=/opt/powerline-taskwarrior

cd $PTW_DIR
pip${PYTHON_VERSION} install .
TASK_TEXT=$(date | md5sum | head -c 16)
task add $TASK_TEXT
export XDG_CONFIG_DIRS=$PTW_DIR/test/.config
LOG_FILE=/tmp/powerline-error.log
if [[ "$(powerline shell right | tee $LOG_FILE | fgrep -c $TASK_TEXT)" -eq 1 ]]; then
  exit 0
else
  cat $LOG_FILE
  exit 1
fi
