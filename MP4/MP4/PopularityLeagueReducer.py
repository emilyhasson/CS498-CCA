#!/usr/bin/env python3
#PopularityLeagueReducer.py
import sys
league_counts = []

# input comes from STDIN
for line in sys.stdin:
    page, count = line.strip().split('\t')
    count = int(count)
    league_counts.append((page, count))

# Sort by counts in ascending order
league_counts.sort(key=lambda x: x[1])

# Calculate rank for each page
ranked_pages = {}
current_rank = 0
previous_count = -1
for page, count in league_counts:
    if count != previous_count:
        current_rank = len(ranked_pages)
        previous_count = count
    ranked_pages[page] = current_rank

for page in sorted(ranked_pages.keys(), key=lambda x: int(x), reverse=True):
    print('%s\t%s' % (page, ranked_pages[page]))
# print('%s\t%s' % (  ,  )) print as final output