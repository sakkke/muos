#!/usr/bin/env bash

./scripts/install_hooks.sh

pipx install poetry

poetry self add poetry-dynamic-versioning

make install-devdeps

npm --prefix ./tools/netlify-cli install
