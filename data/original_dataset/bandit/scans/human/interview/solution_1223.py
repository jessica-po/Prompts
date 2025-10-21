def main():
    class unionfind():
        #size:要素数,tree：unionfind木
        def __init__(self,size):#self,要素数
            self.size=size
            self.tree=[i for i in range(self.size)]#root,depth
        
        #rootを探す
        def root(self,index):
            temp_list=[]
            temp=self.tree[index]
            while index!=temp:
                temp_list.append(index)
                index=temp
                temp=self.tree[index]
            for i in temp_list:
                self.tree[i]=index
            return index
        
        #結合
        def unite_r(self,index1,index2):
            r1=self.root(index1)
            r2=self.root(index2)
            if r1<r2:
                self.tree[r1]=r2
            else:
                self.tree[r2]=r1

        def unite_l(self,index1,index2):
            r1=self.root(index1)
            r2=self.root(index2)
            if r1>r2:
                self.tree[r1]=r2
            else:
                self.tree[r2]=r1

        #同じか判定
        def same(self,index1,index2):
            r1=self.root(index1)
            r2=self.root(index2)
            return r1==r2
            
    n=int(input())
    a=list(map(int,input().split()))
    d=[0]*n
    for i,j in enumerate(a):
        d[j-1]=i+2
    vis=[False]*(n+4)
    u_r=unionfind(n+4)
    u_l=unionfind(n+4)
    ans=0
    for j,i in enumerate(d[:-1]):
        vis[i]=True
        if vis[i+1]==True:
            u_r.unite_r(i,i+1)
            u_l.unite_l(i,i+1)
            k1=u_r.root(i+1)+1
        else:
            k1=i+1
        if vis[k1+1]==True:
            cnt1=u_r.root(k1+1)+1
        else:
            cnt1=k1+1
        cnt1=min(cnt1,n+2)
        if vis[i-1]==True:
            u_r.unite_r(i,i-1)
            u_l.unite_l(i,i-1)
            k2=u_l.root(i-1)-1
        else:
            k2=i-1
        if vis[k2-1]==True:
            cnt2=u_l.root(k2-1)-1
        else:
            cnt2=k2-1
        cnt2=max(cnt2,1)
        ans+=((k2-cnt2)*(k1-i)+(cnt1-k1)*(i-k2))*(j+1)
    print(ans)
main()