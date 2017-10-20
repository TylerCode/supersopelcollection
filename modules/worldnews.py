"""World News Sopel Module

This module will get the latest from BBC News.

Usage: 
.worldnews .wld .world

Example:
.worldnews
News....

Written by TylerCode
Released under WTFPL v2

"""

import feedparser
import sopel.module

@sopel.module.commands('worldnews', 'wld', 'world')
def worldnews(bot, trigger):
    rss_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    # use http://feeds.bbci.co.uk/news/technology/rss.xml for tech news
    rss = feedparser.parse(rss_url)
    title1 = rss.entries[0]['title'] + '.  '
    desc1 = rss.entries[0]['description'] + '.  '
    title2 = rss.entries[1]['title'] + '.  '
    desc2 = rss.entries[1]['description'] + '.  '
    title3 = rss.entries[2]['title'] + '.  '
    desc3 = rss.entries[2]['description'] + '.  '
    title4 = rss.entries[3]['title'] + '.  '
    desc4 = rss.entries[3]['description'] + '.  ' 

    intro = "The latest stories from the World section of the BBC News."
    bot.say(intro)
    bot.say(title1)
    bot.say(desc1)
    bot.say(title2)
    bot.say(desc2)
    bot.say(title3)
    bot.say(desc3)
    bot.say(title4)
    bot.say(desc4)


