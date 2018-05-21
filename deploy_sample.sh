#!/bin/bash

pkill -f post-lunch-prep-bot

git reset --hard HEAD
git pull

pip install -r requirements.txt

zulip-run-bot post-lunch-prep-bot --config-file zuliprc &> error.log &disown;
