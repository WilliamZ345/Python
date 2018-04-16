#! /usr/bin/python

file = open("mysecret.txt","w")


for x in range (0, 5):
	file.write("Hello world\n")
	file.write("My name is William\n")

file.write("That's all!\n")
file.close()
