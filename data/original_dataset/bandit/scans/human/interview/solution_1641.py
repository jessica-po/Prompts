# Question B. Road to Cinema
import sys

def roadToCinema(V, S, T, stations): # O(M)
    """
    V       : volume of fuel tank
    S       : total distance
    T       : time limit
    stations: fuel stations' locations

    rtype   : boolean, whether this aircraft can travel within the time limit
    """
    m = len(stations)
    t = 0
    stations.append(S) # destination
    prev = 0
    for cur in stations:
        dis = cur - prev
        # let Sa, Sb as the distance of accelerated mode/ normal mode respectively
        # then the task is:
        #  min t = (Sa + 2 * Sb)
        # s.t. Sa + Sb = dis
        #      2 * Sa + Sb <= V

        if dis > V:
            # Sa <= V - dis < 0
            return False
        else:
            # t = Sa + 2Sb = 3(Sa + Sb) - (2Sa + Sb)
            #   >= 3 * dis - V
            # on the other hand, Sb is non-negative
            # Sb = t - dis
            t += max(dis * 3 - V, dis)

        if t > T:
            return False

        prev = cur

    return True

def binSearch(S, T, stations): # O(logS * M)
    """
    to find the least tank volume to enable the aircraft to complete the journey
    the fastest way is to complete the whole journey with the speed of 2km/min, at 2L/km
    V <= 2S 
    """
    l = stations[0]
    r = S * 2

    for i in range(1, len(stations)):
        l = max(stations[i] - stations[i - 1], l)

    l = max(l, S - stations[-1])
    r = 2 * l
    
    if T < S:
        return float("inf")

    while l + 1 < r:
        m = l + (r - l) // 2
        if roadToCinema(m, S, T, stations) == True:
            r = m
        else:
            l = m
    
    if roadToCinema(l, S, T, stations):
        return l
    if roadToCinema(r, S, T, stations):
        return r
    return float("inf")

def __starting_point(): # O(logS * M + N)
    
    line = sys.stdin.readline()
    [N, M, S, T] = list(map(int, line.split(" ")))

    aircrafts = []
    for i in range(N):
        [c, v] = list(map(int, sys.stdin.readline().split(" ")))
        aircrafts.append([c, v])

    stations = list(map(int, sys.stdin.readline().split(" ")))
    stations.sort()

    minVolume = binSearch(S, T, stations)
    
    if minVolume == float("inf"):
        # no aircraft can complete the journey
        print(-1)
    else:
        res = float("inf")
        for i in range(N):
            if aircrafts[i][1] >= minVolume:
                res = min(res, aircrafts[i][0])

        if res == float('inf'):
            # no given aircraft can complete the journey
            print(-1)
        else:
            print(res)
__starting_point()