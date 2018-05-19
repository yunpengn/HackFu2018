#!/usr/bin/python3
from random import randint

# Gets the information from standard input.
length = int(input("Please enter the length for the list: "))
lowerBound = int(input("Please enter the lower bound for the range of integer values: "))
upperBound = int(input("Please enter the upper bound for the range of integer values: "))

# Returns an integer between a certain lower bound & upper bound (both inclusive).
def randBetween(lower, upper):
	return randint(lower, upper)

# Initiates and generates a list of (pseudo-)random integers.
myList = [randBetween(lowerBound, upperBound)]
minNum = myList[0]
maxNum = myList[0]
mySum = myList[0]
for _ in range(length):
	# Appends a new random integer.
	newNum = randBetween(lowerBound, upperBound)
	myList.append(newNum)
	# Includes it into the sum.
	mySum += newNum
	# Updates the minimum value if necessary.
	if newNum < minNum:
		minNum = newNum
	# Updates the maximum value if necessary.
	if newNum > maxNum:
		maxNum = newNum

print("\nSequence: ", end = "")
print(myList)
print()
print("List length: {:d}".format(length))
print("Largest integer: {:d}".format(maxNum))
print("Smallest integer: {:d}".format(minNum))
print("Sum: {:d}".format(mySum))
print("Average: {:.1f}".format(mySum / length))
