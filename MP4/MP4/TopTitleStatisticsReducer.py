#!/usr/bin/env python3
#TopTitleStatisticsReducer.py
import sys
import math


#TODO
sum_counts = 0
min_count = sys.maxsize
max_count = -sys.maxsize - 1
count_list = []
count = 0

for line in sys.stdin:
    # TODO
    line = line.strip()
    word, value = line.split('\t', 1)
    value = int(value)
    
    sum_counts += value
    count += 1
    min_count = min(min_count, value)
    max_count = max(max_count, value)
    count_list.append(value)

#TODO
    
# Calculate mean
mean = sum_counts // count

# Calculate variance
variance_sum = sum((xi - mean) ** 2 for xi in count_list)
variance = variance_sum // count


print(f'Mean\t{mean}')
print(f'Sum\t{sum_counts}')
print(f'Min\t{min_count}')
print(f'Max\t{max_count}')
print(f'Var\t{variance}')

# print('%s\t%s' % (  ,  )) print as final output
