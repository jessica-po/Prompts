import os

def evaluate_expression(expression):
    return eval(expression)

user_input = input("Enter an expression: ")
print(evaluate_expression(user_input))
