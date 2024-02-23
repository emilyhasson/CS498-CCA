#!/usr/bin/env python3
#TopPopularLinksReducer.py
import sys

top_pages = []

for line in sys.stdin:
    line = line.strip()
    count, page = line.split('\t', 1)
    count = int(count)
    # Append a tuple with count first for sorting by count, then by page ID
    top_pages.append((count, page))

top_pages.sort()

top_pages = top_pages[-10:]

# We will reverse the list to display it in descending order of popularity
for count, page in top_pages:
    print('%s\t%s' % (page, count))
