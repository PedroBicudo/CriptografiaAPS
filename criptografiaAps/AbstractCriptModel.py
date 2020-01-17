import abc

class AbstractCriptModel(abc.ABC):

    def get_action(self, action):
        return self.encript if action else self.decript

    @abc.abstractmethod
    def encript(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def decript(self, *args, **kwargs):
        raise NotImplementedError

