#!/usr/bin/env bash
source /home/codespace/venv/bin/activate
source ~/.bashrc
#append it to bash so every shell launches with it 
echo 'source /home/codespace/venv/bin/activate' >> ~/.bashrc
make install-tensorflow
