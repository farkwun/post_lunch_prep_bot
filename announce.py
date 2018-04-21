import json
import os
import zulip

from prepsetup import INTRO, ANNOUNCE, DISCUSS


def send_message(message):
    client = zulip.Client(
        site="https://recurse.zulipchat.com",
        email="post-lunch-prep-announcer-bot@recurse.zulipchat.com",
        api_key="fr3P5hi8O1F9jUqae5WQWSrTz2krzf8T"
    )

    request = {
        "subject": "Post-lunch Prep!",
         "type": "private",
         "to": "post-lunch-prep-setup-bot@recurse.zulipchat.com",
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
