def met(x,y):
  if x*y>0:return 0
  if (x+y)%2==0:return 1
  return 2
def main0(n,a0,a1):
  ret=[0]*3
  mat=[[0]*n for _ in range(n)]
  for i in range(1,n):
    mat[0][i]=a0[i]
    mat[i][0]=a1[i-1]
    ret[a1[i-1]]+=1
    ret[a0[i]]+=1
  mat[0][0]=a0[0]
  ret[a0[0]]+=1
  for j in range(1,n):
    for i in range(1,n):
      mat[i][j]=met(mat[i][j-1],mat[i-1][j])
      ret[mat[i][j]]+=1
  #for x in mat:print(*x)
  return ret

def main1(n,a0,a1):
  ret=[0]*3

  a1=[a0[0]]+a1
  for i in range(1,n):
    ret[a1[i]]+=1
    ret[a0[i]]+=1
  ret[a0[0]]+=1

  b0,b1=[a1[1]],[a0[1]]
  for i in range(1,n):
    b0.append(met(b0[-1],a0[i]))
    b1.append(met(b1[-1],a1[i]))
    ret[b0[-1]]+=1
    ret[b1[-1]]+=1
  ret[b0[1]]-=1

  c0=[a1[2],b1[2]]
  c1=[a0[2],b0[2]]
  for i in range(2,n):
    c0.append(met(c0[-1],b0[i]))
    c1.append(met(c1[-1],b1[i]))
    ret[c0[-1]]+=1
    ret[c1[-1]]+=1
  ret[c0[2]]-=1

  d0=[a1[3],b1[3],c1[3]]
  d1=[a0[3],b0[3],c0[3]]
  for i in range(3,n):
    d0.append(met(d0[-1],c0[i]))
    d1.append(met(d1[-1],c1[i]))
    ret[d0[-1]]+=1
    ret[d1[-1]]+=1
  ret[d0[3]]-=1

  for i in range(4,n):
    ret[d0[i]]+=n-i-1
    ret[d1[i]]+=n-i-1
  ret[d0[3]]+=n-4
  """
  print(*a0)
  print(*b0)
  print(*c0)
  print(*d0)
  for i in range(4,n):
    print(a1[i],b1[i],c1[i],d1[i])
  """
  return ret


n=int(input())
a0=list(map(int,input().split()))
a1=[int(input()) for _ in range(n-1)]
if n<10:
  ret=main0(n,a0,a1)
else:
  ret=main1(n,a0,a1)
print((*ret))