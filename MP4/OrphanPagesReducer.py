#!/usr/bin/env python3
#OrphanPagesReducer.py
import sys

orphan_candidates = set()
linked_pages = set()

for line in sys.stdin:
    line = line.strip()
    page_id, links = line.split('\t', 1)
    linked_pages_ids = links.split()

    # Add to orphan candidates if it's not already linked
    if page_id not in linked_pages:
        orphan_candidates.add(page_id)

    for linked_id in linked_pages_ids:
        # If this linked_id is a new page and not the page itself, remove from orphan candidates
        if linked_id != page_id and linked_id in orphan_candidates:
            orphan_candidates.remove(linked_id)
        
        # Keep track of all linked pages to exclude them from orphans later
        linked_pages.add(linked_id)

# Orphan pages are those which are not in linked_pages
orphan_pages = orphan_candidates - linked_pages

# Print orphan pages in sorted order
for page_id in sorted(orphan_pages, key=int):
    print('%s' % (str(page_id))) 