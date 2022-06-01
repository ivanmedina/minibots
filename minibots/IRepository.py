from abc import ABCMeta, abstractmethod

class IBot(metaclass=ABCMeta):

    @abstractmethod
    def bconnect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get(self):
        pass