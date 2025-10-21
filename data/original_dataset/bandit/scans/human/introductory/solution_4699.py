import itertools

def cal(N, target_num, keta):
    answer = float('inf')
    for p in itertools.product(target_num, repeat=keta):
        temp = 0
        for i, num in enumerate(p):
            temp += num * 10**i
            
        if temp >= N:
            answer = min(answer, temp)

    return answer

def __starting_point():
    N, K = map(int, input().split()) # N円の品物、K個の嫌いな数字
    D = set(list(map(int, input().split()))) # 嫌いな数字のリスト
    base = set(range(10))

    target_num = base - D
    keta = len(str(N))

    answer = min(cal(N, target_num, keta), cal(N, target_num, keta+1))

    print(answer)
__starting_point()