"""Cifra de Vigenere."""
from criptografiaAps import AbstractCriptModel
from string import ascii_letters
from operator import add, sub

CHARACTERS = ascii_letters + ''.join(map(str, range(10)))


class Vigenere(AbstractCriptModel):
    """Cifra de Vigenere.

    >>> vigenere = Vigenere()
    >>> vigenere.encript("hello", "abcde")
    'hfnos'
    >>> vigenere.decript("hfnos", "abcde")
    'hello'

    """
        
    def _get_letter(self, letter_pos, key_pos, operator, alphabet):
        """Obter a nova letra apos a encriptacao/desencriptacao.

        Parameters
        ----------
        letter_pos: int
            Posicao da letra.

        key_pos: int
            Posicao da chave.

        operator: function
            Operacao a ser realizada.

        alphabet: str
            Alfabeto a ser usado.

        Returns
        ----------
        str
            Letra do alfabeto.

        """
        return alphabet[operator(letter_pos, key_pos) % len(alphabet)]

    def _get_word(self, msg, key, operator, alphabet):
        """Obter a palavra criptografada/descriptografada.

        Parameters
        ----------
        msg: str
            Mensagem qualquer.

        key: str
            Chave para encriptacao/decriptacao.

        operator: function
            Operacao a ser realizada.

        alphabet: str
            Alfabeto a ser usado.

        Returns
        ----------
        str
            Texto encriptado/decriptado.
        """
        msg_new = ""
        for index, letter in enumerate(msg):
            letter_pos = alphabet.index(letter)
            key_pos = alphabet.index(key[index])
            msg_new += self._get_letter(
                letter_pos, key_pos,
                operator, alphabet
                )
        return msg_new
    
    def encript(self, msg, key, alphabet=CHARACTERS):
        """Encriptar a mensagem.

        Parameters
        ----------
        msg: str
            Texto a ser encriptado.

        key: str
            Chave para encriptacao.

        alphabet: str
            Alfabeto a ser usado.

        Returns
        ----------
        str
            Texto encriptado.

        """
        return self._get_word(
            msg, 
            key, 
            add,
            alphabet
        )


    def decript(self, msg, key, alphabet=CHARACTERS):
        """Decriptar mensagem.
    
        Parameters
        ----------
        msg: str
            Texto encriptado.
    
        key: str
            Chave para decriptacao.
    
        Returns
        ----------
        str
            Texto decriptado.
    
        """
        return self._get_word(
            msg, 
            key, 
            sub, 
            alphabet
        )
