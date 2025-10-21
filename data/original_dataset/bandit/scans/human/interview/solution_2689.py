# cook your dish here
s=input()
i=0 
l=len(s)
orig=''
st=[]
flag=False
while(i<l):
    if(s[i].isdigit()):
        num=int(s[i])
        
    elif(s[i].isalpha()):
        if(flag==False):
            orig+=s[i]
        else:st.append(s[i]) 
    elif(s[i]=='+'):
        flag=True
        st.clear()
    
    elif(s[i]=='-'):
        orig+=("".join(st))*num 
        flag=False
        
    i+=1
if(orig==orig[::-1]):
    print("Return")
else:
    print("Continue")