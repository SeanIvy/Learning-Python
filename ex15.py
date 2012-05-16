# ---------------------------------
# Header
# ---------------------------------

# http://learnpythonthehardway.org/book/ex15.html
# Sean Ivy - 051612
# Exercise 15 - Prompting and Passing

# ---------------------------------
# Start Code
# ---------------------------------

# My personal header
# ---------------------------------

# This sets a variable that produces a line of dashes
seperation = "-" *50
# This sets a variable that references the line of dashes and places a line break before and after it.
line = "\n%s\n" % seperation

# sys is a group of system specific modules, this line tells my program to load the 'argv' module from sys.
from sys import argv

# this line gets values from the argv array, when we start the script originally we set these values. (i.e.: 'python [script name] [file name]'
script, filename = argv

# This prints the line of dashes set up before and adds a line break before it.
print "\n%s" % seperation
# I set this up as a joke, won't be on future scripts.
print "Output of script", script, "."
# This prints the line of dashes set up before and adds a line break after it.
print "%s\n" % seperation

# Now the Exercise
# ---------------------------------

# This is setting up a variable, as far as I can tell the variable 'txt' is set to get the text from whatever filename we specify when starting the script.
txt = open(filename)

# This line let's the user know we're about to print to the screen the text of whatever file was specified in argv (when opening the script).
print "Here's your file, %r:\n" % filename

# This line, as far as I know, opens the txt file specified when running the script, and then outputs the text to screen. I'm not sure what arguments *can* be called in the parens, though I'm assuming it can output database info too.
print txt.read()

# This prints the line of dashes set up before and adds a line break after it.
print "%s\n" % seperation

print "I'll also ask you to type it again:"
file_again = raw_input(">")

txt_again = open(file_again)

print "\n", txt_again.read()

# This prints the line of dashes set up before
print seperation

# ---------------------------------
# End Code
# ---------------------------------
