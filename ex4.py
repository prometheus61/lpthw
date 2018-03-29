# sets the value of the variable cars to 100
cars = 100
# sets the number of seats in the car to 4.0 floating point, not necessary thoguh as cant use partial seats
space_in_car = 4.0
# sets the variable to 30
drivers = 30
# sets passengers to 90
passengers = 90
# sets the variable to be the result of the calculation
cars_not_driven = cars - drivers
# sets the variables to be the same as the other
cars_driven = drivers
# variable is the result of the calculation
carpool_capacity = cars_driven * space_in_car
# as above, result of the calculation
average_passengers_per_car = passengers/cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There wil be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."

# car_pool_capacity is not defined as a variable above so the program cannot find items

