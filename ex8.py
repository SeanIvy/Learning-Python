# ---------------------------------
# Header
# ---------------------------------

# LPTHW - Exercise 8
# Sean Ivy - 051012
# Exercise 8 - Printing, Printing

# ---------------------------------
# Start Code
# ---------------------------------

# Set up 'formatter' variable
# ---------------------------------
formatter = "%r %r %r %r"

# Printing Now
# ---------------------------------
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# ---------------------------------
# End Code
# ---------------------------------
