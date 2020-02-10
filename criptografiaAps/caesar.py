"""Criptografia Cifra de César."""
from criptografiaAps.AbstractCriptModel import AbstractCriptModel


class Caesar(AbstractCriptModel):

    def _get_rot_letter(self, letter, rot, operation, alphabet)
        """Obter a letra rotacionada.

        Parameters
        ----------
        letter: str
            Letra a ser rotacionada.

        rot: int
            Valor de rotacao da cifra.

        operation: function
            Tipo de operacao.

        alphabet: str
            Alfabeto a ser usado.

        Returns
        ----------
        str
            Letra cifrada.

        """

    
    def encript(self, text, rot):
        ...

    def decript(self, enc_text, rot):
        ...