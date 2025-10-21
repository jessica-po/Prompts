n=int(input())
string_list=[input() for i in range(n)]
count = len(set(string_list))
print(count)