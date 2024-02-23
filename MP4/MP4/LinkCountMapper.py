#!/usr/bin/env python3
# LinkCountMapper.py
import sys


for line in sys.stdin:
    line = line.strip()
    page_id, links = line.split(': ', 1)
    linked_pages = links.split()
    for linked_page in linked_pages:
        print('%s\t%s' % (linked_page, 1))
  # print('%s\t%s' % (  ,  )) pass this output to reducer
