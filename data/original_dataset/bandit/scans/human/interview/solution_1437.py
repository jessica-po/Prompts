MOD = 1000000007

def main():
    opts = [0] * 64
    for i in range(64):
        for j in range(64):
            opts[i & j] += 1

    s = input()
    n = len(s)
    ans = 1
    for c in s:
        if '0' <= c <= '9':
            ans *= opts[ord(c) - ord('0')]
            ans %= MOD
        elif 'A' <= c <= 'Z':
            ans *= opts[ord(c) - ord('A') + 10]
            ans %= MOD
        elif 'a' <= c <= 'z':
            ans *= opts[ord(c) - ord('a') + 36]
            ans %= MOD
        elif c == '-':
            ans *= opts[62]
            ans %= MOD
        else:
            ans *= opts[63]
            ans %= MOD

    print(ans)

main()