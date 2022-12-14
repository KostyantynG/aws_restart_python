# Import randint
from random import randint

# Ask the number of dice
dice_number = int(input("How many dice are we rolling? "))
while dice_number > 20:
    print("Please enter an integer from 1 to 20: ")
    dice_number = int(input("How many dice are we rolling? "))
    
# Ask the number of sides for each die
dice_sides = int(input("How many sides on each die? "))
while dice_sides > 20:
    print("Please enter an integer from 1 to 20: ")
    dice_sides = int(input("How many dice are we rolling? "))

# Define the function for rolling the dice
def roll():
    for x in range(dice_number):
        number = randint(1,dice_sides)
        print(f"|{number}|", end="")

# Roll all the dice single time and ask for another round
roll()
print()
user_input = input("Roll again? ('q' to quit) ")

# Check if user wants to continue and roll the dice infinitely until user inputs 'q'
while user_input != "q":
    roll()
    print()
    user_input = input("Roll again? ('q' to quit) ")
