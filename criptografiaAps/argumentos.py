"""Direcionar os parametros argparse para as respectivas criptografias."""
import _io

__all__ = []

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


