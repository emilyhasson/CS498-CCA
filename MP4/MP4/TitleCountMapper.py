#!/usr/bin/env python3
#TitleCountMapper.py

import sys
import string
import re


stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


# Load stop words
# TODO
stopWords = set()
with open(stopWordsPath) as f:
    # TODO
    for line in f.readlines():
        stopWords.add(line.rstrip('\n'))





# Read delimiters into a list
#TODO 
delimiters = "[\t,;\.\?\!\-\:@\[\]\(\)\{\}_\*/]+" 

# Function to clean and split
def clean_split(s, delimiters):
    line = re.sub('\n', '', s)
    line = line.strip()
    words = re.split(delimiters, line)
    words = [i.lower() for i in words]
    words = [i for i in words if i]
    return words

# Process each line from standard input
for line in sys.stdin:
  
    # TODO
    # Normalize delimiters
    words = clean_split(line, delimiters)

    # Process each word
    for word in words:
        if word and word not in stopWords:

            print('%s\t%s' % ( word ,  1)) #pass this output to reducer


