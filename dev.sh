#!/bin/bash

if [ -d ".venv" ]; then
    echo "Activating environment."
else
    echo "The environment does not exist. Creating environment."
    python3 -m pip install python-venv
    python3 -m venv .venv
fi


activate () {
  source .venv/bin/activate
}

activate