#!/bin/bash

set -o errexit -o pipefail -o noclobber -o nounset

set +x

TASK_TEXT=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 16)
task add $TASK_TEXT

export XDG_CONFIG_DIRS=/app/test/.config

LOG_FILE=/tmp/powerline-error.log

if [[ "$(powerline shell right | tee $LOG_FILE | fgrep -c $TASK_TEXT)" -eq 1 ]]; then
  exit 0
else
  cat $LOG_FILE
  exit 1
fi
