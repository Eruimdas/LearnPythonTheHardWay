# initializing a variable with a value
types_of_people = 10
# initializing a string value with text within text.
x = f"There are {types_of_people} types of people."

# initializing a string variabla with a value
binary = "binary"
# initializing a string variable with a value
do_not = "don't"
# initializing a string value with text within text.
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# printing a string with a string in it.
print(f"I said: {x}")
# printing a string with a string in it.
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# printing a string with a string in it.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
