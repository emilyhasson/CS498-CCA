#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO

def parseLine(line):
    parts = line.split(':')
    pageId = int(parts[0])
    linkedPages = parts[1].strip().split() if len(parts) > 1 else []
    return [(int(link), 1) for link in linkedPages]

links = lines.flatMap(parseLine)

linkCounts = links.reduceByKey(lambda a, b: a + b)

topLinks = linkCounts.takeOrdered(10, key=lambda x: (-x[1], x[0]))

# Now sort these topLinks lexicographically by their page ID
topLinksSortedLexicographically = sorted(topLinks, key=lambda x: str(x[0]))

output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")

for (pageId, count) in topLinksSortedLexicographically:
    output.write(f"{pageId}\t{count}\n")

output.close()


sc.stop()

