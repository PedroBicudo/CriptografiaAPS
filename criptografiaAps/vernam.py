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