"""Criptografia OneTimePad via operacao XOR."""


def __hexToChr__(hex_msg):
    r"""Realizar conversao da mensagem em hexadecimal para Caractere.
    
    Arguments:
        hex_msg {str} -- Mensagem em hexadecimal
                exemplo:
                    Entrada:
                        0x74:0x65:0x73:0x74:0x65
                    Saida:
                        ['t', 'e', 's', 't', 'e']

    Returns:
        list -- Lista de valores pertencentes aos caracteres ASCII.

    """
    return list(map(lambda x: chr(int(x, base=16)), hex_msg.split(':')))


def __action__(ord_msg, ord_key):
    """Realizar a operacao XOR, responsavel pela criptografia.
    
    Arguments:
        ord_msg {list[int]} -- Mensagem com caracteres ordenados.
        ord_key {list[int]} -- Chave com caracteres ordenados.
    
    Returns:
        list -- Resultado ordenado da operacao.

    """
    size = len(ord_key) >= len(ord_msg)
    assert size, "'key' e 'msg' devem ter o mesmo tamanho."
    result = []
    for index, letter in enumerate(ord_msg):
        result.append(ord(letter) ^ ord(ord_key[index]))
    return result
    

def encrypt(msg, key):
    """Encriptar a mensagem usando a criptografia OTP.
    
    Arguments:
        msg {str} -- Mensagem a ser criptografada.
        key {str} -- Chave de encriptacao.
    
    Returns:
        str[hex] -- String com formato hexadecimal
            exemplo de saida:
                0x16:0x4:0x7:0x15:0x11

    """
    result = __action__(msg, key)
    return ':'.join(map(hex, result))


def decrypt(hex_msg, key):
    """Desencriptar a mensagem OTP.

    Arguments:
        hex_msg {str[hex]} -- Mensagem string em formato hexadecimal.
        key {str} -- Chave de desencriptacao.
    
    Returns:
        str -- Mensagem descriptografada.

    """
    hex_msg = __hexToChr__(hex_msg)
    return ''.join(map(chr, __action__(hex_msg, key)))

if __name__ == "__main__":
    from itertools import product
    from string import ascii_lowercase
    # Encriptacao
    enc = encrypt('teste', 'abcde')

    # Decriptacao
    dec = decrypt(enc, 'abcde')

    # Tentantiva 
    t = decrypt(enc, 'yncda')

    # Conclusao ASCII One Time Pad
    print("++===========++ ASCIIOneTimePad ++===========++")
    print("Chave verdadeira: abcde")
    print(f"Encriptacao: {enc}\nDesencriptacao: {dec}")
    print(f"Tentativa: {t}")
    print("++===========++++===========++++=============++")