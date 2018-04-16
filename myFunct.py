#!/usr/bin/python
import sys


def myf1(str):
   "My first python function"
   print str
   return;

def myf2(mylist):
   mylist.append([1, 2, 3]);
   mylist.append([8, 9, 10]);
   print "Inside myf2, the numbers are: ", mylist
   print "The total element count is: ", len(mylist)
   return;

# ============= Main Program =============

myf1("Hello, my name is William");
print "This is the main function";
myf1("Help I'm trapped in this program!");

globallist = [100, 200];
print "before globallist is: ", globallist;
print "before globallist length is: ", len(globallist);
myf2(globallist);
print "after globallist is: ", globallist;
print "after globallist length is: ", len(globallist);

