#!/usr/bin/env python3
import sys
import os
import re

# Get filename (docID) from Hadoop environment
pathname = os.environ.get('mapreduce_map_input_file')
doc_id = os.path.basename(pathname) if pathname else "unknown"

for line in sys.stdin:
    line = line.strip().lower()
    # Remove non-alphanumeric characters
    line = re.sub(r'[^a-z0-9\s]', ' ', line)
    words = line.split()
    for word in words:
        if word:  # ignore blanks
            print("{}\t{}".format(word, doc_id))
