#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
import re
from pyspark import SparkConf, SparkContext


stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

# Reading stopwords
with open(stopWordsPath) as f:
    stopWords = set(f.read().splitlines())

# Reading delimiters
with open(delimitersPath) as f:
    delimiters = f.read().strip()


conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[3], 1)

#TODO

# Function to tokenize titles using delimiters
def tokenize_title(title):
    # Replace each delimiter in delimiters with a space
    for delimiter in delimiters:
        title = title.replace(delimiter, ' ')
    # Tokenize by splitting on space, filter out stopwords and empty tokens, then convert to lowercase
    return [word.lower() for word in title.split() if word and word.lower() not in stopWords]

# Applying the tokenization and filtering process
tokens = lines.flatMap(tokenize_title)

# Counting words
wordCounts = tokens.map(lambda word: (word, 1)).reduceByKey(lambda a,b: a+b)

# Sorting and selecting top 10
# Since you need to sort by count and then by the word itself for ties, you'll need to perform a custom sort
topWords = wordCounts.takeOrdered(10, key=lambda x: (-x[1], x[0]))

# Sorting the top words alphabetically
topWordsSortedAlphabetically = sorted(topWords, key=lambda x: x[0])


outputFile = open(sys.argv[4],"w")

#TODO
#write results to output file. Foramt for each line: (line +"\n")

# Writing results to the output file
for (word, count) in topWordsSortedAlphabetically:
    outputFile.write(f"{word}\t{count}\n")
outputFile.close()


sc.stop()
