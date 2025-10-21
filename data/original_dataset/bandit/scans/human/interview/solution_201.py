import sys
f = sys.stdin

C, Hr, Hb, Wr, Wb = map(int, f.readline().strip().split())

if Hr/Wr < Hb/Wb:
    Hr, Hb, Wr, Wb = Hb, Hr, Wb, Wr

if (C % Wr) == 0 and (C // Wr) > 0:
    print((C // Wr)*Hr)
    
elif (C // Wr) == 0:
    print((C // Wb)*Hb)

else:
    nmax =  (C // Wr)
    pmax = nmax*Hr + ((C - nmax*Wr) // Wb) * Hb
    dmax = ((C - (nmax-0)*Wr) % Wb)
    #print(0, pmax, dmax)
    
    #
    #pm1 = (nmax-1)*Hr + ((C - (nmax-1)*Wr) // Wb) * Hb 
    #if pm1>pmax:
    #    pmax = pm1
    if  Hr/Wr > Hb/Wb:
        dx = dmax * (Hb/Wb) / (Hr/Wr - Hb/Wb)    
    elif  Hr/Wr < Hb/Wb: 
        dx = 0 
    else:
        dx = Wb * Wr
        if Wr<Wb:
            nmax =  (C // Wb)
            pmax = nmax*Hb + ((C - nmax*Wb) // Wr) * Hr   
        if Wr>Wb:
            nmax =  (C // Wr)
            pmax = nmax*Hr + ((C - nmax*Wr) // Wb) * Hb   
            
    if Wr>Wb and dx>0:    
        for k in range(1, C//Wr):
            if k*Wr > dx:
                break
            pk = (nmax-k)*Hr + ((C - (nmax-k)*Wr) // Wb) * Hb 
            dk = ((C - (nmax-k)*Wr) % Wb)
            #print(k, pmax, pk, dk)
            if pk>pmax:
                pmax = pk
            if dk==0 :
                break
    elif Wr<Wb and dx>0:   
        for j in range(1, C//Wb+1):
            k = nmax - (C-j*Wb)//Wr
            if k*Wr > dx:
                break
            
            pk = (nmax-k)*Hr + ((C - (nmax-k)*Wr) // Wb) * Hb 
            dk = ((C - (nmax-k)*Wr) % Wb)
            #print(j, k, pmax, pk, dk, (nmax-k), ((C - (nmax-k)*Wr) // Wb) )
            if pk>pmax:
                pmax = pk
                #dmax = dk
            if dk==0 :
                break            
            
#    elif Wr<Wb and dx>0:   
#        for j in range(1, C//Wb+1):
#            k = (j*Wb - dmax)//Wr
#            if k*Wr > dx:
#                break
#            pk = (nmax-k)*Hr + ((C - (nmax-k)*Wr) // Wb) * Hb 
#            dk = ((C - (nmax-k)*Wr) % Wb)
#            print(j, k, pmax, pk, dk, (nmax-k), ((C - (nmax-k)*Wr) // Wb) )
#            if pk>pmax:
#                pmax = pk
#                #dmax = dk
#            if dk==0 :
#                break
            
    print(pmax)