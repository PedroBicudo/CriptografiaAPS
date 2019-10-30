"""Criptografia One Time Pad customizada."""
from types import BuiltinFunctionType
from string import ascii_letters, punctuation
from operator import add, sub

characters = ascii_letters + punctuation + '’ '

def verificadorDeVariaveis(types=[], *args):
    """Verificar se as variaveis estao nos tipos corretos.
    
    Keyword Arguments:
        types {list} -- Lista de tipos (default: {[]})
    
    Raises:
        TypeError: "'msg' deve ser 'tipo'."

    """
    assert len(types) is len(args), "'args' e 'types' com tamanhos diferentes."
    erros = []
    for index, arg in enumerate(args):
        type_name = types[index].__name__
        if isinstance(arg, types[index]) is False:
            erros.append(f"\n'{arg}' deve ser '{type_name}'.")

    if erros:
        raise TypeError("".join(erros))


def getLetter(lpos, kpos, operator, alphabet):
    """Obter a nova letra apos a encriptacao/desencriptacao.

    Arguments:
        lpos {int} -- Posicao da letra.
        kpos {int} -- Posicao da chave.
        operator {BuiltinFunctionType} -- Operacao a ser realizada.
        alphabet {str} -- Alfabeto a ser usado.
    
    Returns:
        str -- Letra do alfabeto.

    """
    verificadorDeVariaveis(
        [int, int, BuiltinFunctionType, str],
        lpos, kpos, operator, alphabet
    )
    return alphabet[operator(lpos, kpos) % len(alphabet)]


def getWord(msg, key, operator, alphabet):
    """Obter palavra.
    
    Arguments:
        msg {str} -- Texto.
        key {str} -- Chave para encriptacao/decriptacao.
        operator {BuiltinFunctionType} -- Operacao a ser realizada.
        alphabet {str} -- Alfabeto a ser usado.
    
    Returns:
        str -- Texto encriptado/decriptado.

    """
    verificadorDeVariaveis(
        [str, str, BuiltinFunctionType, str],
        msg, key, operator, alphabet
        )
    size_msg = len(list(set(msg) - set(alphabet)))
    size_key = len(list(set(msg) - set(alphabet)))
    assert len(key) == len(msg), "'key' e 'msg' devem ter o mesmo tamanho."
    assert  size_msg == 0, f"'msg' deve ter todos os caracteres em {alphabet}."
    assert  size_key == 0, f"'key' deve ter todos os caracteres em {alphabet}."
    
    result = ""
    for index, letter in enumerate(msg):
        lpos = alphabet.index(letter)
        kpos = alphabet.index(key[index])
        result += getLetter(lpos, kpos, operator, alphabet)
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
    return getWord(msg, key, add, alphabet)


def decrypt(msg, key, alphabet=characters):
    """Decriptar mensagem.
    
    Arguments:
        msg {str} -- Texto encriptado.
        key {str} -- Chave para decriptacao.
    
    Returns:
        str -- Texto decriptado.

    """
    return getWord(msg, key, sub, alphabet)

if __name__ == "__main__":
    from string import ascii_lowercase
    # Encriptacao
    enc = encrypt('callric', 'testete', alphabet=ascii_lowercase)
    
    # Decriptacao
    dec = decrypt(enc, 'testete', ascii_lowercase)

    # tentativa resultado=vendeta
    dec1 = decrypt(enc, 'aaqbrig')

    # tentativa resultado=vegetal
    dec2 = decrypt(enc, 'aaxacbv')

    # Conclusao CustomOneTimePad
    print("\n++===========++ CustomOneTimePad ++========++")
    print("Chave verdadeira: testete")
    print(f"Encriptacao: {enc}\nDesencriptacao: {dec}")
    print(f"Tentativas legiveis: {dec1}, {dec2}")
    print("++===========++++===========++++===========++\n")
