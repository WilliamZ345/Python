#!/usr/bin/python

file = open("mynum2.txt", "r")

totalvalue = 0
y = 0
for x, z in file:
   y = y + 1 
   totalvalue = totalvalue + int(x)
   print "x is:", x, "total value =" , totalvalue
print "You added",y,"numbers in with this array."
file.close()

