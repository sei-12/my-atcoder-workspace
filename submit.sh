#!/bin/bash
source ../../venv/bin/activate
cd $1
echo "abc$1" | acc s -- main.py --language 5078 