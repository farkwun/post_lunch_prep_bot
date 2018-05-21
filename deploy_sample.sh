#!/bin/bash

pkill -f prepbot

git reset --hard HEAD
git pull

pip install -r requirements.txt

zulip-run-bot prepbot --config-file zuliprc &> error.log &disown;
