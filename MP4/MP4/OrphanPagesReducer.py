#!/usr/bin/env python3
#OrphanPagesReducer.py
import sys

all_pages = set()
linked_pages = set()


for line in sys.stdin:
  line = line.strip()
  page_id, link = line.split('\t', 1)

  # Add page_id and link to the respective sets
  all_pages.add(page_id)
  linked_pages.add(link)

#TODO
# print(xx) print as final output
  
# Orphan pages are those in all_pages but not in linked_pages
orphan_pages = all_pages - linked_pages
# Print orphan pages in sorted order
for page_id in sorted(orphan_pages, key=int):
    print(page_id)