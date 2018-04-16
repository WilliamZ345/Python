#!/usr/bin/python
import sys

for filename in sys.argv[1:]:
   file = open(filename, "r")
   for line in file:
      print line,
   file.close()
