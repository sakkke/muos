#!/usr/bin/env bash

./scripts/install-hooks.sh

pipx install poetry

poetry self add poetry-dynamic-versioning

poetry install

npm --prefix ./tools/netlify-cli install
