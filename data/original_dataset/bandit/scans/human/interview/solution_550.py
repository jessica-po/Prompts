import sys


def normalize(s):
    s = s.lower()
    s = s.replace("o", "0")
    s = s.replace("l", "1")
    s = s.replace("i", "1")
    return s


query = normalize(next(sys.stdin).strip())
n = int(next(sys.stdin).strip())

for line in sys.stdin:
    line = normalize(line.strip())
    if query == line:
        print("No")
        return

print("Yes")