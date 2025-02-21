#!/bin/bash
echo "Setting Python 3.9 as default for Elastic Beanstalk..."

# Define the correct Python 3.9 path
export PYTHON_PATH="/Users/tonywilson/Documents/PsychSafetyApp/venv/bin/python3.9"

if [ -f "$PYTHON_PATH" ]; then
    export PATH="/Users/tonywilson/Documents/PsychSafetyApp/venv/bin:$PATH"
    echo "Python 3.9 is set as default at $PYTHON_PATH"
    python --version
else
    echo "Python 3.9 is not available on this machine."
fi
