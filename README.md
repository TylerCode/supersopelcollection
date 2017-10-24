# SuperSopelCollection

This is just a place to share some sopel modules I've written. Some of these are useful, most of them are just fun. Feel free to make a pull request if you want to add something to these or if you see any bugs. 

# Modules

## CCount (currently broken)

CCount will count the occurence of every character in a string of text. So for example, if you did the command ".ccount hello there" it would come back with the following.

e - 3
h - 2
l - 2
o - 1
r - 1
t - 1

It's not particularly useful but fin none the less.

## Fortune

Fortune will give users a random fortune from the list in the script. Feel free to add to these. I mostly kept the theme light and funny rather than trying to be more meaningful in any way. 

## Hello

Result of a hello world test, it will simply greet whoever types the command in.

## Pig

This is a "port" of a project I have in another repo. This command will convert any text into pig latin. It has an optional dash so please remove that if you don't want them in there.

## RSSNews

This is probably the module I've spent the most thought on and probably the most useful. This command will give you a news feed of the newest 5 stories from an rss feed. It's currently not that efficient so I'm hoping to make some optimizations but it does work for now. It tends to break down when the response is in HTML but I'm working on stripping that out in those cases. Adding a new feed is rather easy if you look at the code too.

# License

This code is released under the MIT License
