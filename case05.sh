# Bug Category: Cross-Origin Flaws (3)

# The logic of the php is: 

# Exploit: 

#!/bin/bash

# Install Geckodriver
# Ref: https://askubuntu.com/questions/851401/where-to-find-geckodriver-needed-by-selenium-python-package
echo Installing Geockodrive...
export GECKO_DRIVER_VERSION='v0.24.0'

wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux32.tar.gz

tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux32.tar.gz

sudo rm geckodriver-$GECKO_DRIVER_VERSION-linux32.tar.gz

sudo chmod +x geckodriver

sudo cp geckodriver /usr/local/bin/

# Run package installations
echo Upgrading Dependencies...
sudo apt update && sudo apt install -y --only-upgrade firefox
sudo pip3 install selenium==3.14.1
sudo pip3 install --upgrade --ignore-installed urllib3
sudo pip3 install requests

# Run Script
python3 case05.py
