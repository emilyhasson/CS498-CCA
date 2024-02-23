#!/usr/bin/env python3
#OrphanPagesMapper.py
import sys


for line in sys.stdin:
  line = line.strip()
  page_id, links = line.split(': ', 1)
  linked_pages = links.split()
  # print('%s\t%s' % (  ,  )) pass this output to reducer

  for link in linked_pages:
    print('%s\t%s' % (page_id, link))  