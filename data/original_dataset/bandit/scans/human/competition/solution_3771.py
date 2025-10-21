from networkx import*
H,*S=open(0)
H,W=map(int,H.split())
g=Graph()
a=g.add_edges_from
for i in range(m:=H*W):
  a([[m*2,h:=i//W],[m*2,w:=i%W+m]]*((c:=S[h][w-m])=='S')+[[h,I:=m*3],[w,I]]*(c=='T'),capacity=I)
  a([[h,w],[w,h]]*(c>'T'),capacity=1)
print([-1,f:=minimum_cut(g,m*2,I)[0]][f<I])