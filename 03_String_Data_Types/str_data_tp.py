
# assigning a var and printing it
myString = "This is a string."
print(myString)

# retrive the type of var
print(type(myString))

# converting the value of the var to the string
print(str(myString) + " is of the data type " + str(type(myString)))

# creatinting and concatenate strings 
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# creating an input and printitng it
name = input("What is your name? ")

print(name)

# creating other inputs
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

# implement the inputs to one string
print("{}, you like a {} {}!".format(name,color,animal))