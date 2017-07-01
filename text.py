import os

text = ("Have a good day!")

filename = "Hello.txt"

file = open(filename, "r")

for line in file:
	print line,

print text

