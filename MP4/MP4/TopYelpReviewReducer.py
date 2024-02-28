#!/usr/bin/env python3
import sys

data = []
for line in sys.stdin:
    if len(line.split()) == 2:
                
        id, score = line.split()
        data.append((id, float(score)))

sorted_data = sorted(data, key=lambda x: x[1])
top = sorted_data[-10:]
for item in top:
    print(item[0])