"""Direcionar os parametros argparse para as respectivas criptografias."""
from string import ascii_letters as characaters, hexdigits
from random import choices
from rsa import (
    encript as rsa_enc, 
    decript as rsa_dec, 
    chaves
)
from onetimepad import (
    encrypt as otp_enc,
    decrypt as otp_dec
)
from vigenerecipher import (
    encrypt as vig_enc, 
    decrypt as vig_dec
)
from caesar import (
    encript as caesar_enc, 
    decript as caesar_dec
)
import sys
import _io


def isHex(value):
    """Verificar se o valor inserido e hexadecimal.
    
    Arguments:
        value {str} -- Valor representando o suposto hexadecimal.   
    
    Raises:
        ValueError: "Apenas um hexadecimal deve ser inserido."
    
    Returns:
        bool -- Hexadecimal (True) / Nao hexadecimal (False)

    """
    if not isinstance(value, str):
        raise TypeError("'value' deve ser uma string.")

    if value.count('0x') > 1:
        raise ValueError("Apenas um hexadecimal deve ser inserido.")

    return set(value.split('0x')[-1]) <= set(hexdigits)


def get_random_key(msg):
    """Gerar chave aleatoria.
    
    Arguments:
        msg {str} -- Mensagem
    
    Returns:
        str -- Chave aleatoria de acordo com o tamanho da mensagem.

    """
    if all(isHex(value) for value in msg.split(':')):
        msg = msg.split(':')

    return "".join(choices(characaters, k=len(msg)))


def output_format(msg, output):
    """Formato de saida da mensagem criptografada/descriptografada.

    Arguments:
        msg {str} -- Mensagem.
        output {[None, _io.TextIOWrapper]} -- Tipo de saida.

    """
    if isinstance(output, _io.TextIOWrapper):
        output.write(msg)
        output.close()

    else:
        print(f"Text: {msg}")
    

def get_cript_action(cript, action):
    """Escolher a criptografia e a acao a ser efetuada.
    
    Arguments:
        cript {str} -- Nome da criptografia
        action {bool} -- Encriptar/Desencriptar (True or False)
    
    Raises:
        CriptNotFoundError: A criptografia ainda nao foi implementada.
    
    Returns:
        function/None -- Funcao representando acao ou o valor None.

    """
    if cript == "caesar":
        result = caesar_enc if action else caesar_dec
    
    elif cript == "rsa":
        result = rsa_enc if action else rsa_dec
    
    elif cript == "vigenere":
        result = vig_enc if action else vig_dec
    
    elif cript == "otp":
        result = otp_enc if action else otp_dec
    
    elif cript == "rsaGK":
        keys = chaves()
        print(f"Public Keys: {keys[0]}")
        print(f"Private Keys: {keys[1]}")
        sys.exit(0)

    else:
        raise NotImplementedError(f"O projeto nao implementou '{cript}'.")

    return result


def argument_manipulator(input, output, action, cript, **kwargs):
    """Manipular os argumentos inseridos via linha de comando.
    
    Arguments:
        input {str|_oi.TextIOWrapper} -- Mensagem a ser criptografada.
        output {NoneType|_oi.TextIOWrapper} -- Formato de saida.
        action {bool} -- Encriptar/Desencriptar mensagem.
        cript {str} -- Nome da criptografia.
    """
    input_msg = input.read() if isinstance(input, _io.TextIOWrapper) else input
    cript_action = get_cript_action(cript, action)

    if kwargs.get('key', False):
       if kwargs.get('key') == "$RANDOM$":
            kwargs['key'] = get_random_key(input)
            print(f"Chave: {kwargs['key']}")
    
    # Removendo Valores None
    kwargs = dict(filter(lambda kargs: kargs[-1], kwargs.items()))

    # Escolhendo formato de saida
    output_format(cript_action(input_msg, **kwargs), action)
