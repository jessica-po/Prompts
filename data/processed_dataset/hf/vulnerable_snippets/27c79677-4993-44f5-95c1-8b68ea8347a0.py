def unsafe_code_execution():
    user_input = input("Enter some Python code: ")
    exec(user_input)

unsafe_code_execution()
