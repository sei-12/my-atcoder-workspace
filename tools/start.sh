#!/bin/bash

source ./venv/bin/activate
echo -n "task: "
read task

mkdir -p .tmp
cat src/main.rs > .tmp/main.rs
cat src/template.main.rs > src/main.rs

contest_id=$(cat ./data.json | jq -r ".contest_id")
url="https://atcoder.jp/contests/$contest_id/tasks/"$contest_id"_$task"
rm -r .tests
mkdir .tests
oj download -d .tests/ $url > /dev/null

if [ $? -eq 0 ]; then
    echo "success download tests!"
else
    echo "fail download tests!"
fi



