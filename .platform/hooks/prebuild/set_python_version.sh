#!/bin/bash
echo "Setting Python 3.9 as default for Elastic Beanstalk..."
if [ -f /usr/bin/python3.9 ]; then
    ln -sf /usr/bin/python3.9 /usr/bin/python3
    ln -sf /usr/bin/python3.9 /usr/bin/python
else
    echo "Python 3.9 is not available on this machine."
fi
