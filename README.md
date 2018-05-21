# post-lunch-prep-bot
A Zulip bot for running Post-lunch Prep at RC

Post-lunch-prep bot uses the [python-zulip-api](https://github.com/zulip/python-zulip-api) to run the Post-lunch Prep event at RC.

The main bot, found in prepsetup.py, takes in user input via private message and performs the actual announcements.

A secondary bot, with credentials defined in announce.py, is never actually run - rather, the credentials are used to fire off a Python script scheduled using cron.

## Installation

This project has the following dependencies
- [python-zulip-api](https://github.com/zulip/python-zulip-api)
- cron
- two zuliprc files
  - The post-lunch-prep bot itself
  - A scheduling bot

To run the bot - 

1) Clone the [python-zulip-api](https://github.com/zulip/python-zulip-api) repository
2) Navigate to python-zulip-api/zulip_bots/zulip_bots/bots/
3) Clone this repository
4) Navigate into the repository folder
5) Download the zuliprc for whichever bot you'd like to act as the main bot from Zulip
6) Place the zuliprc in this repository directory
7) Run `chmod +x deploy_sample.sh`
8) Run `./deploy_sample.sh`

To set up the cron - 

1) Install `cron` on your system if not already installed
2) Add the cron jobs defined in assets/sample_cron to your machine's crontab taking care to replace $BOT_DIR_WITH_ANNOUNCE_PY with whichever directory contains the announce.py file

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

