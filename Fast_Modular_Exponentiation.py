from Extended_Euclidean_Algorithm import natural

def fme(M,e,n):
    """ 
    Retorna el resultat del càlcul de la potència M^e mod n. Si M, n o e no són naturals, retorna False.

    >>> fme(11,8,27)
    22

    >>> fme(3,13,7)
    3

    >>> fme(3,0,7)
    False

    >>> fme(3,-4,7)
    False

    >>> fme(3,4.5,7)
    False
    """
    
    if natural(M)==True and natural(e)==True and natural(n)==True:
        
        a=M%n # 1r pas: Reduir la base a mòdul n
        
        q=e//2 # 2n pas: Convertim l'exponent a binari
        breves=[]
        r=e%2
        breves.append(r)
        
        while q != 0:
            r=q%2
            breves.append(r)
            q=q//2

        p=1 
        s=a
        
        for element in breves: # 3r pas: A partir de p i s calculem el resultat
            if element == 1:
                p=(p*s)%n
            s=(s**2)%n
        
        return p
    else:
        return False