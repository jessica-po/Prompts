def vulnerable_function():
    user_input = input("Enter some Python code: ")
    exec(user_input)

vulnerable_function()
