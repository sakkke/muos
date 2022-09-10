#!/usr/bin/env bash

CWD="$(cd "$(dirname "$0")" && pwd)"

cp --no-target-directory --recursive --verbose "$CWD/hooks" "$CWD/.git/hooks"
