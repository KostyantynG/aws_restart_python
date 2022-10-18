
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
    print(char)
print("===============")

# Write a while loop that does the same thing!
counter = 0
while len(word) > counter:
    print(word[counter])
    counter += 1
print("===============")

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)

limit = 100
while limit <= 140:
    if limit % 2 == 0:
        print(limit)
    limit += 1
print("===============")

# Write a for loop that does the same thing (with range())
for number in range (100,141,2):
    print(number)
print("===============")

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
user_input = input("Please enter a passphrase: ")
while user_input != "sillygoose":
    user_input = input("Please enter a passphrase: ")