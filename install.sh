#!/bin/bash
echo "Creating directory"
mkdir downloads
chmod 7777 downloads
git clone https://github.com/nashnoor/google-dorks-py.git
cd google-dorks-py
echo "The current working directory is $PWD/downloads. Please enter the following directory in dorks.py *download_dir*
