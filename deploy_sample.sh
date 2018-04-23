#!/bin/bash

pkill -f prepsetup

git reset --hard HEAD
git pull

pip install -r requirements.txt

zulip-run-bot prepsetup --config-file zuliprc &> error.log &disown;
