#!/usr/bin/env python3
#TopTitlesMapper.py
import sys


# TODO



# Simply pass through what we receive from stdin
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    print('%s\t%s' % (word, count))

#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer

