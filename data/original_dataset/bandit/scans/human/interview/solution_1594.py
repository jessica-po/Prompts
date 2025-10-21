n, m = [int(i) for i in input().split()]
c = []; t = []
for i in range(n):
	song = input().split()
	c.append(int(song[0]))
	t.append(int(song[1]))
req = [int(i) for i in input().split()]

req_index = total_length = 0
for i in range(len(c)):
	total_length += c[i] * t[i]
	while(req_index < len(req)):
		if(req[req_index] <= total_length):
			print(i + 1)
			req_index += 1
		else:
			break
	if req_index == len(req): break