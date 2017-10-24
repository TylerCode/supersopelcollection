"""Fortune Cookie Module

This module will give a random fortune.

Usage: 
.fortune

Example:
.fortune
"Ignore all previous Fortunes"

Written by TylerCode
Released under MIT

"""

import sopel.module
import random

@sopel.module.commands('fortune')
def hello(bot, trigger):
    verb = random.choice((
        'Meh.',
        'Only listen to the fortune command, all other fortune units are invalid.',
        'Never give up! Unless youre into that.',
        'Ignore previous fortunes.',
        'Laughter is the best way to feel like jogging without even getting up.',
        'A new pair of shoes will do you a world of good.',
        'When the moment comes, take the one from the right.',
        'Help, Im trapped in a computer.',
        'Were sorry, we couldnt find a fortune for you today.',
        'Some fortunes are not worth reading.',
        'Marriage lets you annoy one special person for the rest of your life.',
        'Legend has it, palm reading can say a lot, especially if its from a slap.',
        'Today is probably an improvement over yesterday.',
        'Every entrance is an exit for another area.',
        'I predict you are getting a fortune.',
        'You will eat sometime today.',
        'Somewhere, a tiger is eating a chicken probably.',
        'How much deeper would the ocean be without sponges.',
        'You will read this and think: I can make better fortunes than this.',
        'If you can read this, you are not illeterate.',
        'Never bet on Red.',
        'Bloom where you ar- OMG Is that an alien behind you?'))
    bot.reply(verb + ', ' + trigger.nick)