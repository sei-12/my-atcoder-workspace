#!/bin/bash

CONTENTS_DIR="./contests"


source ./venv/bin/activate

mkdir -p $CONTENTS_DIR

cd $CONTENTS_DIR

echo -n "contest name: "
read CONTEST_NAME

acc new --choice all $CONTEST_NAME
cd $CONTEST_NAME
code .
