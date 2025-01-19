#!/bin/bash

python3 -m venv ./venv
source ./venv/bin/activate
source ./.env

pip install setuptools
pip install online-judge-tools
npm install -g atcoder-cli

acc login
acc config default-template python