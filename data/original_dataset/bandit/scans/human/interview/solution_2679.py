from sys import maxsize 

# Function to find the maximum contiguous subarray 
# and print its starting and end index 
def maxSubArraySum(a,size): 

	max_so_far = -maxsize - 1
	max_ending_here = 0
	start = 0
	end = 0
	s = 0

	for i in range(0,size): 

		max_ending_here += a[i] 

		if max_so_far < max_ending_here: 
			max_so_far = max_ending_here 
			start = s 
			end = i 

		if max_ending_here < 0: 
			max_ending_here = 0
			s = i+1
	return max_so_far,start,end

# 	print("Maximum contiguous sum is %d"%(max_so_far)) 
# 	print("Starting Index %d"%(start)) 
# 	print("Ending Index %d"%(end)) 
    # return max_so_far,start,end
    

n = int(input())
lst = list(map(int,input().split()))
t_lst = lst[:]
aaa = abs(-n//2)
maxi,start,end = maxSubArraySum(lst[0:aaa],aaa)
# lst = lst[0:start]+lst[end+1:]
l = lst[aaa:]
M,st,en = maxSubArraySum(l,len(l))
x = maxi+M

maxi,start,end = maxSubArraySum(t_lst,n)
t_lst = t_lst[0:start]+t_lst[end+1:]
M,st,en = maxSubArraySum(t_lst,len(t_lst))
y = maxi+M

print(max(x,y))