import os

def unsafe_function(user_input):
    eval(user_input)

unsafe_function("os.system('rm -rf /')")
