#!/usr/bin/python
import sys
if (len(sys.argv)!=3):
   print "Usage: ", sys.argv[0], " file1 file2"; 
   quit();   

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
x = 0
for i in range(len(array1)):
    x=x+1;  
    if (array1[i] != array2[i]):
        print sys.argv[1], ": line number: ", x, "is ", array1[i];
        print sys.argv[2], ": line number: ", x, "is ", array2[i];
    else:
        print "These two values match!"

 




file.close()
