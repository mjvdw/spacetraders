#!/bin/bash

if [ ! -d ".venv" ]; then
    sudo apt install python3.10-venv -y
fi

source .venv/bin/activate
pip install -r requirements.txt
openapi-generator generate -i SpaceTraders.json -g python --skip-validate-spec -o packages/spacetraders-sdk
pip install packages/spacetraders-sdk
