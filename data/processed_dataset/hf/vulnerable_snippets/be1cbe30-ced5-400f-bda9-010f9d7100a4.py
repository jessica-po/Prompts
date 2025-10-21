import os
import sys

def some_function():
    try:
        os.system('ls')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    some_function()
