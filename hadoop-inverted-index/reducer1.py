#!/usr/bin/env python3
import sys

records = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split("\t")
    if len(parts) != 3:
        continue
    word, count, doc_list = parts
    records.append((word, int(count), doc_list))

records.sort(key=lambda x: (-x[1], x[0]))

for word, count, doc_list in records[:10]:
    print("{}\t{}\t{}".format(word, count, doc_list))
