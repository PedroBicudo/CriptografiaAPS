"""Criptografia Cifra de César."""
from criptografiaAps.AbstractCriptModel import AbstractCriptModel


class Caesar(AbstractCriptModel):
    
    def encript(self, text, rot):
        ...

    def decript(self, enc_text, rot):
        ...