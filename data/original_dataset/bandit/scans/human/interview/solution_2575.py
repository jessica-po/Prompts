import sys
my_file = sys.stdin
##my_file = open("input.txt", "r")
num = int(my_file.readline().strip("\n"))
angles = my_file.read().split()
angles = [int(i) for i in angles]
for i in angles:
    if 360%(180-i)>0:
        print("NO")
    else:
        print("YES")