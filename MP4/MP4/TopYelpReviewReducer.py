#!/usr/bin/env python3
#TopYelpReviewReducer.py
import sys

# scores = {}
scores = []

for line in sys.stdin:
    # line = line.strip()
    # if line == " ":
    #     continue

    if len(line.split()) != 2:
        continue
    business_id, avg_score = line.split()

    avg_score = float(avg_score)

    scores.append((business_id, avg_score))

sorted_scores = sorted(scores, key=lambda x: x[1])
top_businesses = sorted_scores[-10:]
# top_businesses_sort = sorted(top_businesses.items(), key=lambda x: (x[1], x[0]), reverse=True)

# top_businesses = top_businesses[-N:]

# for business in reversed(top_businesses_sort):
#     print('%s\t%s' % business)

for business in top_businesses:
    print(business[0])