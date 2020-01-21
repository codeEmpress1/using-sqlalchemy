from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def create(param):
        pass

    @abstractmethod
    def fetch(param):
        pass

    @abstractmethod
    def delete(param):
        pass

    @abstractmethod
    def return_all():
        pass