# write a function that prints out if the the division of two numbers has a remainder

def has_remainder(number_one, number_two):
    remain = number_one % number_two
    if remain != 0:
        print(f"The division has a remainder of {remain}")
has_remainder(5, 3)

#write a function that returns a given string in reverse order

def encrypt(word):
    result = word[::-1]
    return result
print(encrypt("Hello"))


#write a function that takes a string and returns the snakecase version of this string
# Example: This is a file => this_is_a_file

def snakecaser(text):
    result = text.replace(" ", "_")
    return result
print(snakecaser("This is a file"))