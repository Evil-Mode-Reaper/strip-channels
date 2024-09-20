#!/bin/bash
#
# Sets up the local environment to run this script in a Python venv.
# NOTE: Still in progress.


python_version="$(cat "$(dirname "${BASH_SOURCE}")/.python-version")"

if  [[ "$(python3 --version)" != "$python_version" ]] && [[ ! -d "$HOME/.pyenv" ]]; then
    git clone https://github.com/pyenv/pyenv.git "$HOME/.pyenv"
fi

