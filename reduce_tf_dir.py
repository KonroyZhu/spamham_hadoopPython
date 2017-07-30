#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
total=0
# input comes from STDIN
tempdict={}
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
			tempdict[current_word]=current_count
        current_count = count
        current_word = word

total_words=len(tempdict)
for key in tempdict:
	sys.stdout=open("reduceoutdictham.txt","a")
	print '%s\t%s' % (key, (int(tempdict.get(key))/float(total_words)))
	
