"""Cifra de Vernam."""
from criptografiaAps import AbstractCriptModel
from string import hexdigits

class Vernam(AbstractCriptModel):
    """Cifra de Vernam.

    >>> vernam = Vernam()    
    >>> vernam.encript('teste', 'abcde')
    '0x15:0x7:0x10:0x10:0x0'
    >>> vernam.decript('0x15:0x7:0x10:0x10:0x0', 'abcde')
    'teste'

    """

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
        
        Raises
        ---------
        TypeError
            msg ou key devem ser str ou list.
        
        ValueError
            key deve ter tamanho maior ou igual a msg.

        Returns
        ----------
        list
            Valores numéricos inteiros referentes a mensagem criptografada.

        """
        if not isinstance(msg, (str, list)):
            raise TypeError("'msg' devem ser do tipo string ou list.")

        if not isinstance(key, (str, list)):
            raise TypeError("key' devem ser do tipo string ou list.")

        if len(key) < len(msg):
            raise ValueError("'key' deve ter tamanho maior ou igual a 'msg'.")

        msg_new = []
        for index, letter in enumerate(msg):
            msg_new.append(ord(letter) ^ ord(key[index]))
        return msg_new

    def encript(self, msg, key):
        """Encriptar a mensagem usando a cifra de Vernam.

        Parameters
        ----------
        msg: str
            Mensagem a ser criptografada.

        key: str
            Chave de encriptacao.

        Returns
        ----------
        str
            String com formato hexadecimal (ex: '0xAA:0xBB')

        """
        msg_enc = self._vernam(msg, key)
        return ':'.join(map(hex, msg_enc))


    def decript(self, msg_hex, key):
        """Desencriptar a mensagem usando a cifra de Vernam.

        Parameters
        ----------
        msg_hex: str
            Mensagem em formato hexadecimal.

        key: str
            Chave de desencriptacao.

        Returns:
            str -- Mensagem descriptografada.

        """
        msg_int = self._hex_to_chr(msg_hex)
        return ''.join(map(chr, self._vernam(msg_int, key)))
