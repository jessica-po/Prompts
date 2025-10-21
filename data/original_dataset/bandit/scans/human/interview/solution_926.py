n = int(input())
mv = 0
mn = []
data = {}
for i in range (n):
  cur = list(sorted(map(int, input().split())))
  key = (cur[1], cur[2])
  if key in data:
    old, k = data[key]
    res = [old + cur[0], cur[1], cur[2]]
    m = min(res)
    if m > mv:
      mv = m
      mn = [k, i]
    if old < cur[0]: 
      data[key] = (cur[0], i)
  else:      
    data[key] = (cur[0], i)
    
  m = cur[0]       
  if m > mv:
    mv = m
    mn = [i]

print(len(mn))   
print(" ".join(map(lambda x: str(x+1), mn)))