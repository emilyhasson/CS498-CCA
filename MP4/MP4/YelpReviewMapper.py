#!/usr/bin/env python3

import sys
import string
import json

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
        stopWords = f.read().split('\n')

with open(delimitersPath) as f:
        delimiters = f.read()

out = []
for line in sys.stdin:
        data = json.loads(line) 
        stars = data['stars'] - 3


        text = data['text']
        cleaned = []
        for delimiter in delimiters:
            text = text.strip().replace(delimiter, ' ')
        tokens = line.split()
        for token in tokens:
            if token.isspace() or token.strip() == '':
                continue
            if (token.strip().lower() not in stopWords):
                cleaned.append(token.lower().strip())

        tup = {}
        tup['business_id'] = data["business_id"]
        tup['stars'] = stars
        tup['text'] = cleaned
        out.append(tup)

for item in out:
    print(item)