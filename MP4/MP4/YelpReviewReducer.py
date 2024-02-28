#!/usr/bin/env python3
from operator import itemgetter
import sys

data = {}

# input comes from STDIN
for line in sys.stdin:
        line = eval(line)
        key = line['business_id']
        if key not in data:
                data[key] = {"sum": 0, "numReviews": 0}
        data[key]["sum"] += line["stars"] * len(line["text"])
        data[key]["numReviews"] += 1

scores = []
for business_id, data_dict in data.items():
        if data_dict["numReviews"] != 0:
                score = data_dict["sum"] / data_dict["numReviews"]
                scores.append((business_id, score))

for item in scores:
        print('%s\t%s' % (item[0], item[1]))