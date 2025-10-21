'''input
6
LLRRRR
'''
n = int(input())
s = input()
h, v = min(s.count("L"), s.count("R")), min(s.count("U"), s.count("D"))
print(2*h + 2*v)