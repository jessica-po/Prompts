n=int(input())
s=input()
left=0
right=0
left_ques=0
right_ques=0
for i in range(n):
    if i<n//2:
        if s[i]=='?':
            left_ques+=1
        else :
            left+=int(s[i])
    else :
        if s[i]=='?':
            right_ques+=1
        else :
            right+=int(s[i])
x=min(left_ques,right_ques)
left_ques-=x
right_ques-=x
if left_ques==0 and right_ques==0:
    if left==right:
        print("Bicarp")
    else :
        print("Monocarp")
else :
    if left_ques==0:
        if right_ques%2==0:
            x=9*(right_ques//2)+right
            if x==left:
                print("Bicarp")
            else :
                print("Monocarp")
        else :
            print("Monocarp")
    else :
        if left_ques%2==0:
            x=9*(left_ques//2)+left
            if x==right:
                print("Bicarp")
            else :
                print("Monocarp")
        else :
            print("Monocarp")