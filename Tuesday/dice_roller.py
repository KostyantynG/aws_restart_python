from random import randint

dice_number = int(input("How many dice are we rolling? "))
dice_sides = int(input("How many sides on each die? "))

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
