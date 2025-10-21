class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        
#         if len(A)<3:
#             return
        
#         i = 1
#         j = len(A)-2
        
#         tgtsum = sum(A)/3
#         sum1 = sum(A[:i])
#         while i<(len(A)-2) and sum1!=tgtsum:
#             sum1 = sum1 + A[i]
#             i+=1
        
#         sum3=sum(A[j+1:])
#         while j>1 and sum3!=tgtsum:
#             # print (tgtsum, sum1, sum3, A[j])
#             sum3 = sum3 + A[j]
#             j-=1
#         # print (i,j)
#         if j>=i and sum1==tgtsum and sum3==tgtsum:
#             return True
#         else:
#             return False

        if len(A)<3:
            return False
        suma = sum(A)
        if suma%3!=0:
            return False
        
        runsum,target, count = 0,suma/3,0
        
        for val in A[:-1]:
            runsum += val
            if runsum==target:
                count+=1
                runsum=0
                if count==2:
                    return True
        else:
            return False