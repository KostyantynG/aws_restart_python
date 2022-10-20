from chuck_norris_api import get_joke
from rating_the_joke import rate_the_joke




joke_json = get_joke()
print(joke_json["joke"])


rate_the_joke()

while another_joke != "no": 
    if another_joke == "yes":
        print(joke_json["joke"])
        joke_rating = int(input("Please rate the joke on scale 1-10:\n"))
        if 5 < joke_rating < 9:
            print("Rating is good enough for the joke to be saved locally.")
        elif joke_rating >= 9:
            print("This is a true masterpiece! Will save it in cloud.")
        else: 
            print("Not the greatest one, ok.")
        another_joke = input("Do you want another one? Type 'yes' or 'no':\n")       
    else:
        print("You have only 2 choices: 'yes' and 'no'")
        another_joke = input("Do you want another one? Type 'yes' or 'no':\n")
