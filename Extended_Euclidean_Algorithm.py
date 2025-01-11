def natural(x):
    """
    Retorna True si un nombre és natural i False si no és natural.

    >>> natural(8)
    True

    >>> natural(0)
    False

    >>> natural(-8)
    False

    >>> natural(8.5)
    False

    >>> natural(-8.5)
    False
    """
    if isinstance(x, int)==True and x>0: #isinstance ha sigut idea del chat. La primera part és per saber si és enter. Segons el chat és la manera més òptima. Després mirem si és un natural 
        return True
    else:
        return False


def euclides(n,a):
    """
    Retorna x,y (coeficients de la identitat de Bézout que fan que n*x+a*y=MCD(n,a)) i l'MCD. 
    Si n o a no són naturals o bé n=a, retorna False.

    >>> euclides(15,15)
    False

    >>> euclides(15,8)
    (-1, 2, 1)

    >>> euclides(8,15)
    (2, -1, 1)

    >>> euclides(4023,325)
    (37, -458, 1)

    >>> euclides(325,4023)
    (-458, 37, 1)

    >>> euclides(8,1)
    (0, 1, 1)

    >>> euclides(1,8)
    (1, 0, 1)

    >>> euclides(8,15.5)
    False
    """
    if natural(n)==True and natural(a)==True: # Comprovem n i a són naturals
        if n<a: # Canviem l'ordre si n < a
            nbona=a
            abona=n
        elif n>a: # Deixem igual si n > a
            nbona=n 
            abona=a
        elif n==a:
            return False
    else:
        return False
    
    iteracions=0; # Iniciem les iteracions a 0
    valorsq=[]; # Creem la llista buida on es guardaran els valors dels quocients
    
    while abona!=0: # Calculem tots els r i q
        r=nbona%abona
        q=nbona//abona
        nbona=abona
        abona=r

        iteracions=iteracions+1
        valorsq.append(-q)
    
    del valorsq[-1] #Elimino l'últim coeficient, no interessa
    mcd=nbona
    
    if iteracions==1: # Tenim en compte si introduim euclides(x, 1)
        if n<a:
            x=1
            y=0
            
        elif n>a:
            x=0
            y=1
        
    elif iteracions>1: 
        if n<a:
            nbona2=a
            abona2=n
        elif n>a:
            nbona2=n
            abona2=a
            
        x=1
        y=valorsq[-1]
        index=-2
            
        while (nbona2 * x + abona2 * y) != mcd and abs(index) <= len(valorsq): #abs(index) <= len(valorsq) ha sigut idea del chat perquè em petava
            x,y=y,x+y*valorsq[index]; # Calculem x i y
            index=index-1
        if n<a:
            x,y=y,x

    return x,y,mcd