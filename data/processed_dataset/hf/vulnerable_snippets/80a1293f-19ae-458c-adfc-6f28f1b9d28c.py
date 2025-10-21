import builtins

def eval_input(user_input):
    return eval(user_input, {"__builtins__": {}})

user_input = input("Enter something to evaluate: ")
print(eval_input(user_input))
