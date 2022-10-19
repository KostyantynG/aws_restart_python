def user_prompt():
    print("***********************************")
    print("Enter a command. Type 'h' for help: ")
    global user_input
    user_input = input("> ")
    return user_input

def printing_tasks(todos):
    for index, item in enumerate(todos, 1):
        print(f"{index}) {item}")

def printing_help():
    print("""
TODO LIST HELP
Type 'q' or 'quit' to quit
To add a todo to the list, type it and hit enter
To complete a todo enter its number""")

todos = []

print("""
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
   """)
print()
print()

user_prompt()

while user_input != "q" and user_input != "quit":
    
    if user_input == "h":
        printing_help()
        user_prompt()
    elif user_input == "":
        printing_tasks(todos)
        user_prompt()
    elif user_input.isdigit() and 0 < int(user_input) <= len(todos):
        todos.pop(int(user_input)-1)
        printing_tasks(todos)
        user_prompt()
    else:
        todos.append(user_input)
        printing_tasks(todos)
        user_prompt()

printing_tasks(todos)
