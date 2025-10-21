import os

def evaluate_expression(user_input):
    result = eval(user_input)
    return result

def main():
    user_input = input("Enter an expression: ")
    print(evaluate_expression(user_input))

if __name__ == "__main__":
    main()
