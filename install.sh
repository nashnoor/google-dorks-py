#!/bin/bash
echo "Cloning directory"
git clone https://github.com/nashnoor/google-dorks-py.git
cd google-dorks-py
echo "Creating directory"
mkdir downloads
chmod 7777 *
echo "Running pip install"
sudo pip install -r requirements.txt
echo "The current working directory is $PWD/downloads. Please enter the following directory in dorks.py  download_dir "
