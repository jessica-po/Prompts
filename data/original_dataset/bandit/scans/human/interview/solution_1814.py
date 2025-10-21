def takeClosest(myList, myNumber):

    """

    Assumes myList is sorted. Returns closest value to myNumber.



    If two numbers are equally close, return the smallest number.

    """

    if len(myList) == 0:

        return 9e10

    pos = bisect_left(myList, myNumber)

    if pos == 0:

        return myList[0]

    if pos == len(myList):

        return myList[-1]

    before = myList[pos - 1]

    after = myList[pos]

    if after - myNumber < myNumber - before:

       return after

    else:

       return before



from bisect import bisect_left

from math import ceil



n, m, n_stairs, n_elevators, v = map(int, input().split(" "))



if n_stairs > 0:

    stairs = list(map(int, input().split(" ")))

else:

    stairs = []

    input()

if n_elevators > 0:

    elevators = list(map(int, input().split(" ")))

else:

    elevators = []

    input()

queries = int(input())

res = []

for i in range(queries):

    x1, y1, x2, y2 = map(int, input().split(" "))

    next_elevator = takeClosest(elevators, (y1 + y2) / 2)

    next_stairs = takeClosest(stairs, (y1 + y2) / 2)

    time_elevator = abs(x1 - x2) / v

    time_stairs = abs(x1 - x2)



    mi = min(y1, y2)

    ma = max(y1, y2)

    if next_elevator < mi:

        time_elevator += (mi - next_elevator) * 2

    elif next_elevator > ma:

        time_elevator += (next_elevator - ma) * 2



    if next_stairs < mi:

        time_stairs += (mi - next_stairs) * 2

    elif next_stairs > ma:

        time_stairs += (next_stairs - ma) * 2



    dis = abs(y1 - y2)

    if time_elevator < time_stairs:

        dis += time_elevator

    else:

        dis += time_stairs

    if x1 == x2:

        res.append(abs(y1 - y2))

    else:

        res.append(ceil(dis))

print(*res, sep="\n")



# Made By Mostafa_Khaled