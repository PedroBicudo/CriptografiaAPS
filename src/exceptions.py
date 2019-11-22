"""Arquivos contendo as exceções do projeto."""

class CriptException(BaseException):
    """Excecao base para o projeto."""

class SizeStringError(CriptException):
    """Erro de tamanho de string."""