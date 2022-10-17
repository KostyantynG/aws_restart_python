# String

# Either use single or double quotes
"Hello he's"
'Helllo: "lödkafglkl" '

# For Multiline Strings you can use tripple quotes
"""
sldöjfgjlk

"""
'''

dlsfkglkdfj
'''
# To print something on the terminal, use print(whatToPrint)
print("""
sldöjfgjlk

""")
print("Hello")

# To get some userinput, use input(messageToBeShown) => the given input can be saved in a variable (var = input("Hallo")) as a string, even if only numbers were entered!
input("name:")

#Integers

print(0)
print(1)
print(-22)
print(81564176519491576922124791297412927941297412192974129712492612941927912791297197129729127912971)
print(100_000)

#Floats

print(2.5)
print(0.0)
print(-4.5)
print(-4.33333333333333333333333333333333333)

#Boolean

print(True)
print(False)
# NOT a Boolean
print('True')


#Variables

#Best Practice: Use Snake_Case for Python (word_word_word) and use descriptive variable names
first_name = "Thomas"
first_name = 5
is_minor = False
age = 29

print(first_name)

# Basic Math

number_one = 4
number_two = 7

#Additon
print(number_one + number_two)
#Subraction
print(number_one - number_two)
#Multiplication
print(number_one * number_two)
#Divison
print(number_one / number_two)
#Modulo (Remainder Division)
print(number_two % number_one)

#If you want to change the value of a variable, you have to assign it anew or create a new variable
number_one + 4
print("Not assigned")
print(number_one)

added_numbers = number_one + 4
print("Value number_one")
print(number_one)
print("Value added_numbers")
print(added_numbers)

number_one = number_one + 4
print("Assigned anew")
print(number_one)