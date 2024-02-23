#!/usr/bin/env python3
#PopularityLeagueMapper.py
import sys


leaguePath = sys.argv[1]

league_ids = set()
with open(leaguePath) as f:
       for line in f:
              league_ids.add(line.strip())




# For each input line, output if the page ID is in the league list
for line in sys.stdin:
       page, count = line.strip().split('\t')
       if page in league_ids:
              print('%s\t%s' % (page, count))

# print('%s\t%s' % (  ,  )) pass this output to reducer
