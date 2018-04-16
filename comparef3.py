#!/usr/bin/python
import sys

array1 = [];
array2 = [];

file = open(sys.argv[1], "r")
for line in file:
    array1.append(line);
    print line;
file.close()
file = open(sys.argv[2], "r")
for line in file:
    array2.append(line);
    print line;
file.close()
x = 0
for j in range(len(array1)):
    x=x+1;  
    if (array[j] == array2[i]):
        print "These two values match!";
    else:
        j=j+1; 
        print sys.argv[1], ": line number: ", x, "is ", array1[i];
        print sys.argv[2], ": line number: ", x, "is ", array2[i];
 




file.close()
