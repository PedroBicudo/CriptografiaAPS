"""Cifra de Vernam."""
from criptografiaAps import AbstractCriptModel
from string import hexdigits

class Vernam(AbstractCriptModel):


    def _is_hex(self, value):
        """Verifica se é um hexadecimal.

        Parameters
        -----------
        value: str
            Possível valor em hexadecimal.
        
        Returns
        -----------
        bool

        """
        value = value.replace('0X', '0x')
        if value.count('0x') > 1:
            raise ValueError("Apenas um hexadecimal deve ser inserido.")

        return set(value.split('0x')[-1]) <= set(hexdigits)
    
    def _hex_to_chr(self, msg_hex, sep=':'):
        """Realizar conversao da mensagem em hexadecimal para Caractere ASCII.

        Parameters
        ----------
        msg_hex: str
            Mensagem em hexadecimal

        sep: str
            Delimitador de hexadecimal {default: ':'}.

        Returns
        ----------
        list
            Lista contendo cada valor hexadecimal traduzido para o seu
            respectivo caractere na tabela ASCII.

        """
        msg_dec = [int(value_hex, base=16) for value_hex in msg_hex.split(sep)]
        return [chr(value_dec) for value_dec in msg_dec]

    def _vernam(self, msg, key):
        """Realizar a operacao XOR, responsavel pela criptografia.

        Parameters
        ----------
        msg: [list|str]
            Mensagem a ser criptografada.

        key: [list|str]
            Chave de tamanho igual ou superior.

        Returns
        ----------
        list
            Valores numéricos inteiros referentes a mensagem criptografada.

        """
        if not isinstance(msg, (str, list)):
            raise TypeError(f"'msg' devem ser do tipo string ou list.")

        if not isinstance(key, (str, list)):
            raise TypeError(f"key' devem ser do tipo string ou list.")

        if len(key) < len(msg):
            raise ValueError("'key' deve ter tamanho maior ou igual a 'msg'.")

        msg_new = []
        for index, letter in enumerate(msg):
            msg_new.append(ord(letter) ^ ord(key[index]))
        return msg_new
