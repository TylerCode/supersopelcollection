"""RSS News Sopel Module

This module will get the latest from RSS Feeds.

Usage: 
.rssnews <category>

Example:
.rssnews hack or .rssnews tech
News....

Written by TylerCode
Released into public domain under the unlicense.

"""

import feedparser
import sopel.module

# You can customize this
outtro = "That's all for now."

@sopel.module.commands('rssnews')
@sopel.module.example('.rssnews world')
def worldnews(bot, trigger):
    valid = False
    intro = "Here is the latest news on that topic"

    if(trigger.group(2) == 'world'):
        intro = "Here are the latest stories from the World section of the BBC News."
        rss_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
        valid = True
    if(trigger.group(2) == 'tech'):
        intro = "Stories from the Technology section of BBC News."
        rss_url = 'http://feeds.bbci.co.uk/news/technology/rss.xml'
        valid = True
    if(trigger.group(2) == 'hack'):
        intro = "Latest from Hacker News"
        rss_url = 'https://news.ycombinator.com/rss'
        valid = True
    if(trigger.group(2) == 'slash'):
        intro = "Latest from Slashdot"
        rss_url = 'http://rss.slashdot.org/Slashdot/slashdotMain'
        valid = True
    if(trigger.group(2) == 'linux'):
        intro = "Linux news from Slashdot"
        rss_url = 'http://rss.slashdot.org/Slashdot/slashdotLinux'
        valid = True
    if(trigger.group(2) == 'ubuntu'):
        intro = "News from OMG Ubuntu!"
        rss_url = 'http://feeds.feedburner.com/d0od'
        valid = True

    if(trigger.group(2) == 'list'):
        bot.reply("world tech hack slash linux ubuntu")

    if(valid == True):
        getNews(rss_url,bot,intro)
    else:
        bot.reply("Please specify a topic, for example: .rssnews world or .rssnews tech. For a full list, type .rssnews list")
        


def getNews(rss_url,bot,intro):
    rss = feedparser.parse(rss_url)
    title1 = rss.entries[0]['title'] + '.  '
    desc1 = rss.entries[0]['description'] + '.  '
    title2 = rss.entries[1]['title'] + '.  '
    desc2 = rss.entries[1]['description'] + '.  '
    title3 = rss.entries[2]['title'] + '.  '
    desc3 = rss.entries[2]['description'] + '.  '
    title4 = rss.entries[3]['title'] + '.  '
    desc4 = rss.entries[3]['description'] + '.  ' 
    title5 = rss.entries[4]['title'] + '.  '
    desc5 = rss.entries[4]['description'] + '.  ' 

    desc1 = extractLinks(desc1)
    desc2 = extractLinks(desc2)
    desc3 = extractLinks(desc3)
    desc4 = extractLinks(desc4)
    desc5 = extractLinks(desc5)
        

    bot.say(intro)
    bot.say("===========")
    bot.say(title1 + ": ")
    bot.say(desc1)
    bot.say("===========")
    bot.say(title2 + ": ")
    bot.say(desc2)
    bot.say("===========")
    bot.say(title3 + ": ")
    bot.say(desc3)
    bot.say("===========")
    bot.say(title4 + ": ")
    bot.say(desc4)
    bot.say("===========")
    bot.say(title5 + ": ")
    bot.say(desc5)
    bot.say("===========")
    bot.say(outtro)

def extractLinks(inputString):
    if("<a" in inputString):
        offset = inputString.find("<a")
        offset2 = inputString.find("/a")
        return inputString[offset:offset2]
    else:
        return inputString
