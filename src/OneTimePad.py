"""Criptografia OneTimePad via operacao XOR."""
from exceptions import SizeStringError


def hex_to_chr(hex_msg, sep=':'):
    """Realizar conversao da mensagem em hexadecimal para Caractere.
    
    Arguments:
        hex_msg {str} -- Mensagem em hexadecimal (ex: '0x44:0x55:0x66')
        sep {str} -- Delimitador de hexadecimal {default: ':'}.

    Returns:
        list -- Mensagem traduzida para os caracteres da tabela ASCII.

    """
    if not isinstance(hex_msg, str) or not isinstance(sep, str):
        raise TypeError(f"O parametro 'hex_msg' e 'sep' devem ser string.")
    
    dec_msg = list(map(lambda hex_v: int(hex_v, base=16), hex_msg.split(sep)))
    return list(map(lambda dec_v: chr(dec_v), dec_msg))


def action(msg, key):
    """Realizar a operacao XOR, responsavel pela criptografia.
    
    Arguments:
        msg {list} -- Mensagem a ser criptografada.
        key {list} -- Chave de tamanho igual ou superior.
    
    Returns:
        list -- Resultado ordenado da operacao.

    """
    if not isinstance(msg, str) or not isinstance(key, str):
        raise TypeError(f"'msg' e 'key' devem ser do tipo string.")
    
    if len(key) < len(msg):
        raise SizeStringError("'key' deve ter tamanho maior ou igual a 'msg'.")

    result = []
    for index, letter in enumerate(msg):
        result.append(ord(letter) ^ ord(key[index]))
    return result
    

def encrypt(msg, key):
    """Encriptar a mensagem usando a criptografia OTP.
    
    Arguments:
        msg {str} -- Mensagem a ser criptografada.
        key {str} -- Chave de encriptacao.
    
    Returns:
        str -- String com formato hexadecimal (ex: '0xAA:0xBB')

    """
    result = action(msg, key)
    return ':'.join(map(hex, result))


def decrypt(hex_msg, key):
    """Desencriptar a mensagem OTP.

    Arguments:
        hex_msg {str} -- Mensagem em formato hexadecimal. (ex: '0xAA:0xBB')
        key {str} -- Chave de desencriptacao.
    
    Returns:
        str -- Mensagem descriptografada.

    """
    hex_msg = hex_to_chr(hex_msg)
    return ''.join(map(chr, action(hex_msg, key)))
