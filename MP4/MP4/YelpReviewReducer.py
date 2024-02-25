#!/usr/bin/env python3
#YelpReviewReducer.py
from operator import itemgetter
import sys

scores = {}
review_counts = {}

# input comes from STDIN
for line in sys.stdin:
    # line = line.strip()
    business_id, weighted_score = line.split('\t')
    weighted_score = float(weighted_score)

    if business_id in scores:
        scores[business_id] += weighted_score
        review_counts[business_id] += 1
    else:
        scores[business_id] = weighted_score
        review_counts[business_id] = 1

for business_id in scores:
    avg_score = scores[business_id] / review_counts[business_id]
    print('%s\t%s' % (business_id, avg_score))
# print('%s\t%s' % (  ,  )) print as final output
