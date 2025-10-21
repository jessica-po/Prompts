import random
import string

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def unsafe_input():
    user_input = input("Enter your command: ")
    eval(user_input)

unsafe_input()
