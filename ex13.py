# ---------------------------------
# Header
# ---------------------------------

# LPTHW - Exercise 13
# Sean Ivy - 051012
# Exercise 13 - Parameters, Unpacking, Variables

# ---------------------------------
# Start Code
# ---------------------------------

# My personal variables
# ---------------------------------

seperation = "-" *32
line = "\n%s\n" % seperation

# Now the Exercise
# ---------------------------------

from sys import argv

prompt = "Please give me a %s Variable.\n>" 

first = raw_input(prompt % "first")
second = raw_input(prompt % "second")
third = raw_input(prompt % "third")

script = argv[0]

print seperation
print "Output of script", script, "commencing."
print seperation

print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print seperation
# ---------------------------------
# End Code
# ---------------------------------
