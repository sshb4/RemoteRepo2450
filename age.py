#create a simple python program that tries to guess your age. You write the program. It should do these things:

#Greet you and tell you that it is going to try to guess your age.
#Ask for your name
#Guess an age between 15 and 30 and let you answer 'y' or 'n'
#If it guesses right, it exults and says "<your name> is <age> years old." and quit.
#If it guesses wrong, it says "Rats." and tries to guess again.

import random

print("Hello, I am going to guess your age.")
name = input("What is your name? ")

guess = random.randint(15,30)

answer = input("Yes (y) or no (n) ? ")
if answer == "y":
	print(name, " is", age, " years old.")
	return;	
if answer == "n":
	print("Rats.")

while answer != "y":
	guess = random.randint(15,30)
#need to move things around


