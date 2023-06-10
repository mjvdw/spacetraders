#!/bin/bash

if [ -d ".venv" ]; then
    echo "Activating environment."
else
    echo "The environment does not exist. Creating environment."
    sudo apt install python3.10-venv -y
fi

source .venv/bin/activate
pip install -r requirements.txt
openapi-generator generate -i SpaceTraders.json -g python --skip-validate-spec -o backend/packages/spacetraders-sdk