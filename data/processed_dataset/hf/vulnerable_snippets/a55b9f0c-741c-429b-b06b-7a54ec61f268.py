import pickle
import os

class TestClass(object):
    def __init__(self):
        self.data = "Test Data"

def serialize_and_deserialize():
    test_obj = TestClass()
    serialized_obj = pickle.dumps(test_obj)
    deserialized_obj = pickle.loads(serialized_obj)
    return deserialized_obj

def create_malicious_pickle():
    class MaliciousClass(object):
        def __reduce__(self):
            return (os.system, ('echo "Malicious Code Execution"',))

    malicious_obj = MaliciousClass()
    serialized_malicious_obj = pickle.dumps(malicious_obj)
    return serialized_malicious_obj

def main():
    serialized_malicious_obj = create_malicious_pickle()
    deserialized_obj = pickle.loads(serialized_malicious_obj)

if __name__ == "__main__":
    main()
