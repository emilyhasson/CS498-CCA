#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1)

#TODO

# Extracting counts from the input
wordCounts = lines.map(lambda line: int(line.split('\t')[1]))

# Calculating statistics
totalCount = wordCounts.count()
sumCount = wordCounts.sum()
meanCount = sumCount // totalCount  # Floor division to get an integer result
minCount = wordCounts.min()
maxCount = wordCounts.max()
# Variance calculation
# Variance = (sum((xi - mean)^2)) / n
# Use map to compute the squared differences, sum them, and divide by the count
varianceCount = wordCounts.map(lambda x: (x - meanCount) ** 2).sum() // totalCount


outputFile = open(sys.argv[2], "w")
'''
TODO write your output here
write results to output file. Format
outputFile.write('Mean\t%s\n' % ans1)
outputFile.write('Sum\t%s\n' % ans2)
outputFile.write('Min\t%s\n' % ans3)
outputFile.write('Max\t%s\n' % ans4)
outputFile.write('Var\t%s\n' % ans5)
'''

# Writing the statistics to the output file
outputFile.write('Mean\t%s\n' % meanCount)
outputFile.write('Sum\t%s\n' % sumCount)
outputFile.write('Min\t%s\n' % minCount)
outputFile.write('Max\t%s\n' % maxCount)
outputFile.write('Var\t%s\n' % varianceCount)

outputFile.close()


sc.stop()

