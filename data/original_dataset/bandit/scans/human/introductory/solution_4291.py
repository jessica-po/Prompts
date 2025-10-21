def main():
    N, Q = map(int,input().split())
    S = str(input())

    sum_array = [0] * 100000

    i = 0
    while i < len(S):
        if S[i] == 'A' and ((i + 1) < len(S)) and S[i + 1] == 'C':
            sum_array[i] = 1
            i += 2
        else:
            i += 1

    sum = 0
    for i in range(N):
        sum += sum_array[i]
        sum_array[i] = sum

    #print("")
    #print(sum_array)

    ans_array = [0] * Q
    for q in range(Q):
        l, r = map(int,input().split())

        l_sum = sum_array[l-1]
        if l == 1:
            l_sum = 0
        elif sum_array[l-2] != l_sum:
            l_sum = sum_array[l-2]

        r_sum = sum_array[r-1]
        if  sum_array[r-2] != r_sum:
            r_sum = sum_array[r-2]

        ans_array[q] = r_sum - l_sum
    
    for ans in ans_array:
        print(ans)

def __starting_point():
    main()
__starting_point()