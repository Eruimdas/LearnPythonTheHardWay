# importing necessary modules
from sys import argv
# taking arguments into variables
script, filename = argv
# opening text file
txt = open(filename)
# printing what's asked and file's text.
print(f"Here's your file {filename}:")
print(txt.read())

#print("Type the filename again:")
#file_again = input("> ")

#txt_again = open(file_again)

#print(txt_again.read())
# closing the opened text file
txt.close()
#txt_again.close()
