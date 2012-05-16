# ---------------------------------------
# Header
# ---------------------------------------

# LPTHW - Exercise 5
# Sean Ivy - 05/08/12
# Exercise 5 - More Variables and Printing

# ---------------------------------------
# Start Code
# ---------------------------------------

# Variable Setup
# ---------------------------------------

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
height_cm = (height * 2.54)
weight = 180.0 # lbs
weight_k = (weight * 0.4535)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Using the Variables
# ---------------------------------------

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %f cm tall." % height_cm
print "He's %d pounds heavy." % weight
print "He's %g kilograms heavy." % weight_k
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %g, and %g. I get %g." % (age, height_cm, weight_k, age + height_cm + weight_k)

# ---------------------------------------
# End Code
# ---------------------------------------
