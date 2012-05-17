# ------------------------------------------------
#					  Header
# ------------------------------------------------
# http://learnpythonthehardway.org/book/ex17.html
# ------------------------------------------------

# I like to add line breaks into my output,
# these variables allow me to do that easily
# and cohesively.

separation = "-" *50
line = "\n%s\n" % separation

# ------------------------------------------------

from sys import argv
from os.path import exists

scripts, from_file, to_file = argv
print "%s\n" % separation
print "Copying from %s to %s" % (from_file, to_file)
print line

# we could do these two on one line as well, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print separation

print "Does the output file exist? %r" % exists(to_file)
print "Ready to copy. hit RETURN to continue, CTRL-C (^C) to abort."
raw_input(">")

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()

# ------------------------------------------------
#				  End Script
# ------------------------------------------------