#!/usr/bin/env bash

./install-hooks.sh

pipx install poetry

poetry self add poetry-dynamic-versioning

poetry install

npm --prefix ./netlify-cli install
