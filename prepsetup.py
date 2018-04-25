# See readme.md for instructions on running this code.  
from typing import Any
from os import environ

AUTH_IDS = set()

PASSWORD = "prep"

# COMMANDS
HELP = "help"
TOPIC = "topic"
HOST = "host"
RESOURCE = "resource"
ONE = "one"
TWO = "two"
PRINT = "print"

COMMAND_IDX = 0

COMMANDS = {
    HELP: lambda command: help(command),
    TOPIC: lambda command: set_topic(command),
    HOST: lambda command: set_host(command),
    RESOURCE: lambda command: set_resource(command),
    ONE: lambda command: set_one(command),
    TWO: lambda command: set_two(command),
    PRINT: lambda command: print_setup(command)
}

def help(command):
    return ("Welcome to Post-lunch Prep Setup!\n\n" +
            "To set today's topic, enter '{} <topic_title>'\n".format(TOPIC) +
            "To set today's resource, enter '{} <link>'\n".format(RESOURCE) +
            "To set today's host, enter '{} <@mention_user>'\n".format(HOST) +
            "To set the first question, enter '{} <link>'\n".format(ONE) +
            "To set the second question, enter '{} <link>'\n".format(TWO) +
            "To output today's setup, enter '{}'\n\n".format(PRINT) +
            "Separate commands by line breaks!"
    )

def set_resource(command):
    environ["PLP_RESOURCE"] = command[1]
    return ("Set resource to {}\n".format(get_env(ENV_RESOURCE)))

def set_topic(command):
    environ["PLP_TOPIC"] = ' '.join(command[1:])
    return ("Set topic to {}\n".format(get_env(ENV_TOPIC)))

def set_host(command):
    environ["PLP_HOST"] = ' '.join(command[1:])
    return ("Set host to {}\n".format(get_env(ENV_HOST)))

def set_one(command):
    environ["PLP_ONE"] = command[1]
    return ("Set first question to {}\n".format(get_env(ENV_ONE)))

def set_two(command):
    environ["PLP_TWO"] = command[1]
    return ("Set second question to {}\n".format(get_env(ENV_TWO)))

def print_setup(command):
    return("Today's setup is:\n\n"
           "Topic: {topic}\n\n"
           "Host: {host}\n\n"
           "Resource :{resource}\n\n"
           "First q: {one}\n\n"
           "Second q: {two}\n\n".format(
               topic=get_env(ENV_TOPIC),
               host=get_env(ENV_HOST),
               resource=get_env(ENV_RESOURCE),
               one=get_env(ENV_ONE),
               two=get_env(ENV_TWO)
           )
    )

# ENV VARS
ENV_RESOURCE = "PLP_RESOURCE"
ENV_TOPIC = "PLP_TOPIC"
ENV_ONE = "PLP_ONE"
ENV_TWO = "PLP_TWO"
ENV_HOST = "PLP_HOST"

def get_env(key):
    return environ.get(key, "")

# ANNOUNCEMENTS
INTRO = "intro"
ANNOUNCE = "announce"
DISCUSS = "discuss"
ANNOUNCER_EMAIL = "post-lunch-prep-announcer-bot@recurse.zulipchat.com"

ANNOUNCEMENTS = {
    INTRO: lambda: (
        "Hi everyone!\n\n" +
        "Today's topic will be {}!\n\n".format(get_env(ENV_TOPIC)) +
        "Today's resource on our topic can be found [here]({}). Please do give it a read through if you'd like to refresh your understanding and see some code samples!\n\n".format(get_env(ENV_RESOURCE)) +
        "The questions will be projected in the Mainspace from 1:45 PM to 2:45 PM. The leftmost question will tend to be more introductory, while the rightmost question will typically have a more involved implementation.\n\nIf you'd like to be notified whenever Post-lunch Prep makes this post, please feel free to join the User Group @*PLPRemindMe* in your Organization Settings <3"),

    ANNOUNCE: lambda: (
        "For those following along, today's questions are:\n\n" +
        "1) {}\n".format(get_env(ENV_ONE)) +
        "2) {}\n\n".format(get_env(ENV_TWO)) +
        "If you're interested in pairing come to the projector in the main space and we'll see if we can match you up :). {} will be running today's session!\n\n".format(get_env(ENV_HOST)) +
        "Please feel free to join us in Turing @ 2:45 PM for our discussion!"
    ),

    DISCUSS: lambda: (
        "Our post-lunch prep discussion will be in Turing in 10 minutes!\n\n"
        "Please come join regardless of whether you have completed, or even attempted, the questions :)\n\n"
        "If you have a solution you would like to present or discuss, send it over via PM to {}.".format(get_env(ENV_HOST))
    )
}

class HelloWorldHandler(object):
    def usage(self) -> str:
        return '''
        This is a boilerplate bot that responds to a user query with
        "beep boop", which is robot for  "Hello World".

        This bot can be used as a template for other, more
        sophisticated, bots.
        '''

    def announce(self, message : Any, bot_handler: Any):
        bot_handler.send_message(dict(
            type="stream",
            to="455 Broadway",
            subject="Post-lunch Prep!",
            content=message)
        )

    def handle_message(self, message: Any, bot_handler: Any) -> None:
        for key in message.keys():
            print(key, message[key])
        msg_type = message['type']
        if msg_type != 'private':
            bot_handler.send_reply(message, "Sorry! I only respond to PMs :(")
            return
        user_id = message['sender_id']
        user_email = message['sender_email']
        sent_msg = message['content']
        if user_email == ANNOUNCER_EMAIL:
            self.announce(ANNOUNCEMENTS[sent_msg](), bot_handler)
            return
        if user_id in AUTH_IDS:
            bot_handler.send_reply(message, self.parse_message(sent_msg))
        else:
            bot_handler.send_reply(message, self.authenticate(user_id, sent_msg))

    def authenticate(self, user_id, sent_msg):
        if sent_msg == PASSWORD:
            AUTH_IDS.add(user_id)
            return "Authenticated! Type '{}' for more options".format(HELP)
        return "Wrong password!"

    def parse_message(self, string):
        commands = string.splitlines()
        response = ""
        for command in commands:
            if command:
                response += self.parse_command(command)
        return response

    def command_valid(self, cmd_arr):
        cmd = cmd_arr[0].lower()
        return (
            (cmd in COMMANDS) and
            (
                (len(cmd_arr) == 1 and (cmd == HELP or cmd == PRINT)) or
                (cmd == TOPIC or cmd == HOST) or
                (len(cmd_arr) == 2)
            )
        )

    def parse_command(self, command):
        cmd_arr = command.split(' ')
        if self.command_valid(cmd_arr):
            return COMMANDS[cmd_arr[0].lower()](cmd_arr)
        else:
            return "Could not parse command: {0}. Please enter '{1}' for help!".format(command, HELP)

handler_class = HelloWorldHandler
