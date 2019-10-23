"""Direcionar os parametros argparse para as respectivas criptografias."""
from string import ascii_letters as characaters
from random import choices
from RSA import (
    encript as rsa_enc, 
    decript as rsa_dec,
    chaves
)
from OneTimePadASCII import (
    encrypt as asciiotp_enc, 
    decrypt as asciiotp_dec
)
from OneTimePadCustom import (
    encrypt as customotp_enc,
    decrypt as customotp_dec
)
from Caesar import (
    encript as caesar_enc,
    decript as caesar_dec
)
import sys

criptografias = {
    "caesar": {
        "action": {
            "enc": caesar_enc,
            "dec": caesar_dec
        }
    },
    "rsa": {
        "action": {
            "enc": rsa_enc,
            "dec": rsa_dec
        }
    },
    "otp": {
        "action": {
            "enc": customotp_enc,
            "dec": customotp_dec
        }
    },
    "asciiotp": {
        "action": {
            "enc": asciiotp_enc,
            "dec": asciiotp_dec
        }
    }
}


def getRandomKey(msg):
    """Gerar chave aleatoria.
    
    Arguments:
        msg {str} -- Mensagem
    
    Returns:
        str -- Chave aleatoria de acordo com o tamanho da mensagem.

    """
    if all('0x' in value for value in msg.split(':')):
        msg = msg.split(':')
    return "".join(choices(characaters, k=len(msg)))


def removerArgs(kwargs, name):
    """Apagar argumentos do dicionario.
    
    Arguments:
        kwargs {dict} -- Dicionario com os parametros.
        name {str} -- Indice a ser apagado.
    
    Returns:
        dict -- kwargs

    """
    return kwargs.pop(name)


def getText(kwargs):
    """Verificar qual o tipo de entrada.
    
    Arguments:
        kwargs {dict} -- Dicionario com os parametros.
    
    Returns:
        dict -- Kwargs modificado.

    """
    if kwargs.get('file') != None:
        kwargs['txt'] = kwargs['file'].read()
    
    return removerArgs(kwargs, 'file')

def chaveExiste(kwargs):
    """Verificar se a chave e aleatoria.
    
    Arguments:
        kwargs {dict} -- Dicionarios com os parametros.
    
    Returns:
        dict -- Kwargs

    """
    if kwargs.get('key'):
        if kwargs.get('key') == "$RANDOM$":
            kwargs['key'] = getRandomKey(kwargs['txt'])

    return kwargs


def manipularArgumentos(**kwargs):
    """Manipular argumentos e direcionar para a respectiva funcao."""
    getText(kwargs)
    chaveExiste(kwargs)
    if kwargs.get('generateKeys') is True:
        keys = chaves()
        print("Chaves publicas:", keys[0])
        print("Chave privada:", keys[1])
        sys.exit(0)
    
    # Acao a ser tomada
    cript = criptografias[kwargs['cript']]['action']
    removerArgs(kwargs, 'cript')
    if kwargs['encript'] is True:
        cript = cript['enc']
    else:
        cript = cript['dec']
    
    removerArgs(kwargs, 'encript')
    removerArgs(kwargs, 'decript')

    args = list(filter(lambda x: x != None, list(kwargs.values())))
    print(f"Text: {cript(*args)}")