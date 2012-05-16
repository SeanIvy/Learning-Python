# ---------------------------------
# Header
# ---------------------------------

# LPTHW - Exercise 10
# Sean Ivy - 051012
# Exercise 10 - What Was That?

# ---------------------------------
# Start Code
# ---------------------------------

seperation = "-" *32
line = "\n%s\n" % seperation

# Example one
# ---------------------------------
print seperation
# spaces in code are ignored
print "I am 6'2\" tall." # escape double-quote inside a string.
print 'I am 6\'2" tall.' # escape single-quote inside a string.
print line


# Example two
# ---------------------------------
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass""" # Putting """ on a new line causes a \n break

print tabby_cat

print line

print persian_cat

print line

print backslash_cat

print line

print fat_cat

print seperation
# ---------------------------------
# End Code
# ---------------------------------
