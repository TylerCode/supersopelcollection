"""Character Counter for Sopel

Simply counts the number of characters in a block of text
Ported this from:
https://github.com/TylerCode/halla-varlden/blob/master/3-CountVowels.py

Usage: 
.ccount .characters .charcount

Example:
.ccount taco time

Written by TylerCode
Released under WTFPL v2

"""

import sopel.module
import random

@sopel.module.commands('ccount', 'characters', 'charcount')
def vcount(bot, trigger):
    #Input processing
    inputString = trigger.group(2)
    inputString = inputString.lower()
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','.',',','!','?','"',"'",'-','_','&',';',':','*','(',')']
    counts = []

    countThatShiz(inputString)

    loops = 0

    bot.reply("Breakdown of text block")

    for r in counts:
        if r != 0:
            bot.reply(letters[loops] + " - " + str(r))
        loops += 1


    bot.reply("That's all folks")

def countThatShiz(r):
    for a in letters:
        counted = 0
        counted = r.count(a)
        counts.append(counted)


