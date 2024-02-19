#!/usr/bin/env python3
#TitleCountMapper.py

import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


# Load stop words
# TODO
stopWords = set()
with open(stopWordsPath) as f:
    # TODO
    for line in f:
        stopWords.add(line.strip().lower())





# Read delimiters into a list
#TODO 
with open(delimitersPath) as f:
    # TODO
    delimiters = f.read().strip()

# Function to replace all delimiters with a space
def replace_delimiters(s, delimiters):
    for delimiter in delimiters:
        s = s.replace(delimiter, ' ')
    return s

# Process each line from standard input
for line in sys.stdin:
  
    # TODO
    # Normalize delimiters
    line = replace_delimiters(line, delimiters)
    # Tokenize the line
    words = line.split()
    # Process each word
    for word in words:
        word = word.lower().strip(string.punctuation)
        if word and word not in stopWords:

            print('%s\t%s' % ( word ,  1)) #pass this output to reducer


