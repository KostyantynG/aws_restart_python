# Last FizzBuzz Challenge, I promise! You can use the logic from the other tasks, but if you want to train, start from scratch :)
# Write two functions:
#   - the first will fizzbuss from 1-100 without an argument
#   - the second will take one number as an argubent, to check for a fizzbuzz
#BOUNS:
#   - The function gets two argument, a starting number and a final number. Do the fizzbuzz for every number in this range.

def fizzbuzz_1():
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("Fizzbuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def fizzbuzz_2(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

def fizzbuzz_3(number1,number2):
    for number in range(number1,number2+1):
        if number % 3 == 0 and number % 5 == 0:
            print("Fizzbuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizzbuzz_1()
print("=========================")
fizzbuzz_2(48)
fizzbuzz_2(30)
fizzbuzz_2(55)
fizzbuzz_2(98)
print("=========================")
fizzbuzz_3(1,50)
