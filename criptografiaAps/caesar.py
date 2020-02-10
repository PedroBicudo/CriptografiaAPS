"""Criptografia Cifra de César."""
from AbstractCriptModel import AbstractCriptModel
from string import ascii_lowercase

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
        if len(letter) != 1:
            raise ValueError("'letter' deve ter length 1.")

        if letter not in alphabet:
            letter_new = letter

        else:
            letter_pos = alphabet.index(letter)
            letter_new = alphabet[operation(letter_pos, rot) % len(alphabet)]
        
        return letter_new
    
    def _caesar(self, text, rot, operation, alphabet):
        """Criptografar/descriptografar a cifra.

        Parameters
        ----------
        text: str
            Mensagem.

        rot: int
            Valor de rotacao da cifra.

        operation: function
            Tipo de operacao.

        alphabet: str
            Alfabeto a ser usado.

        Returns
        ----------
        str
            Mensagem criptografada/descriptografada.

        """
        text_new = [
            self._get_rot_letter(l, rot, operation, alphabet)
            for l in text
        ]
        return ''.join(text_new)
    
    def encript(self, msg, rot, custom_alphabet=ascii_lowercase):
        """Encriptar a mensagem.

        Parameters
        ----------
        msg: str
            Mensagem.
        
        rot: int
            Valor de rotação.
        
        custom_alphabet: str
            Alfabeto customizado {default: ascii_lowercase}
        
        Returns
        ---------
        str
            Mensagem criptografada.
        """
        return self._caesar(msg, rot, lambda x, y: x+y, custom_alphabet)

    def decript(self, msg, rot, custom_alphabet=ascii_lowercase):
        """Desencriptar mensagem.
        
        Parameters
        ----------
        msg: str
            Mensagem.
        
        rot: int
            Valor de rotação.
        
        custom_alphabet: str
            Alfabeto customizado {default: ascii_lowercase}

        Returns
        ---------
        str
            Mensagem criptografada.        
        """
        return self._caesar(msg, rot, lambda x, y: x-y, custom_alphabet)