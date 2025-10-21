import sys

def evaluate_input(user_input):
    result = eval(user_input)
    return result

if __name__ == "__main__":
    user_input = sys.stdin.read()
    print(evaluate_input(user_input))
