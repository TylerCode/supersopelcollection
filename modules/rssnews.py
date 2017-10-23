"""RSS News Sopel Module

This module will get the latest from RSS Feeds.

Usage: 
.news<type>

Example:
.newsworld or .newstech
News....

Written by TylerCode
Released under WTFPL v2

"""

import feedparser
import sopel.module

# You can customize these both
intro = "Here is the latest on that topic"
outtro = "That's all for now."

@sopel.module.commands('newsworld')
def worldnews(bot, trigger):
    intro = "The latest stories from the World section of the BBC News."
    rss_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    getNews(rss_url,bot)

@sopel.module.commands('newstech')
def worldnews(bot, trigger):
    intro = "The latest stories from the Technology section of the BBC News."
    rss_url = 'http://feeds.bbci.co.uk/news/technology/rss.xml'
    getNews(rss_url,bot)

@sopel.module.commands('newshack')
def worldnews(bot, trigger):
    intro = "The latest stories from Hacker News."
    rss_url = 'https://news.ycombinator.com/rss'
    getNews(rss_url,bot)


def getNews(rss_url,bot):
    rss = feedparser.parse(rss_url)
    title1 = rss.entries[0]['title'] + '.  '
    desc1 = rss.entries[0]['description'] + '.  '
    title2 = rss.entries[1]['title'] + '.  '
    desc2 = rss.entries[1]['description'] + '.  '
    title3 = rss.entries[2]['title'] + '.  '
    desc3 = rss.entries[2]['description'] + '.  '
    title4 = rss.entries[3]['title'] + '.  '
    desc4 = rss.entries[3]['description'] + '.  ' 

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
    bot.say(outtro)
