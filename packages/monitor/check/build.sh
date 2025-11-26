#!/bin/bash
set -e
python3 -m venv --without-pip virtualenv
pip install -r requirements.txt --target virtualenv/lib/python3.9/site-packages
