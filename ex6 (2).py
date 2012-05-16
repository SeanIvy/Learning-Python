# ---------------------------------
# Header
# ---------------------------------

# LPTHW - Exercise 6
# Sean Ivy - 050912
# Exercise 6 - Strings and Text

# ---------------------------------
# Start Code
# ---------------------------------

# Setting up Variables
# ---------------------------------

x = "There are %d types of people." % 10 # String within a string. x sets up the variable "There are %d types of people." %d calling a decimal string, so Python is looking for the string to be a number.
binary = "binary" # variable binary, calling string "binary". This is showing how double quotes makes it a string.
do_not = "don't" # Reinforcing the message from line 17. This time in the form of a contraction.
y = "Those who know %s and those who %s." % (binary, do_not) # now 2 strings within a string. y sets up the variable "Those who know %s (string call) and those who %s (another string call)." Line 19 shows how to call multiple variables into the same string.

# Using the Variables
# ---------------------------------

print x
print y

print "I said: %r." % x # Talk to steve about the use of %r here instead of %s.
print "I also said: '%s' ." % y # Just a call back to the variable y, with 2 additional strings inserted into this string.

# Setting up more Variables
# ---------------------------------

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # I believe %r is used here because the string will call back to a function call (False) instead of a string?

# Using more Variables
# ---------------------------------

print joke_evaluation % hilarious # Printing the variable joke_evaluation, and setting up what string the %r in 'joke_evaluation' is calling.

# Last Variable setup and use
# ---------------------------------

w = "This is the left side of..."
e = "a string with a right side."

print w + e # Line 47 is what I call a 'knot' as it ties two strings together.

# ---------------------------------
# End Code
# ---------------------------------
