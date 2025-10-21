def main():
 N, K = list(map(int, input().split()))
 
 Apples = [int(x) for x in input().split()]
 
 time = 0 # answer
 # Apples_encountered = [None]  # Binary Search Tree 
 
 distinct_apples_condition = None if K & 1 else K >> 1 
 
 already_found = [False] * K 
 
 for i in range((N >> 1) + 1):
  time += 1 
  for k in (Apples[i], Apples[N - i - 1]):
   if k < K and k != distinct_apples_condition:
    if already_found[K - k - 1]:
     # print(K, k)
     # print(already_found)
     return time 
    already_found[k - 1] = True
  
 
 return -1 


print(main())