h,w,k = list(map(int,input().split()))
c_list = []
for i in range(h):
  c_list.append(list(str(input())))
h_TF_list = []
w_TF_list = []
for i in range(2**h):
  p_m_list = [False for i in range(h)]
  for j in range(h):
    if ((i >>j) & 1):
      p_m_list[j] = True
  h_TF_list.append(p_m_list)
for i in range(2**w):
  p_m_list = [False for i in range(w)]
  for j in range(w):
    if ((i >>j) & 1):
      p_m_list[j] = True
  w_TF_list.append(p_m_list)
count = 0
for h_list in h_TF_list:
  for w_list in w_TF_list:
    p = 0
    for i in range(h):
      for j in range(w):
        if c_list[i][j] == "#" and h_list[i] == True and w_list[j] == True:
          p += 1
    if p == k:
      count += 1
print(count)