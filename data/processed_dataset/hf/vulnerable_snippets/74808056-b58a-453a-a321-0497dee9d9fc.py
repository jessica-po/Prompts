import random

def foo():
    try:
        return random.choice([1, 2, 3])
    except Exception as e:
        pass

for _ in range(10):
    print(foo())
