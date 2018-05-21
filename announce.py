import json
import os
import zulip

from post-lunch-prep-bot import INTRO, ANNOUNCE, DISCUSS

def send_message(message):
    client = zulip.Client(
        config_file="announcerzuliprc"
    )

    request = {
        "subject": "Post-lunch Prep!",
         "type": "private",
         "to": "prep-bot@recurse.zulipchat.com",
         "content": message
    }
    result = client.send_message(request)
    print(result)

def test(event, context):
    send_message("Hi, I'm PrepBot (kinda like SwoleBot but for your brain.)")


def pre_announce():
    send_message(INTRO)
def announce():
    send_message(ANNOUNCE)
def post_announce():
    send_message(DISCUSS)
