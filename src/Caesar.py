"""Cifra de cesar."""
from exceptions import SizeStringError
from string import ascii_lowercase
from operator import add, sub


def getRotLetter(letter, rot, operation, alphabet):
    """Obter a letra rotacionada.

    Arguments:
        letter {str} -- Letra a ser rotacionada.
        rot {int} -- Valor de rotacao da cifra.
        operation {BuiltinFunctionType} -- Tipo de operacao.
        alphabet {str} -- Alfabeto a ser usado.

    Returns:
        str -- Letra cifrada.

    """
    if not isinstance(letter, str) or not isinstance(alphabet, str):
        raise TypeError("'letter' e 'alphabet' devem ser do tipo string.")
    
    if len(letter) > 1 or not letter:
        raise SizeStringError("'letter' deve ter length 1.")

    if not isinstance(rot, int):
        raise TypeError("'rot' deve ser do tipo integer.")

    if not callable(operation):
        raise TypeError("'operation' deve ser uma funcao.")


    if letter not in alphabet:
        result = letter

    else:
        pos_letter = alphabet.index(letter)
        result = alphabet[operation(pos_letter, rot) % len(alphabet)]
    return result


def caesar(msg, rot, operation, alphabet=ascii_lowercase):
    """Criptografar/descriptografar a cifra.

    Arguments:
        msg {str} -- Mensagem.
        rot {int} -- Valor de rotacao da cifra.
        operation {BuiltinFunctionType} -- Tipo de operacao.
        alphabet {str} -- Alfabeto a ser usado.
    
    Returns:
        str -- Mensagem criptografada/descriptografada.

    """
    message = map(lambda l: getRotLetter(l, rot, operation, alphabet), msg)
    return ''.join(message)


def encript(msg, rot, alphabet=ascii_lowercase):
    """Encriptar a mensagem.

    Arguments:
        msg {str} -- Mensagem
        rot {int} -- Valor de rotacao da cifra.
    
    Keyword Arguments:
        alphabet {str} -- Alfabeto a ser usado. (default: {ascii_lowercase})
    
    Returns:
        str -- Mensagem criptografada.

    """
    return caesar(msg, rot, add, alphabet)


def decript(msg, rot, alphabet=ascii_lowercase):
    """Desencriptar a mensagem.

    Arguments:
        msg {str} -- Mensagem
        rot {int} -- Valor de rotacao da cifra.
    
    Keyword Arguments:
        alphabet {str} -- Alfabeto a ser usado. (default: {ascii_lowercase})
    
    Returns:
        str -- Mensagem descriptografada.

    """
    return caesar(msg, rot, sub, alphabet)