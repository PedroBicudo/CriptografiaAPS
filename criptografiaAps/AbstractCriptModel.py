"""Classe de abstração de criptografias."""
import abc

class AbstractCriptModel(abc.ABC):
    """AbstractCriptModel."""

    def get_action(self, action):
        """Obter ação da criptografia.
        
        Esse método é utilizado pelo arquivo argumentos.
        
        Parameters
        ----------
        action: bool
            Valor boolean para obter ação de criptografia ou descriptografia. 
        
        Returns
        ----------
        method
            Método representando a ação a ser realizada.
        """
        return self.encript if action else self.decript

    @abc.abstractmethod
    def encript(self, *args, **kwargs):
        """Encriptar mensagem."""
        raise NotImplementedError

    @abc.abstractmethod
    def decript(self, *args, **kwargs):
        """Desencriptar mensagem."""
        raise NotImplementedError
