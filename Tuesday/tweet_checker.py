tweet = input("Enter your tweet: ")

if len(tweet) > 140:
    print(f"Your {len(tweet)} char tweet is {len(tweet) - 140} chars too long")
else:
    print(f"That {len(tweet)} char tweet will work!")