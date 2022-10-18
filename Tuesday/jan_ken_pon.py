from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
pc_move = num
if pc_move == 1:
    pc_move = rock
elif pc_move == 2:
    pc_move = paper
elif pc_move == 3:
    pc_move = scissors


# Ask a user to enter their move
print("=============================================================")
user_move = input("Make your move, mortal! 1 - rock, 2 - paper, 3 - scissors: ")

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move

if user_move == "1":
    user_move = rock
elif user_move == "2":
    user_move = paper
elif user_move == "3":
    user_move = scissors
else:
    print("Only 1, 2 and 3 are the options, human!");exit()
print("=============================================================")
print("Your move is: ")
print(user_move)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print()
print("And my move is: ")
print(pc_move)
print()
# Figure out who wins and print the result!

if user_move == rock and pc_move == paper:
    print("Haha, you lose!")
elif user_move == rock and pc_move == scissors:
    print("You've won!")
elif user_move == rock and pc_move == rock:
    print("It's a draw!")
elif user_move == paper and pc_move == scissors:
    print("Haha, you lose!")
elif user_move == paper and pc_move == rock:
    print("You've won!")
elif user_move == paper and pc_move == paper:
    print("It's a draw!")
elif user_move == scissors and pc_move == rock:
    print("Haha, you lose!")
elif user_move == scissors and pc_move == paper:
    print("You've won!")
elif user_move == scissors and pc_move == scissors:
    print("It's a draw!")

print("=============================================================")