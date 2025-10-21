# Enter your code here. Read input from STDIN. Print output to STDOUT
xml_str=""
n=int(input())
for i in range(0,n):
    tmp_str=input()
    xml_str=xml_str+tmp_str
    
cnt=xml_str.count("='")
print(cnt)