"""Arquivos contendo as exceções do projeto."""
from typing import NamedTuple

class CriptException(BaseException):
    """Excecao base para o projeto."""

class SizeStringError(CriptException):
    """Erro de tamanho de string."""

class CriptNotFoundError(CriptException):
    """A criptografia nao e conhecida."""
    