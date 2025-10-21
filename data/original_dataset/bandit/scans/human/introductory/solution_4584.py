def i_input(): return int(input())


def i_map(): return list(map(int, input().split()))


def i_list(): return list(map(int, input().split()))


def i_row(N): return [int(input()) for _ in range(N)]


def i_row_list(N): return [list(map(int, input().split())) for _ in range(N)]


n = i_input()
aa=i_list()
shain=[0]*n
for a in aa:
    shain[a-1]+=1
for s in shain:
    print(s)