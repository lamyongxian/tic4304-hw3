# Bug Category: Execution after Redirect (4)

# The logic of the php is: 

# Exploit: 

#!/bin/bash

# Install Geckodriver
# Ref: https://askubuntu.com/questions/851401/where-to-find-geckodriver-needed-by-selenium-python-package

export GECKO_DRIVER_VERSION='v0.24.0'

wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz

tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz

sudo rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz

sudo chmod +x geckodriver

sudo cp geckodriver /usr/local/bin/

# Run Script
pip3 install selenium
pip3 install requests
python3 case05.py
