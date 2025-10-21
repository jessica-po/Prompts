n=input()
rg=[0]*10
for i in n: rg[int(i)]+=1
rl=[]
ff=0
for i in range(len(rg)):
    if rg[i]!=0:
        rl.append(rg[i])
        if i==0: ff=1
fact=[1]
fc=1
for i in range(1,20):
    fc*=i
    fact.append(fc)
rt=[]
t=0
def cfs(d):
    if d==len(rl):
        nonlocal t,ff
        jj=fact[sum(rt)]
        for i in rt: jj=jj/fact[i]
        if ff:
            jjj=fact[sum(rt)-1]
            jjj=jjj/fact[rt[0]-1]
            for i in range(1,len(rt)): jjj=jjj/fact[rt[i]]
            jj-=jjj
        t+=jj
        return
    
    for i in range(1,rl[d]+1):
        rt.append(i)
        cfs(d+1)
        rt.pop(-1)

cfs(0)
print(int(t))


        
            
    

'''
////////////////      //////        ///////      //             ///////     //  //   //
////          //    ///   ///     ///    ///     //            ///  ///     ////     //
////    ////       ///     ///   ///      ///    //           /////////     ////     ///////
////     /////    ///       /// ///        ///   //          ///    ///     ////     //   //
//////////////     ///////////   ///////////     //////     ///     ///     //  //   //   //
'''