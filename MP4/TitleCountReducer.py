#!/usr/bin/env python3
#TitleCountReducer.py
from operator import itemgetter
import sys

#TODO
current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# TODO
# print('%s\t%s' % (  ,  )) print as final output
        
# Do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s' % (current_word, current_count))