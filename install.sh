#!/bin/bash

python3 -m venv ./venv
source ./venv/bin/activate
source ./.env

pip install setuptools
pip install online-judge-tools
npm install -g atcoder-cli

acc login

CUR_DIR=$(pwd)
TEMPLATES_DIR=$CUR_DIR/templates
cd `acc config-dir`
ln -s $TEMPLATES_DIR/* .
cd $CUR_DIR


acc config default-template python