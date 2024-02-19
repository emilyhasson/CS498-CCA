#!/usr/bin/env python3
#TopTitlesReducer.py

import sys

n = 10  # Number of top words to find
word_counts = {}


# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)
    
    word_counts[word] = word_counts.get(word, 0) + count
    

# Sort the words first by count (ascending) and then lexicographically (ascending)
# Python's tuple sorting is 'stable' and will sort by first element, then second, etc.
sorted_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]))

# top N items ( bottom of our sorted list)
top_n_words = sorted_words[-n:]

for word, count in top_n_words:
    print('%s\t%s' % (word, count))
    # print('%s\t%s' % (  ,  )) print as final output