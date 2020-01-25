from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def create(self, **params):
        pass

    @abstractmethod
    def fetch(self, **params):
        pass

    @abstractmethod
    def delete(self, **params):
        pass

    @abstractmethod
    def return_all(self, **params):
        pass
