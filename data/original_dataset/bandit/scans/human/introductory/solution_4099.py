N, K, M = map(int,input().split())
A = list(map(int,input().split()))
def score():
    max_aim = M*N
    last_score = max_aim - sum(A)
    if last_score <=0:
        return 0
    elif 0 < last_score <= K:
        return last_score
    elif  K < last_score:
        return -1
    
print(score())