#!/bin/bash

echo -n "name:"
read name

file_path=".archive/$name.rs"
cat ./src/main.rs > $file_path
cat ./src/template.main.rs > ./src/main.rs