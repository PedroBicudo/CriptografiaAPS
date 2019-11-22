"""Cifra de Vigenère."""
from string import ascii_letters, punctuation
from exceptions import SizeStringError
from operator import add, sub

characters = ascii_letters + punctuation + '’ '


def get_letter(lpos, kpos, operator, alphabet):
    """Obter a nova letra apos a encriptacao/desencriptacao.

    Arguments:
        lpos {int} -- Posicao da letra.
        kpos {int} -- Posicao da chave.
        operator {function} -- Operacao a ser realizada.
        alphabet {str} -- Alfabeto a ser usado.
    
    Returns:
        str -- Letra do alfabeto.

    """
    if not all(isinstance(arg, int) for arg in [lpos, kpos]):
        raise TypeError("'lpos' e 'kpos' devem ser do tipo int.")
    
    if not isinstance(alphabet, str):
        raise TypeError("'alphabet' deve ser do tipo str.")

    if not callable(operator):
        raise TypeError("'operator' deve ser uma funcao.")

    return alphabet[operator(lpos, kpos) % len(alphabet)]


def get_word(msg, key, operator, alphabet):
    """Obter palavra.
    
    Arguments:
        msg {str} -- Texto.
        key {str} -- Chave para encriptacao/decriptacao.
        operator {function} -- Operacao a ser realizada.
        alphabet {str} -- Alfabeto a ser usado.
    
    Returns:
        str -- Texto encriptado/decriptado.

    """
    if len(key) < len(msg):
        raise SizeStringError("'key' deve ter tamanho maior ou igual a 'msg'.")
    
    if not all(isinstance(arg, str) for arg in [key, msg]):
        raise TypeError("'key', 'msg' e 'alphabet' devem ser strings.")
    
    if not set(msg) <= set(alphabet):
        raise IndexError(f"'msg' deve ter todos os caracteres em 'alphabet'.")
    
    if not set(key) <= set(alphabet):
        raise IndexError(f"'key' deve ter todos os caracteres em 'alphabet'.")

    result = ""
    for index, letter in enumerate(msg):
        lpos = alphabet.index(letter)
        kpos = alphabet.index(key[index])
        result += get_letter(lpos, kpos, operator, alphabet)
    return result


def encrypt(msg, key, alphabet=characters):
    """Encriptar a mensagem.

    Arguments:
        msg {str} -- Texto a ser encriptado.
        key {str} -- Chave para encriptacao.
        alphabet {str} -- Alfabeto a ser usado.
    
    Returns:
        str -- Texto encriptado.

    """
    return get_word(msg, key, add, alphabet)


def decrypt(msg, key, alphabet=characters):
    """Decriptar mensagem.
    
    Arguments:
        msg {str} -- Texto encriptado.
        key {str} -- Chave para decriptacao.
    
    Returns:
        str -- Texto decriptado.

    """
    return get_word(msg, key, sub, alphabet)