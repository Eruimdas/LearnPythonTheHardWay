# assigning value 100 to the variable cars
cars = 100
# assigning value 4 to the variable space_in_a_car
space_in_a_car = 4
# assigning value 30 to the variable drivers
drivers = 30
# assigning value 90 to the variable passengers
passengers = 90
# computing value of cars_not_driven
cars_not_driven = cars - drivers
# assigning value of drivers to cars_driven
cars_driven = drivers
# computing value of carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# computing value of average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Study Drills:
# The error happened because variable was not initialized.
# Nothing happens because all of other variables are integers.
