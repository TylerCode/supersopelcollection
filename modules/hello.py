"""Greeting/Hello module for Sopel

Includes a response to the person who called it for example:

.hi
Hello, <username>

Written by TylerCode
Released into public domain under the unlicense.

"""

import sopel.module
import random

@sopel.module.commands('hello', 'hi')
def hello(bot, trigger):
    verb = random.choice(('Hey!', 'Hello!', 'Hi!', 'Hola', 'Heyoo', 'Hey', 'Hello', 'Hi'))
    bot.say(verb + ', ' + trigger.nick)