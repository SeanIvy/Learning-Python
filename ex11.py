# ---------------------------------
# Header
# ---------------------------------

# LPTHW - Exercise 11
# Sean Ivy - 051012
# Exercise 11 - What Was That?

# ---------------------------------
# Start Code
# ---------------------------------

# My personal variables
# ---------------------------------

seperation = "-" *32
line = "\n%s\n" % seperation


# Now the Exercise
# ---------------------------------

print "How old are you?",
age = raw_input()
print line

print "How tall are you?",
height = raw_input()
print line

print "How much do you  weigh?",
weight = raw_input()
print line

print "So, you're %r years old, %r tall, and %r heavy?" % (
    age, height, weight)

# ---------------------------------
# End Code
# ---------------------------------
