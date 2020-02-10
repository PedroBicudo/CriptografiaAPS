"""Criptografia Cifra de César."""
from criptografiaAps.AbstractCriptModel import AbstractCriptModel

class Caesar(AbstractCriptModel):

    def _get_rot_letter(self, letter, rot, operation, alphabet):
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
        if len(letter) > 1 or not letter:
            raise ValueError("'letter' deve ter length 1.")

        if letter not in alphabet:
            letter_new = letter

        else:
            letter_pos = alphabet.index(letter)
            letter_new = alphabet[operation(letter_pos, rot) % len(alphabet)]
        
        return letter_new
    
    def encript(self, text, rot):
        ...

    def decript(self, enc_text, rot):
        ...