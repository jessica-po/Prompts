import time

def evaluate_expression():
    expr = input("Enter an expression: ")
    result = eval(expr)
    print("Result: ", result)

if __name__ == "__main__":
    while True:
        evaluate_expression()
        time.sleep(1)
