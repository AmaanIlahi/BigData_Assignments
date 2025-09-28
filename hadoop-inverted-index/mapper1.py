#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        word, docs = line.split("\t", 1)
        doc_list = docs.split(",")
        count = len(doc_list)
        print("{}\t{}\t{}".format(word, count, ",".join(doc_list)))
    except ValueError:
        continue
