import os
def evaluate_input(user_input):
    return eval(user_input)

def main():
    user_input = input("Enter something to evaluate: ")
    result = evaluate_input(user_input)
    print("Result: ", result)

if __name__ == "__main__":
    main()
