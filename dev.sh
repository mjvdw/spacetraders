#!/bin/bash

if [ -d ".venv" ]; then
    echo "Activating environment."
else
    echo "The environment does not exist. Creating environment."
    sudo apt install python3.10-venv -y
    python3 -m venv .venv
fi