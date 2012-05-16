# ---------------------------------------
# Header
# ---------------------------------------

# LPTHW - Exercise 3
# Sean Ivy - 05/08/12
# Exercise 3 - Numbers and Math

# ---------------------------------------
# Start Code
# ---------------------------------------

print "I will now count my chickens:"

# Calculate 25 + (30 / 6) because of Order of Operations. 25 + 5 = 30. Result 30
print "Hens", 25 + 30 / 6

# Calculate 100 - [(25 * 3) modulus 4]
# modulus operator produces the 'remainder' of an equation so this equation would read 100 - (75 modulus 4) and since the highest multiplication factor of 4 without going over 75 is 72; then 75 % 4 is 3. thus 100 - 3 = 97. Result 97
print "Roosters", 100 - 25 * 3 % 4  

print "Now I will count the eggs:"

# Calculate 3 + 2 + 1 - 5 + (4 % 2) - (1 / 4) + 6. Order of Operations dictates the first calculation is 1 divided by 4, since we're not using floating point, no decimals are used, this 1/4 = 0. the next operation is the modulus. (4 % 2) is 0 since 2 goes into 4 perfectly leaving no remainder. thus the equation is 3 + 2 + 1 - 5 + 0 - 0 + 6. Result 7.
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

# This will return a False result.
print 3 + 2 < 5 - 7

# Calculate 3 + 2. Result 5.
print "What is 3 + 2?", 3 + 2
# Calculate 5 - 7. Result -2.
print "What is 5 - 7?", 5 - 7

print "Oh that's why it's False."

print "How about some more."

# Returns True.
print "Is it greater?", 5 > -2
# Returns True.
print "Is it greater or equal?", 5 >= -2
# Returns False.
print "Is it less or equal?", 5 <= -2

# ---------------------------------------
# End Code
# ---------------------------------------
