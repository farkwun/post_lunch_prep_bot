#!/bin/bash

pkill -f post_lunch_prep_bot

git reset --hard HEAD
git pull

pip install -r requirements.txt

zulip-run-bot post_lunch_prep_bot --config-file zuliprc &> error.log &disown;
