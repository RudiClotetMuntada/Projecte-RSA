from Fast_Modular_Exponentiation import fme # Importem funcions necessàries d'altres fitxers i llibreries de Python
from ENCRYPT_SYST import calculate_block_size


def blocks_to_text(blocks, block_size):
    """
    Converteix els blocs en text de nou
    """
    byte_data = b'' # Creem una nova variable on guardarem els bytes
    for block in blocks: # Per cada bloc a la llista blocks
        block_bytes = block.to_bytes(block_size, 'big') # Converteix els blocs en bytes, llegint de dreta a esquerra és a dir el byte més singificant primer
        byte_data += block_bytes #Guardem el resultat
    byte_data = byte_data.rstrip(b'\x00') #Vam preguntar al IA com eliminar el padding i ens va donar aquesta solució, utilizant la funció rstrip

    # Convertim de tornada a UTF8
    text = byte_data.decode('utf-8')
    return text



def decrypt(encrypted_blocks, n, d):
    """
    Desencripta el missatge, utilitzant els paràmetres n i d de l'RSA.     
    Retorna un string amb el missatge desencriptat
    Un seguit de testos, l'últim ha de fallar.
    >>> decrypt([3000, 3179, 1853], 3233, 2753)
    'Hi!'
    >>> decrypt([669, 1307, 1307, 1759, 524, 99, 28], 3233, 2753)
    'GOODBYE'
    >>> decrypt([3000, 1313, 745, 745, 2185, 1853], 3233, 2753)
    'Hello!'
    >>> decrypt([1058, 4680, 3867, 3867, 3716, 3162, 4132, 3716, 1580, 3867, 2891, 2087], 5561, 4457)
    'Hello world!'
    >>> decrypt([3000, 1313, 745, 745, 2185, 1853], 3233, 2752) 
    'Hello!'
    """
    # Calcula el tamany del bloc utilizant la funció que hem fet servir a l'encriptació
    block_size = calculate_block_size(n)

    # Desencriptem cada bloc
    decrypted_blocks = [] # Creem la llista on tindrem els blocs desencriptats
    for block in encrypted_blocks:
        # Desencriptem la funció fme anteriorment creada
        decrypted_block = fme(block, d, n)
        decrypted_blocks.append(decrypted_block) # Afegim els blocs a la llista


    return blocks_to_text(decrypted_blocks, block_size)
