# ---------------------------------
# Header
# ---------------------------------

# LPTHW - Exercise 14
author = "Sean Ivy - 051612"
title = "Exercise 14 - Prompting and Passing"

# ---------------------------------
# Start Code
# ---------------------------------

# My personal header
# ---------------------------------

seperation = "-" *50
line = "\n%s\n" % seperation

from sys import argv

script, user_name = argv

print seperation
print "Output of script", script, "commencing."
print seperation
print title
print author
print "%s\n" % seperation

# Now the Exercise
# ---------------------------------

prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

print line

print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print"""
Alright, so you said %r about liking me.
You live in %s, wherever that is,
and you have a %s computer. Nice!
""" % (likes, lives, computer)

# ---------------------------------
# End Code
# ---------------------------------
