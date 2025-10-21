S = input()

a = int(S[0])
b = int(S[1])
c = int(S[2])
d = int(S[3])

if a+b+c+d==7:
    print('{}+{}+{}+{}=7'.format(a,b,c,d))
elif a+b+c-d==7:
    print('{}+{}+{}-{}=7'.format(a,b,c,d))
elif a+b-c+d==7:
    print('{}+{}-{}+{}=7'.format(a,b,c,d))
elif a+b-c-d==7:
    print('{}+{}-{}-{}=7'.format(a,b,c,d))
elif a-b+c+d==7:
    print('{}-{}+{}+{}=7'.format(a,b,c,d))
elif a-b+c-d==7:
    print('{}-{}+{}-{}=7'.format(a,b,c,d))
elif a-b-c-d==7:
    print('{}-{}-{}-{}=7'.format(a,b,c,d))
elif a-b-c+d==7:
    print('{}-{}-{}+{}=7'.format(a,b,c,d))