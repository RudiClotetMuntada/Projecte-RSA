from Extended_Euclidean_Algorithm import euclides, natural
from Fast_Modular_Exponentiation import fme

import random

def primer(x): 
    """
    Retorna True si un nombre és primer i False si no ho és o bé si no és natural.

    >>> primer(4.5)
    False

    >>> primer(-8)
    False

    >>> primer(1)
    False

    >>> primer(2)
    True

    >>> primer(3)
    True

    >>> primer(14939)
    True

    >>> primer(14933)
    False
    """

    if x == 1 or natural(x)==False: # 1 per conveni no és primer
        return False

    elif x == 2: # 2 sempre és primer
        return True

    divisor=2
    r=1

    while divisor<=(int(x**0.5)+1) and r!=0: # Comprovem tots els divisors fins a sqrt(x)
        r=x%divisor
        divisor=divisor+1

    if r==0:
        return False

    else:
        return True

def Generar_e(phieuler): 
    """
    En el context de l'RSA, genera una e aleatòria entre 2 i phi(n) i que sigui coprimer amb phi(n).

    En aquest cas, no podem fer un doctest ja que al generar nombres aleatoris no podem saber quin generarà.
    Tantmateix, posarem algun exemple del seu funcionament per veure que genera e correctament.
    """

    trobat=False

    while trobat == False:

        e=random.randint(3,phieuler-1) #Ambdós estan inclosos, per això posem aquests límits.
        _,_,mcd=euclides(e,phieuler)

        if mcd == 1: 
            trobat = True
    
    return e

def GenKey(p,q): 
    """
    En el context de l'RSA, genera una clau pública n,e i una clau privada d donats uns primers p i q. 
    Si p o q no són primers o no són naturals, retorna False.

    En aquest cas, no podem fer un doctest ja que al generar e aleatòria no podem saber quina e generarà.
    Tantmateix, posarem algun exemple del seu funcionament per veure que genera n,e i d correctament.

    >>> GenKey(8,-14)
    False

    >>> GenKey(8,1.4)
    False

    >>> GenKey(8,0)
    False
    """

    if natural(p)==True and natural(q)==True and primer(p)==True and primer(q) == True:

        n=p*q # Seguim els passos de l'RSA
        phieuler=(p-1)*(q-1)
    
        e=Generar_e(phieuler)
    
        d,_,_=euclides(e,phieuler)
    
        if d<0:
            while d<0:
                d=d+phieuler
    
        elif d>0:
            d=d%phieuler

        return(n,e,d)
       
    else:
        return False