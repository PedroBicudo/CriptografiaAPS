"""Direcionar os parametros argparse para as respectivas criptografias."""
# Importando modulos usados
from string import ascii_letters, punctuation, hexdigits
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
    # Caracter especial ’ nao esta presente em punctuation
    characaters = ascii_letters
    if all('0x' in value for value in msg.split(':')):
        msg = msg.split(':')
    return "".join(choices(characaters, k=len(msg)))

def removerArgs(kwargs, name):
    return kwargs.pop(name)

def getText(kwargs):
    # Texto
    if kwargs.get('file') != None:
        kwargs['txt'] = kwargs['file'].read()
    
    return removerArgs(kwargs, 'file')

def chaveExiste(kwargs):
    # Chave, se existir
    if kwargs.get('key'):
        if kwargs.get('key') == "$RANDOM$":
            kwargs['key'] = getRandomKey(kwargs['txt'])

    return kwargs

def manipularArgumentos(**kwargs):
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

    # print(f"Chave: {kwargs['key']}\n")

    args = list(filter(lambda x: x != None, list(kwargs.values())))
    print(f"Text: {cript(*args)}")