#Declaring number of cars
cars = 100
#Assigning passenger capacity to each car
space_in_a_car = 4.0
#Assigning numbers of drivers available to the variable drivers
drivers = 30
#Assigning number of passengers to the variable passengers
passengers = 90
#Evaluating number of cars driven and simultaneously assigning it to the vaiable
cars_not_driven = cars - drivers
#drivers although already used is now being declared
cars_driven = drivers
#Calculating carpool capacity using an expression in variables
carpool_capacity = cars_driven * space_in_a_car
#Calculating average passengers using other variables
average_passengers_per_car = passengers / cars_driven

#Now printing number of cars using the variable
print "There are", cars, "cars available."
#Printing number of drivers using variable drivers
print "There are only", drivers, "drivers available"
#Printing cars not driven using the variable
print "There will be", cars_not_driven, "empty cars today."
#Printing carpool capacity using the variable
print "We can transport", carpool_capacity, "people today."
#Printing number of passengers to be carpooled
print "We have", passengers, "to carpool today."
#Printing average passengers using the variable
print "We need to put about", average_passengers_per_car, "in each car."