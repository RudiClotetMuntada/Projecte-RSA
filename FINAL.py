from ENCRYPT_SYST import encrypt
from Decryp_SYSTM import decrypt
from RSA_Generation_Key_Algorithm import GenKey  # Importem funcions necessàries d'altres fitxers i llibreries de Python


def test_rsa_with_message(message, p, q): 
    """
    Test RSA d'encriptació i desencriptació amb un missatge donat i uns primers p i q.
    """
    print(f"\nComprovant amb el següent missatge: '{message}'")
    print(" ")

    # Generem clau
    keys = GenKey(p, q)
    if keys == False:
        print("Error! Primers no vàlids")
        return

    n, e, d = keys
    print(f"Claus generades:")
    print(f"n = {n}")
    print(f"e = {e}")
    print(f"d = {d}")

    try:
        # Encriptem
        encrypted_blocks = encrypt(message, n, e)
        print(f"\nBlocs encriptats: {encrypted_blocks}")

        # Desencriptem
        decrypted_text = decrypt(encrypted_blocks, n, d)
        print(f"Text desencriptat: '{decrypted_text}'")

        # Verifiquem
        if decrypted_text == message:
            print("\nCorrecte! El missatge coincideix amb l'original")
        else:
            print("\nError! El missatge NO coincideix amb l'original")

    except ValueError as e:
        print(f"Error durant l'encriptació o desencriptació. Consell: Comprova que els caràcters siguin vàlids!: {e}")


if __name__ == "__main__":
    # Provem amb un missatge llarg. Caràcters, nombres i caràcters especials
    test_message = "Hola! Això és un test d'RSA llarg. Haviam si funciona... 123%%%%====####¥¥¥"

    # Utilitzem primers grans
    p = 911
    q = 619

    test_rsa_with_message(test_message, p, q)