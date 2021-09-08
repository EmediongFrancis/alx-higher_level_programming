#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
akpatre = number % 10
if akpatre > 5:
    print("Last digit of", number, "is", akpatre, "and is greater than 5")
elif akpatre == 0:
    print("Last digit of", number, "is", akpatre, "and is 0")
else:
    print("Last digit of", number, "is", akpatre, "and is less than 6 and not 0")
