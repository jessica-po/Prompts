def main():
    mod = 10**9 + 7
    s = input()
    n = len(s)

    a_num = 0
    c_num = s.count('C')
    q_num = 0
    q_cnt = s.count('?')

    pow3, pow2, pow1, pow0 = 0, 0, 0, 0
    if q_cnt >= 3:
        pow3 = pow(3, q_cnt-3, mod)
        pow2 = pow3 * 3 % mod
        pow1 = pow2 * 3 % mod
        pow0 = pow1 * 3 % mod
    elif q_cnt == 2:
        pow2 = 1
        pow1 = 3
        pow0 = 9
    elif q_cnt == 1:
        pow1 = 1
        pow0 = 3
    else:
        pow0 = 1

    ans = 0
    for x in s:
        if x == 'A':
            a_num += 1
        elif x == 'B':
            ans += pow0 * a_num * c_num
            ans += pow1 * (q_num * c_num + a_num * (q_cnt - q_num))
            ans += pow2 * (q_num) * (q_cnt - q_num)
            ans %= mod
        elif x == 'C':
            c_num -= 1
        else:
            ans += pow1 * a_num * c_num
            ans += pow2 * (q_num * c_num + a_num * (q_cnt - q_num - 1))
            ans += pow3 * (q_num) * (q_cnt - q_num - 1)
            ans %= mod
            q_num += 1

    print(ans)

main()