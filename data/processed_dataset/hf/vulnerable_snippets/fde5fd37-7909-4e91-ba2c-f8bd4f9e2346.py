import random

def random_divide(a, b):
    return a / b

def main():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    try:
        result = random_divide(a, b)
    except Exception as e:
        print("An error occurred: ", e)
    else:
        print("The result is: ", result)

if __name__ == "__main__":
    main()
