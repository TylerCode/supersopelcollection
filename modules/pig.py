"""Pig Latin Translator for Sopel

This module will translate any phrase into pig latin. Fun for the whole family!
Adapted from my pig latin code found below:
https://github.com/TylerCode/halla-varlden/blob/master/2-PigLatin.py

Usage: 
.pig <input> or .piglatin <input>

Example:
.pig That burrito was terrible
atthay urritobay asway erribletay

Written by TylerCode
Released under MIT

"""

import sopel.module
import re

@sopel.module.commands('pig', 'piglatin')
def piglatin(bot, trigger):
    inputString = trigger.group(2)
    inputString = inputString.lower()
    bot.reply(doTheBiz(inputString))



def anaize(x): #Anaize refers to ananabay, it is in charge of determining the endstring 
    return {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5,
    }.get(x, 9)

def stringSplit(r): #Splits the sentence, and returns a list
    return re.sub("[^\w]", " ",  r).split() #re.sub(pattern, repl, string, count=0, flags=0)

def removePuctuation(a): #Removes puctuation from the original string, or it will someday
    return ""


def translate(i): #Does the heavy lifting
    #Follows the rules outlined in https://en.wikipedia.org/wiki/Pig_Latin
    
    wordReturn = "" #Word to return
    firstLetter = i[0] #grabs the first letter
    
    if anaize(firstLetter) > 6: #Detects vowels 
        i = i[1:] #Removes the first letter of the word.
        wordReturn = i + "-" + firstLetter + "ay"
    else:
        wordReturn = i + "-" + "yay" #Remove the "-" from this line and the one above to get rid of the dash
        
    return wordReturn

def latinize(l): #Takes in a list of words, and returns a list of words that has been translated, 
    #just wanted to keep the loop isolated for code reusability 
    count = 0

    for s in l:
        l[count] = translate(l[count])
        count += 1 #Forgot this the first time, like a moron
    return l


def reconstruct(o): #Takes in a list of words put into pig latin, and rebuilds them into a stringSplit
    returnString = ""
    for c in o: #My hatred for python grows with this simplification. It makes it harder to read than c# or c++
        returnString += " " + c
        
    return returnString


def doTheBiz(stringy): #The main part of the program, I like things wrapped in functions
    outstring = ""
    #stringy = removePuctuation(stringy) #Put this in when complete
    listOfWords = stringSplit(stringy)
    listOfWords = latinize(listOfWords)
    outstring = reconstruct(listOfWords)
    return outstring