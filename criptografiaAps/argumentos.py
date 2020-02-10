"""Direcionar os parametros argparse para as respectivas criptografias."""
from criptografiaAps import Caesar
import _io

__all__ = ["argument_manipulator"]

def _output_format(msg, output):
    """Formato de saida da mensagem criptografada/descriptografada.

    Parameters
    ----------
    msg: str
        Mensagem a ser visualizada.

    output: [None, _io.TextIOWrapper]
        Tipo de saida.

    """
    if isinstance(output, _io.TextIOWrapper):
        output.write(msg)
        output.close()

    else:
        print(f"Text: {msg}")

def _get_cript_action(cript, action):
    """Escolher a criptografia e a acao a ser efetuada.

    Parameters
    ----------
    cript: str
        Nome da criptografia

    action: bool
        Encriptar/Desencriptar (True or False)

    Raises
    ----------
    NotImplementedError
        A criptografia especificada nao foi implementada.

    Returns
    ----------
    function|None
        Funcao representando acao na criptografia ou None, como caso
        especifico.

        Existem tres tipos de saida possiveis, sendo elas criptografia,
        descriptografia e geracao de chaves para a criptografia RSA.

    """
    raise NotImplementedError

def argument_manipulator(inpt, output, action, cript, **kwargs):
    """Manipular os argumentos inseridos via linha de comando.

    Parameters
    ----------
    inpt : [str|_oi.TextIOWrapper]
        Mensagem a ser criptografada.

    output: [NoneType|_oi.TextIOWrapper]
        Formato de saida.

    action: bool
        Encriptar/Desencriptar mensagem.

    cript: str
        Nome da criptografia.

    """
    text = inpt.read() if isinstance(inpt, _io.TextIOWrapper) else inpt
    cript_action = _get_cript_action(cript, action)

    # Removendo Valores None
    kwargs = dict(filter(lambda kargs: kargs[-1], kwargs.items()))

    _output_format(cript_action(text, **kwargs), action)