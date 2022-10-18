player1_name = input("enter player 1's name: ")
player2_name = input("enter player 2's name: ")

toothpicks_number = 13
print()

while toothpicks_number > 0:
    for counter in range(toothpicks_number):
        print("|",end=" ")
    print(f"""
There are {toothpicks_number} toothpicks left
How many do you take, {player1_name} ?""")

    toothpicks_take = int(input())
    while toothpicks_take not in range (1,4):
        print("You can take only 1, 2 or 3 matchstick(s)")
        toothpicks_take = int(input())
    toothpicks_number -= toothpicks_take
    if toothpicks_number < 1:
        print(f"""{player1_name} wins!!!
        GAME OVER!!!""")
        exit()

    for counter in range(toothpicks_number):
        print("|",end=" ")
    print(f"""
There are {toothpicks_number} toothpicks left
How many do you take, {player2_name} ?""")

    toothpicks_take = int(input())
    while toothpicks_take not in range (1,4):
        print("You can take only 1, 2 or 3 matchstick(s)")
        toothpicks_take = int(input())
    toothpicks_number -= toothpicks_take
    if toothpicks_number < 1:
        print(f"""{player2_name} wins!!!
        GAME OVER!!!""")
        exit()
