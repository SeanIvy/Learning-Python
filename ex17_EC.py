# http://learnpythonthehardway.org/book/ex17.html
# Extra Credit - How small can we get this script?
from sys import argv

script, from_file, to_file = argv
input = open(from_file)
indata = input.read()

print "Ready to copy %s to %s. Hit RETURN to continue, CTRL-C to abort" % (from_file,  to_file)
raw_input(">")

output = open(to_file, 'w')
output.write(indata)
output.close()
input.close()