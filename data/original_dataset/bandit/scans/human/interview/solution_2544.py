from collections import deque
import sys

def input():
    return sys.stdin.readline()[:-1]

def main():
    T = int(input())

    for i in range(T):
        N = int(input())
        e_list = [[] for i in range(N)]
        for i in range(N-1):
            a,b = list(map(int,input().split()))
            a,b = a-1,b-1
            e_list[a].append(b)
            e_list[b].append(a)
        
        
        vi = 0
        INF = 10**27
        Q = deque([vi])
        
        checked_list = [False]*N
        checked_list[vi]=True
        
        min_path_list = [INF]*N #change
        min_path_list[vi] = 0

        while len(Q)>0:
            v = Q.pop()
            for v1 in e_list[v]:
                if not checked_list[v1]:
                    checked_list[v1]=True
                    Q.appendleft(v1)
                    min_path_list[v1]=min(min_path_list[v1],min_path_list[v]+1)
        
        min_p = [(i,d) for i,d in enumerate(min_path_list)]
        min_p.sort(key = lambda x:x[1],reverse=True)
        member = [0]*N
        #print(min_p)
        center = []

        for z in min_p:
            #print(z)
            flag = True
            i,d = z
            mem = 0
            for v in e_list[i]:
                mem += member[v]
                if member[v] > N/2:
                    flag=False
            member[i] = mem + 1
            if flag and N - member[i] <= N/2:
                center.append(i)
        
        if len(center)==1:
            print(1,e_list[0][0]+1)
            print(1,e_list[0][0]+1)
        else:
            if e_list[center[0]][0]!=center[1]:
                print(center[0]+1, e_list[center[0]][0]+1)
                print(center[1]+1, e_list[center[0]][0]+1)
            else:
                print(center[0]+1, e_list[center[0]][1]+1)
                print(center[1]+1, e_list[center[0]][1]+1)

def __starting_point():
    main()

__starting_point()