#!/usr/bin/env python3
#LinkCountReducer.py
import sys
from collections import defaultdict

current_page = None
current_count = 0
page = None

link_counts = defaultdict(int)


# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    page, count = line.split('\t', 1)
    count = int(count)

    if current_page == page:
        current_count += count
    else:
        if current_page:
            link_counts[current_page] = current_count
        current_count = count
        current_page = page


for page, count in link_counts.items():
    print('%s\t%s' % (page, count))

# print('%s\t%s' % (  ,  )) print as final output
    