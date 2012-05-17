# ------------------------------------------------
#					  Header
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex16.html
# ------------------------------------------------

# I like to add line breaks into my output,
# these variables allow me to do that easily
# and cohesively.

separation = "-" *50
line = "\n%s\n" % separation

# ------------------------------------------------

from sys import argv

script, filename = argv

print "%s\n" % separation
print "we're going to erase %s." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print line
print "Opening the file..."
target = open(filename, 'w' 'r')

print line

print "Deleting the file contents..."
target.truncate()

print line

print "Now I'm going to ask you for three lines of text.\n"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print line

print "I'm going to write these lines to the file..."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print line

print "And finally, we close it, saving the changes...."
target.close()

print line

print "Now, Let's display the output of that file..."

print line

txt = open(filename)
print txt.read()
txt.close()
print line

# ------------------------------------------------
#				  End Script
# ------------------------------------------------