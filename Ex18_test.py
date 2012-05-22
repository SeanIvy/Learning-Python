# test of my linebreak code"

separation = "-" *50
linebreak = "\n%s\n" % separation

print "This is a test of my linebreak variable code"
print linebreak

def linebreak_new(key="-", length=50):
	print key*length

print "this is a test of my linebreak function"
linebreak_new()
print "this is a test of the linebreak with '*' and '80'."
linebreak_new("*"	,80)

print "this is a test of user input."
key_in = raw_input("type a string to use for the linebreak\n>")
len_in = raw_input("type a number to use for the line length\n>")

linebreak_new(key_in, int(len_in))

print "thanks for playing!"