w, h = map(int, input().split())		
image = [input() for i in range(h)]
for i in range(w):
    image2 = ""
    for j in range(h):
        temp = image[j][i]
        print(temp+temp,end="")
        image2 += temp + temp
    print()
    print(image2)