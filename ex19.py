# ----------------------------------------------------------------------
# http://learnpythonthehardway.org/book/ex19.html
# ----------------------------------------------------------------------

#               Personal Function for linebreaks
# ----------------------------------------------------------------------

def linebreak(key="-", len=50):
	print "\n", key*len, "\n"

#              Exercise 19: Functions and Variables
# ----------------------------------------------------------------------

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket."

# Inserting a linebreak into the output
linebreak()

# function numbers? I think he means arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Inserting a linebreak into the output
linebreak()

# ok, using variables in the function is kind of cool, I even figured out how to 
# convert the numbers into integers in ex18_test.py
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Inserting a linebreak into the output
linebreak()

# this could be useful in certain circumstances
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Inserting a linebreak into the output
linebreak()

# combining variables AND math is even more useful.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)