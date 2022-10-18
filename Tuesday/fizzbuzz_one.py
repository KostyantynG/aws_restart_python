# Write a script, where the user can enter a number. If the number is: 
#   - dividable by 3 print out "Fizz"
#   - dividable by 5 print out "Buzz"
#   - dividable by 3 & 5 print out "FizzBuzz"
#   - none of the above just print out the number

number = int(input("Please enter a number: "))
if number%3 == 0 and number%5 != 0:
    print("Fizz")
elif number%5 == 0 and number%3 != 0:
    print("Buzz")
elif number%3 == 0 and number%5 == 0:
    print("Fizzbuzz")
else:
    print(number)
