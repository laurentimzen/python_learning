#total number of cars
cars = 100
# amount of space in each car as a floating point number
space_in_a_car = 4.0
# number of drivers available
drivers = 30
# number of total passengers
passengers = 90
# determines the amount of cars that wont be driven
cars_not_driven = cars - drivers
# determins the amount of cars that will be driven
cars_driven = drivers
# determins the maximum number of passengers
carpool_capacity = cars_driven * space_in_a_car
# determines the average number of passengers per car 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars total."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"
