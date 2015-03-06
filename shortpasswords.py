#!/usr/bin/python
# This script takes a password list and spits out a new password list 
# with only passwords that are a given length or shorter.
import sys

if sys.argv.__len__() == 1:
	source = raw_input("Enter the source file: ")
	length = int(raw_input("Enter the max length of password: "))
if sys.argv.__len__() == 2:
	source = sys.argv[1]
	length = int(raw_input("Enter the max length of password: "))
if sys.argv.__len__() == 3:
	source = sys.argv[1]
	length = int(sys.argv[2])

# print "length = " + length
sourcefile = file(source , "r")
destfile = file(source + "." + str(length) + "max" , "w")
linesread = 0
lineswritten = 0

for x in sourcefile.readlines():
	linesread += 1
#	print "x.__len__ = " + str(x.__len__())
#	print "length = " + str(length)
	if x.__len__() <= length:
#		print "running"
		destfile.write(x)
		lineswritten += 1

print str(linesread) + "lines read"
print str(lineswritten) + "lines written"

