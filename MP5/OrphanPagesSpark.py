#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

def parseLine(line):
    parts = line.split(':')
    pageId = int(parts[0])
    links = parts[1].strip().split() if len(parts) > 1 else []
    return [(pageId, 0)] + [(int(link), 1) for link in links]

links = lines.flatMap(parseLine)

# Reducing to find orphan pages
orphanPages = links.reduceByKey(lambda a, b: a + b).filter(lambda x: x[1] == 0).map(lambda x: x[0])



output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (line + "\n")

# Collecting orphan page IDs
orphanPageIds = orphanPages.collect()

# Sorting lexicographically by converting IDs to strings
orphanPageIdsSortedLexicographically = sorted(orphanPageIds, key=lambda x: str(x))

# Writing sorted page IDs to the output file
for pageId in orphanPageIdsSortedLexicographically:
    output.write(str(pageId) + "\n")

output.close()


sc.stop()

