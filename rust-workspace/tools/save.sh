#!/bin/bash

echo -n "task:"
read task

contest_id=$(cat ./data.json | jq ".contest_id" -r)
file_path=".archive/$(date '+%Y-%m-%d-%H-%M-%S')-$contest_id-$task.rs"

cat ./src/main.rs > $file_path