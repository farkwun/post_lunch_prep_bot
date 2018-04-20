# See readme.md for instructions on running this code.  
from typing import Any
from os import environ

AUTH_IDS = set()

PASSWORD = "prep"

HELP = "help"
TOPIC = "topic"
RESOURCE = "resource"
ONE = "one"
TWO = "two"
PRINT = "print"

ENV_RESOURCE = "PLP_RESOURCE"
ENV_TOPIC = "PLP_TOPIC"
ENV_ONE = "PLP_ONE"
ENV_TWO = "PLP_TWO"

COMMAND_IDX = 0

COMMANDS = {
    HELP: lambda command: help(command),
    TOPIC: lambda command: set_topic(command),
    RESOURCE: lambda command: set_resource(command),
    ONE: lambda command: set_one(command),
    TWO: lambda command: set_two(command),
    PRINT: lambda command: print_setup(command)
}

def help(command):
    return ("Welcome to Post-lunch Prep Setup!\n\n" + 
            "To set today's topic, enter '{} <topic_title>'\n".format(TOPIC) + 
            "To set today's resource, enter '{} <link>'\n".format(RESOURCE) + 
            "To set the first question, enter '{} <link>'\n".format(ONE) + 
            "To set the second question, enter '{} <link>'\n".format(TWO) +
            "To output today's setup, enter '{}'\n\n".format(PRINT) +
            "Separate commands by line breaks!"
    )
def set_resource(command):
    environ["PLP_RESOURCE"] = command[1]
    return ("Set resource to {}\n".format(get_env(ENV_RESOURCE)))
def set_topic(command):
    environ["PLP_TOPIC"] = command[1]
    return ("Set topic to {}\n".format(get_env(ENV_TOPIC)))
def set_one(command):
    environ["PLP_ONE"] = command[1]
    return ("Set first question to {}\n".format(get_env(ENV_ONE)))
def set_two(command):
    environ["PLP_TWO"] = command[1]
    return ("Set second question to {}\n".format(get_env(ENV_TWO)))
def print_setup(command):
    return("Today's setup is:\n"
           "Topic: {0}\n\n"
           "Resource :{1}\n\n"
           "First q: {2}\n\n"
           "Second q: {3}\n\n".format(
               get_env(ENV_TOPIC),
               get_env(ENV_RESOURCE),
               get_env(ENV_ONE),
               get_env(ENV_TWO)
           )
           )

def get_env(key):
    return environ.get(key, "")
class HelloWorldHandler(object):
    def usage(self) -> str:
        return '''
        This is a boilerplate bot that responds to a user query with
        "beep boop", which is robot for "Hello World".

        This bot can be used as a template for other, more
        sophisticated, bots.
        '''

    def handle_message(self, message: Any, bot_handler: Any) -> None:
        user_id = message['sender_id']
        sent_msg = message['content']
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
            response += self.parse_command(command)
        return response

    def command_valid(self, cmd_arr):
        return (
            (cmd_arr[0].lower() in COMMANDS) and
            (
                (len(cmd_arr) == 1 and (cmd_arr[0] == HELP or cmd_arr[0] == PRINT)) or
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
