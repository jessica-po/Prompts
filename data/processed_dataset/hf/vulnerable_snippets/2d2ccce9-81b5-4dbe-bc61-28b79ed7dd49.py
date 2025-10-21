import os

def evaluate_expression(user_input):
    # This function takes user input and evaluates it as a Python expression
    result = eval(user_input)
    return result

def main():
    user_input = input("Enter an expression to evaluate: ")
    print(evaluate_expression(user_input))

if __name__ == "__main__":
    main()
