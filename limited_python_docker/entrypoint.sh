#!/bin/bash
echo "import $2" >> limit_resources.py

export PYTHONPATH=${PYTHONPATH}:$1

last_pwd=$(pwd)

cd $1

python $last_pwd/limit_resources.py
