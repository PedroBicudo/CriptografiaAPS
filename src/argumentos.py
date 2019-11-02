"""Direcionar os parametros argparse para as respectivas criptografias."""
from string import ascii_letters as characaters
from random import choices
from RSA import (
    encript as rsa_enc, 
    decript as rsa_dec,
    chaves
)
from OneTimePad import (
    encrypt as otp_enc, 
    decrypt as otp_dec
)
from VigenereCipher import (
    encrypt as vig_enc,
    decrypt as vig_dec
)
from Caesar import (
    encript as caesar_enc,
    decript as caesar_dec
)
import sys
import _io

criptografias = {
    "caesar": {
        "action": {
            True: caesar_enc,
            False: caesar_dec
        }
    },
    "rsa": {
        "action": {
            True: rsa_enc,
            False: rsa_dec
        }
    },
    "vigenere": {
        "action": {
            True: vig_enc,
            False: vig_dec
        }
    },
    "otp": {
        "action": {
            True: otp_enc,
            False: otp_dec
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


def chaveExiste(kwargs): 
    """Verificar se a chave e aleatoria.
    
    Arguments:
        kwargs {dict} -- KeyWord Arguments
    
    Returns:
        dict -- Kwargs

    """
    if kwargs.get('key'):
        if kwargs.get('key') == "$RANDOM$":
            kwargs['key'] = getRandomKey(kwargs['input'])
            print(f"Chave: {kwargs['key']}")

    return kwargs

def output(msg, output: [None, _io.TextIOWrapper]):
    """Formato de saida da mensagem criptografada/descriptografada.

    Description:
        Se o tipo de saida for _io.TextIOWrapper ele escreve no
        arquivo, caso contrario, simplesmente imprime na tela.
    
    Arguments:
        msg {str} -- Mensagem.
        output {[None, _io.TextIOWrapper]} -- Tipo de saida.
    """
    if output is not None:
        output.write(msg)
        output.close()
        sys.exit(0)
    
    print(f"Text: {msg}")
    

def inputType(kwargs):
    """Define o tipo de entrada.

    Description:
        Buscar ver qual o tipo de entrada, se for arquivo
        sera adicionado o metodo '.read()' e retornado.
    
    Arguments:
        kwargs {dict} -- KeyWord Arguments
    
    Returns:
        dict -- KeyWord Arguments

    """
    if isinstance(kwargs['input'], _io.TextIOWrapper):
        kwargs['input'] = kwargs['input'].read()
    return kwargs


def criptType(kwargs):
    """Obter o tipo de criptografia.
    
    Arguments:
        kwargs {dict} -- KeyWord Arguments.
    
    Returns:
        function -- Funcao representando a acao da criptografia.

    """
    cript = criptografias[kwargs['cript']]['action']
    return cript[kwargs['action']]


def manipularArgumentos(**kwargs):
    """Manipular argumentos inseridos e direcionar para o usuario."""
    # Tipo de entrada
    inputType(kwargs)

    chaveExiste(kwargs)
    if kwargs.get('generateKeys', False):
        keys = chaves()
        print("Chaves publicas:", keys[0])
        print("Chave privada:", keys[1])
        sys.exit(0)
    
    # Acao a ser tomada
    cript = criptType(kwargs)
    kwargs.pop('action')
    kwargs.pop('cript')


    # Tipo de saida
    saida = None if not kwargs.get('output', False) else kwargs['output']
    if kwargs.get('output'):
        kwargs.pop('output')
    
    # Eliminando valores None
    args = list(filter(lambda x: x != None, list(kwargs.values())))

    output(cript(*args), saida)