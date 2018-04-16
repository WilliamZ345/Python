#!/usr/bin/python

file = open("student.data", "r")


myName = raw_input("Enter your name: ")
noMatch = 1 
print "Your input is: ", myName

totalvalue = 0
y = 0
for x in file:
   y=y+1
   name, bod, math, science, writing, art, music = x.rstrip().split(',') 
   
   if myName == name:
       print y,"  name:", name, "  bod:", bod, " math:", math, " science:", science, " writing:", writing, " art:", art, " music:", music 
       noMatch = 0      


if noMatch == 1:
    print "The name you inputted does not exist on this list."

file.close()

