# myValue="This is a string."
# print(myValue)
# print(type(myValue))
# print(str(myValue) + " is of the data type " + str(type(myValue)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print(type(thirdString))
print(str(thirdString) + " is of the data type " + str(type(thirdString)))
name = input("What is your name? ")
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))