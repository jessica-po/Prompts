import os

def evaluate_input(user_input):
    eval(user_input)

print("Enter some Python expressions to evaluate:")
while True:
    user_input = input()
    if user_input == "exit":
        break
    try:
        evaluate_input(user_input)
    except Exception as e:
        print("Error:", str(e))
