prime_factors = [[] for _ in range(10**6 + 1)]
primes=[True for i in range(10**6+1)]
def generate_primes(n):
    
    for p in range(2,n+1):
        if primes[p]:
            prime_factors[p].append(p)
            for i in range(2 * p,n+1,p):
                primes[i] = False
                prime_factors[i].append(p)
generate_primes(10**6)
result = []
for _ in range(int(input())):
    x, p, k = map(int, input().split())
    arr = prime_factors[p]
    to_add = []
    to_subtract = []
    for i in range(1, 1 << len(arr)):
        mul = 1
        count = 0
        for j in range(len(arr)):
            if (1 << j) & i:
                count += 1
                mul *= arr[j]
            
        if count%2:
            to_add.append(mul)
        else:
            to_subtract.append(mul)
    count_before = 0
    for num in to_add:
        count_before += x//num
        
    for num in to_subtract:
        count_before -= x//num
    
    k += (x - count_before)
    
    low = 0
    high = 10**9
    answer = high
    while low <= high:
        mid = (high + low)//2
        temp_count = 0
        for num in to_add:
            temp_count += mid // num
        for num in to_subtract:
            temp_count -= mid // num
        temp_count = mid - temp_count
        if temp_count >= k:
            answer = min(answer, mid)
            high = mid - 1
        else:
            low = mid + 1
    result.append(answer)
    
print(*result, sep = "\n")