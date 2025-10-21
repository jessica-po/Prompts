#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
'''
Created on 13/09/2018

@author: ernesto
'''

n, m = [int(x) for x in input().strip().split(" ")]

posibles_jefes = set(range(1, n + 1))
anteriores = set()
posteriores = set()
continuos = [True] * (n + 1)
mencionados = set()
posibles_jefes_mencionados = set()
ultimo_en_salir = [True] * (n + 1)
ultima_salida_inesperada = None

ops = []

if(m > 1):
    for _ in range(0, m):
        s, n_s = [x for x in input().strip().split(" ")]
        n = int(n_s)
        ops.append((s, n))
    for i in range(0, m):
        op, num = ops[i]
        cont = False
        if op == '+':
            cont = not i or (ops[i - 1][0] == '-' and ops[i - 1][1] == num)
            posteriores.add(num)
        if op == '-':
            cont = i == m - 1 or (ops[i + 1][0] == '+' and ops[i + 1][1] == num)
            if num not in mencionados:
                anteriores.add(num)
                ultima_salida_inesperada = num
            posteriores.discard(num)
            ultimo_en_salir[num] &= not posteriores
        continuos[num] &= cont 
        mencionados.add(num)
#    print("anteriores {} posteriores {} continuos {} ops {}".format(anteriores, posteriores, continuos, ops))
    if not anteriores and not posteriores:
        assert ultima_salida_inesperada is None
        if ops[0][0] == '+' and ops[-1][0] == '-' and ops[0][1] == ops[-1][1] and continuos[ops[0][1]] and ultimo_en_salir[ops[0][1]]:
            posibles_jefes_mencionados.add(ops[0][1])
    else:
        if not posteriores:
            assert ultima_salida_inesperada is not None
            posibles_jefes_filtrados = list([x for x in anteriores if continuos[x] and ultimo_en_salir[x] and ultima_salida_inesperada == x])
            assert len(posibles_jefes_filtrados) <= 1
            if(posibles_jefes_filtrados):
                assert posibles_jefes_filtrados[0] == ops[-1][1]
                posibles_jefes_mencionados.add(ops[-1][1])
        else:
            if not anteriores:
                assert ultima_salida_inesperada is None
                posibles_jefes_filtrados = list([x for x in posteriores if continuos[x] and ultimo_en_salir[x]])
#                print("posibles {}".format(posibles_jefes_filtrados))
                assert len(posibles_jefes_filtrados) <= 1
                if(posibles_jefes_filtrados):
                    assert posibles_jefes_filtrados[0] == ops[0][1]
                    posibles_jefes_mencionados.add(ops[0][1])
            else:
                assert ultima_salida_inesperada is not None
#                print("continuos {}".format(continuos))
                posibles_jefes_mencionados = set([x for x in anteriores & posteriores if ultimo_en_salir[x] and continuos[x] and ultima_salida_inesperada == x])

#    print("posibles jefes menc {}".format(posibles_jefes_mencionados))
    posibles_jefes -= (mencionados - posibles_jefes_mencionados)
        
print(len(posibles_jefes))
if(len(posibles_jefes)):
    print(" ".join(map(str, sorted(posibles_jefes))))