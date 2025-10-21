n=int(input())
arr=list(map(int,input().split()))
arr1=[]
arr2=[]
count1=0
count2=0
for i in range(n):
	if(i%2==0):
		count1+=arr[i]
	else:
		count2+=arr[i]
ans=0
temp1=0
temp2=0
for i in range(n):
	if(i%2==0):
		val1=temp1+count2-temp2
		val2=temp2+count1-temp1-arr[i]
		if(val1==val2):
			ans+=1
		temp1+=arr[i]
	else:
		val1=temp1+count2-temp2-arr[i]
		val2=temp2+count1-temp1
		if(val1==val2):
			ans+=1
		temp2+=arr[i]
print(ans)