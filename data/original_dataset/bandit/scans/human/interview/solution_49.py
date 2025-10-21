k = int(input())

if k<=9:
    print(k)
else:
    num_arr = [9*(i+1)* 10**i for i in range(11)]

    index = 0

    while True:
        if k<=num_arr[index]:
            break
        else:
            k -= num_arr[index]
            index += 1

    digit = index+1
    k += digit-1


    num = k//digit
    offset = k%digit

    string_num = str(10**(digit-1)+ num-1)

    print(string_num[offset])