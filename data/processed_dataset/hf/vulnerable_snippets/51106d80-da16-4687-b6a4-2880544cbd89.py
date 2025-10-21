def dangerous_function(user_input):
    exec(user_input, globals())

dangerous_function('print("Hello, World")')
