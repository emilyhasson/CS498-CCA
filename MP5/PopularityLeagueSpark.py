#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
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


leagueIds = sc.textFile(sys.argv[2], 1)

#TODO

leagueIdsList = leagueIds.map(lambda line: int(line)).collect()
broadcastLeagueIds = sc.broadcast(set(leagueIdsList))

# Filtering to get counts for pages only in the league
leagueLinkCounts = linkCounts.filter(lambda x: x[0] in broadcastLeagueIds.value)


# Collecting popularity counts for league pages
popularityCounts = leagueLinkCounts.collectAsMap()

def calculateRank(pageId, counts):
    lessPopular = sum(1 for count in counts.values() if count < counts[pageId])
    return lessPopular

# Calculating ranks for each page in the league
ranks = [(pageId, calculateRank(pageId, popularityCounts)) for pageId in popularityCounts]


output = open(sys.argv[3], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")

# Sorting by page ID for consistent output
sortedRanks = sorted(ranks, key=lambda x: str(x[0]))

# Writing results to the output file
for (pageId, rank) in sortedRanks:
    output.write(f"{pageId}\t{rank}\n")

output.close()


sc.stop()

