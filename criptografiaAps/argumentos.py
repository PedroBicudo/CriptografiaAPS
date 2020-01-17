"""Direcionar os parametros argparse para as respectivas criptografias."""
import _io

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

