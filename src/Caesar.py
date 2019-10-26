"""Cifra de cesar."""
from string import ascii_lowercase
from operator import add, sub


def getRotLetter(letter, rot, operation, alphabet):
    """Obter a letra rotacionada.

    Description:
        Sera verificado se a letra existe no alfabeto. Caso
        nao exista, a propria letra sera retornada. Caso contrario
        sua posicao sera mapeada no alfabeto e a nova letra 
        sera buscada a partir de uma operacao fornecida metodo 
        anterior __caesar__ e o resultado dessa operacao estara 
        sujeita ao modulo do tamanho do alfabeto para evitar 
        IndexError.

    Arguments:
        letter {str} -- Letra a ser rotacionada.
        rot {int} -- Valor de rotacao da cifra.
        operation {BuiltinFunctionType} -- Tipo de operacao.
        alphabet {str} -- Alfabeto a ser usado.

    Returns:
        str -- Letra cifrada.

    """
    if letter not in alphabet:
        result = letter
    else:
        pos_letter = alphabet.index(letter)
        result = alphabet[operation(pos_letter, rot) % len(alphabet)]
    return result


def __caesar__(msg, rot, operation, alphabet):
    """Criptografar/descriptografar a cifra.

    Description:
        Vai mapear todas as letras em 'msg', inserindo no
        metodo getRotLetter com os atributos fornecidos pelo
        metodo __caesar__. Em seguida todos os valores serao
        concatenados e retornados ao usuario.
    
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
    print(f"Chave: {rot}\n")
    return __caesar__(msg, rot, add, alphabet)


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
    return __caesar__(msg, rot, sub, alphabet)
    

if __name__ == "__main__":
    from string import ascii_uppercase, ascii_letters
    ##
    ## CASO O CARACTER NAO ESTEJA NO ALFABETO 
    ## ELE MESMO SERA RETORNADO!
    ##

    # Exemplo com alfabeto lowercase
    new_letter = encript('teste', 12)
    print(new_letter)
    org_letter = decript(new_letter, 12)
    print(org_letter, end='\n\n')

    # Exemplo com alfabeto UpperCase
    new_letter = encript('ALGUMA COISA', 55, ascii_uppercase)
    org_letter = decript(new_letter, 55, ascii_uppercase)
    print(new_letter)
    print(org_letter, end='\n\n')

    # Exemplo com ambos os tipos
    new_letter = encript('Alguma Coisa123', 125, ascii_letters)
    org_letter = decript(new_letter, 125, ascii_letters)
    print(new_letter)
    print(org_letter, end='\n\n')