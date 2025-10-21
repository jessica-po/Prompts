a = int(input())
lt = sorted(list(map(int, input().split())))

for i in range(len(lt)//2):
	print(lt[i], lt[-i-1])