#!/bin/bash

set -o errexit -o pipefail -o noclobber -o nounset

# Initialize Taskwarrior database
echo yes | task version

TASK_TEXT=$(openssl rand -hex 16)
task add $TASK_TEXT

export XDG_CONFIG_DIRS="$(dirname -- "${BASH_SOURCE[0]}")/.config"

LOG_FILE=/tmp/powerline-error.log

if [[ "$(powerline shell right | tee $LOG_FILE | fgrep -c $TASK_TEXT)" -ne 1 ]]; then
    echo -e "\033[1;31m======== TEST FAILED ========\033[0m"
    echo The output expected to contain "$TASK_TEXT"
    echo The following was printed instead:
    cat $LOG_FILE
    echo
    exit 1
fi

echo -e "\033[1;32m======== TEST PASSED ========\033[0m"
