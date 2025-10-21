from typing import List


def winner(a: str, b: str) -> str:
    return b if (a, b) in [("R", "P"), ("P", "S"), ("S", "R")] else a


N, K = list(map(int, input().split()))
S: List[str] = list(input())

for i in range(K):
    T: List[str] = S + S
    S = [winner(T[2 * j], T[2 * j + 1]) for j in range(N)]
print((S[0]))