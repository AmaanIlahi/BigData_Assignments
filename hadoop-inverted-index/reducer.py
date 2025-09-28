#!/usr/bin/env python3
import sys

current_word = None
doc_set = set()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    word, doc_id = line.split("\t", 1)

    if current_word == word:
        doc_set.add(doc_id)
    else:
        if current_word:
            sorted_docs = sorted(doc_set)
            print("{}\t{}".format(current_word, ",".join(sorted_docs)))
        current_word = word
        doc_set = {doc_id}

if current_word:
    sorted_docs = sorted(doc_set)
    print("{}\t{}".format(current_word, ",".join(sorted_docs)))
