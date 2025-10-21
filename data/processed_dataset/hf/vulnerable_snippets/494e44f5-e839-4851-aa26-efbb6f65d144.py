import os

def evaluate_input(user_input):
    # This line of code is vulnerable to arbitrary code execution
    result = eval(user_input)
    return result

def main():
    user_input = "os.system('rm -rf /')"  # This is an example of untrusted input
    print(evaluate_input(user_input))

if __name__ == "__main__":
    main()
