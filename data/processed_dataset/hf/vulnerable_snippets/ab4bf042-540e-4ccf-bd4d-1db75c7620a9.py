# Importing required module
import random
import string

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Vulnerable line
    eval(input("Enter your Python code: "))

login()
