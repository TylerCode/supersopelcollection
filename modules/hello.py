# Written by TylerCode
# Released under WTFPL v2

# Super simple, nothing special

import sopel.module
import random

@sopel.module.commands('hello', 'hi')
def hello(bot, trigger):
    verb = random.choice(('Hey!', 'Hello!', 'Hi!', 'Hola', 'Heyoo', 'Hey', 'Hello', 'Hi'))
    bot.say(verb)