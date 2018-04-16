#! /usr/bin/python

with open(mynumfile.txt) as f:
	content = f.readlines()


content = [x.strip() for x in content]
