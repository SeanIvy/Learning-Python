# -------------------------------------------------
# http://learnpythonthehardway.org/book/ex20.html
# -------------------------------------------------
#               Personal Variables
# -------------------------------------------------
def linebreak(key="-", len=50):
	print "\n", key*len, "\n"

#                Exercise 20: Functions and Files
# -------------------------------------------------

# ah, our old friend argv
from sys import argv

# setting the arguments present in how we ran our script 
script, input_file = argv

# function to print the whole text file
def print_all(f):
	print f.read() # we've used this previously, I'm guessing f.read means read and output to screen whatever file is specified as argument 'f'

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

# Inserting a linebreak
linebreak()

print "Now let's rewind, kind of like a tape."

rewind(current_file)

# Inserting a linebreak
linebreak()

print "let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# Inserting a linebreak
linebreak()
