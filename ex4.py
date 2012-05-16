# ---------------------------------------
# Header
# ---------------------------------------

# LPTHW - Exercise 4
# Sean Ivy - 05/08/12
# Exercise 4 - Variables and Names

# ---------------------------------------
# Start Code
# ---------------------------------------

# Setting up Variables
# ---------------------------------------
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Using Variables
# ---------------------------------------
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity," people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# ---------------------------------------
# End Code
# ---------------------------------------
