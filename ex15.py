# ---------------------------------
# Header
# ---------------------------------

# LPTHW - Exercise 15
author = "Sean Ivy - 051612"
title = "Exercise 15 - Prompting and Passing"

# ---------------------------------
# Start Code
# ---------------------------------

# My personal header
# ---------------------------------

seperation = "-" *50
line = "\n%s\n" % seperation

from sys import argv

script, filename = argv

print seperation
print "Output of script", script, "."
print seperation
print title
print author
print "%s\n" % seperation

# Now the Exercise
# ---------------------------------

txt = open(filename)

print "Here's your file, %r:\n" % filename
print txt.read()

print "%s\n" % seperation

print "I'll also ask you to type it again:"
file_again = raw_input(">")

txt_again = open(file_again)

print "\n", txt_again.read()

print seperation

# ---------------------------------
# End Code
# ---------------------------------
