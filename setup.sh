#!/bin/bash
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

pip install -U pip

# Install packages from requirements.txt
pip install -r requirements.txt