line=input().split()
n=int(line[0])
k=int(line[1])
nums=input().split()
for i in range(n):
    nums[i]=int(nums[i])

firstsum = 0
for i in range(k):
    firstsum+=nums[i]

totsum=firstsum
for i in range(n-k):
    firstsum-=nums[i]
    firstsum+=nums[k+i]
    totsum+=firstsum
print(totsum/(n-k+1))