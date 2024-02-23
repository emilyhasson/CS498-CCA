#!/usr/bin/env python3
#TopPopularLinksMapper.py
import sys

for line in sys.stdin:
    line = line.strip()
    page, count = line.split('\t', 1)
    print('%s\t%s' % (count, page))
