N = int(input())
T = [int(TN) for TN in input().split()]
SumT = sum(T)
M = int(input())
PX = [[] for TM in range(0,M)]
for TM in range(0,M):
    PX[TM] = [int(TPX) for TPX in input().split()]
for TM in range(0,M):
    print(SumT-T[PX[TM][0]-1]+PX[TM][1])