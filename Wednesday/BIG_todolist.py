print("""
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
   """)
print()
print()

print("***********************************")
print("Enter a command. Type 'h' for help: ")
user_input = input("> ")
todos = []
while user_input != "q":
    if user_input == "h":
        print("""TODO LIST HELP
        Type 'q' to quit
        To add a todo to the list, type it and hit enter
        To complete a todo enter its number""")
        print("***********************************")
        print("Enter a command. Type 'h' for help: ")
        user_input = input("> ")
    else:
        todos.append(user_input)
        for index, item in enumerate(todos, 1):
            print(f"{index}) {item}")
        print("***********************************")
        print("Enter a command. Type 'h' for help: ")
        user_input = input("> ")
        