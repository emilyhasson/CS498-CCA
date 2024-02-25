#!/usr/bin/env python3
#YelpReviewMapper.py

import sys
import string
import json

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
    stopWords = f.read().split('\n')


with open(delimitersPath) as f:
    delimiters = f.read()
    # delimiters = f.readline()
    # delimiters = list(delimiters)

cleaned = []
for line in sys.stdin:
    if line != "":
        # Parse JSON line
        review = json.loads(line)
        business_id = review['business_id']
        stars = int(review['stars'])
        text = review['text']

        adjusted_stars = stars - 3

        
        for delimiter in delimiters:
            text = text.strip()
            text = text.replace(delimiter, ' ')
        tokens = line.split()

        

        for token in tokens:
            token = token.strip().lower()
            if token != '' and token not in stopWords:
                cleaned.append(token)
        

        # tokens = [token for token in text.split() if token and token not in stopWords]

        # translator = str.maketrans(delimiters, ' ' * len(delimiters))
        # tokens = text.translate(translator).split()
        # tokens = [token for token in tokens if token and token not in stopWords]


        review_length = len(cleaned)

        score = adjusted_stars * review_length
        print('%s\t%s' % (business_id, score))
    # print('%s\t%s' % (  ,  )) pass this output to reducer
