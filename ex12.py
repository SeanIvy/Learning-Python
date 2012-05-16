# ---------------------------------
# Header
# ---------------------------------

# LPTHW - Exercise 12
# Sean Ivy - 051012
# Exercise 12 - Prompting People

# ---------------------------------
# Start Code
# ---------------------------------

# My personal variables
# ---------------------------------

seperation = "-" *32
line = "\n%s\n" % seperation

age = "How old are you? (years)\n>"
height = "How tall are you? (inches)\n>"
weight = "How much do you weight? (pounds)\n>"

# Now the Exercise
# ---------------------------------

years = raw_input(age)
inches = raw_input(height)
pounds = raw_input(weight)

print "So; you're %s years old, %s inches tall, and %s pounds." % (
    years, inches, pounds)


# ---------------------------------
# End Code
# ---------------------------------
