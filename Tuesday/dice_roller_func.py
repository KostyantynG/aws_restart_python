from random import randint

dice_number = int(input("How many dice are we rolling? "))
while dice_number > 20:
    print("Please enter an integer from 1 to 20: ")
    dice_number = int(input("How many dice are we rolling? "))
    
dice_sides = int(input("How many sides on each die? "))
while dice_sides > 20:
    print("Please enter an integer from 1 to 20: ")
    dice_sides = int(input("How many dice are we rolling? "))

def roll():
    for x in range(dice_number):
        number = randint(1,dice_sides)
        print(f"|{number}|", end="")

roll()
print()
user_input = input("Roll again? ('q' to quit) ")
while user_input != "q":
    roll()
    print()
    user_input = input("Roll again? ('q' to quit) ")
else:
    exit()
