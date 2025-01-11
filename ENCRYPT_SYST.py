from Fast_Modular_Exponentiation import fme # Importem funcions necessàries d'altres fitxers i llibreries de Python
import math


def calculate_block_size(n):
    """
    Podem treballar en bits o bytes, decidim treballar en bytes,aquesta funcio retorna el numero maxim de bytes que
    podem encriptar en un bloc.
    En un principi el nostre codi no tenia la part de restar 1, pero, una vegada acabat, el vam donar a una
    inteligencia artificial per tal de que sugerir millores, i ens va indicar que per seguretat era millor treballar en
    bits - 1.
    """
    bits = math.floor(math.log2(n)); #Indicat per el professor, ens permet obtenir el numero de bits a n.
    bytes_size = (bits - 1) // 8; #Convertim de bits a bites, tenint en compte el factor de seguretat
    return max(1, bytes_size) #Retornem


def text_to_blocks(text, block_size):
    """
    Converteix el text introduit a format UTF 8 en blocs de la mesura especificada.
    Afegeix padding si es necessari.
    """
    byte_data = text.encode('utf-8') #Converteix el text introduit per nosaltres en format UTF-8 a través de la funció encode de Python. 
   
    #Utilizem encode perquè suposem que l'input serà un string.

    # Aquesta funció l'hem creat amb ajuda de inteligencia artificial
    blocks = [] # Creem la llista buida blocs
    for i in range(0, len(byte_data), block_size): # Fem servir la funció range. Crea una seqüència entre 0, la longitud del byte agafant steps del tamany del bloc.
        block = byte_data[i:i + block_size] # Comencem des d'i fins a i + block size (tamany del bloc)

        # En aquesta part afegim el padding necessari en cas que la longitud no sigui block size

        if len(block) < block_size:
            block = block + b'\x00' * (block_size - len(block)) # El nou bloc serà el bloc que teníem més el padding necesari fins a obtenir la longitud block size

        # Convertim el bloc a un enter
        block_int = int.from_bytes(block, 'big')
        blocks.append(block_int) # Ho afegim a la llista

    return blocks 


def encrypt(text, n, e):
    """
    Funció d'encriptació final.

    Paràmetres:
    text (str): El text a encriptar (el qual convertim a UTF8)
    n (int): Public key
    e (int): Public key

    Retorna una llista dels blocs ja encriptats

    >>> encrypt("Hello!", 3233, 17)
    [3000, 1313, 745, 745, 2185, 1853]
    """
    # Calcula el tamany del bloc
    block_size = calculate_block_size(n)

    # Converteix text a blocs
    blocks = text_to_blocks(text, block_size)

    # Encripta cada bloc
    encrypted_blocks = [] # Creem la llista buida dels blocs encriptats
    for block in blocks:
        # Simplement encriptem utilzant c=m^e fent servir fme
        encrypted_block = fme(block, e, n)
        encrypted_blocks.append(encrypted_block)

    return encrypted_blocks
