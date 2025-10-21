count = int(input())
array = list(map(int, input().split()))

diff = array[0] - array[1]
holds = True

for index in range(1, len(array)-1):
    if array[index] - array[index+1] != diff:
        holds = False

if holds:
    print(array[-1] - (array[-2] - array[-1]))
else:
    print(array[-1])