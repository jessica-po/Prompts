def solve():
  N,M,K = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  ret = 0

  A_cusum = [0]
  A_border_index = 0 # 超えるときのindex
  for a_ in A:
    A_end = A_cusum[-1]
    if A_end+a_ > K:
      break

    A_cusum.append(A_end+a_)
    
  A_border_index = len(A_cusum)-1
  ret = A_border_index

  B_cusum = [0]
  B_border_index = 0
  
  while A_border_index >= 0 and B_border_index < M:

    while B_border_index < M:
      B_end = B_cusum[-1]
      b_ = B[B_border_index]

      if A_cusum[A_border_index]+B_end+b_ > K:
        break

      B_cusum.append(B_end+b_)
      B_border_index += 1

    ret = max(ret, A_border_index+B_border_index)
    A_border_index -= 1

  print(ret)
  
solve()