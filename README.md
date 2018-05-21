# post_lunch_prep_bot
A Zulip bot for running Post-lunch Prep at RC

Post-lunch-prep bot uses the [python-zulip-api](https://github.com/zulip/python-zulip-api) to run the Post-lunch Prep event at RC.

The main bot (post_lunch_prep_bot.py) takes in user input via private message to configure the days questions and performs the actual announcements.

A secondary script (announce.py) run via a scheduled cron and triggers main bot to annouce post lunch prep. This is a workaround as zulip bots don't currently support scheduled actions.

## Installation

This project has the following dependencies
- [python-zulip-api](https://github.com/zulip/python-zulip-api)
- cron
- A zuliprc file for the post-lunch-prep bot called zuliprc (a sample zuliprc can be found in the repository)
- A zuliprc file for the scheduling bot called announcerzuliprc (a sample announcerzuliprc can be found in the repository)

### 1 - Run the bot 

1) Clone the [python-zulip-api](https://github.com/zulip/python-zulip-api) repository
2) Navigate to python-zulip-api/zulip_bots/zulip_bots/bots/
3) Clone this repository
4) Navigate into the repository folder
5) Ensure the zuliprc and announcerzuliprc credentials are set - (cannot be the same)
7) Run `chmod +x deploy_sample.sh`
8) Run `./deploy_sample.sh`

 ### 2 - Set up the cron

1) Install `cron` on your system if not already installed
2) Add the cron jobs defined in assets/sample_cron to your machine's crontab taking care to replace $BOT_DIR_WITH_ANNOUNCE_PY with whichever directory contains the announce.py file
3) Ensure the announcerzuliprc credentials are set

### 3 - Check if working

Send a private message with the text "help" to PrepBot in Zulip.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

