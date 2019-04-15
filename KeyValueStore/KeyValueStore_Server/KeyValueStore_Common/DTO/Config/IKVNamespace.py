from abc import abstractmethod,ABC

class IKVNamespace(ABC):

    @abstractmethod
    def GetKVNamespace(self):
        pass

    
    @abstractmethod
    def GetTTLSeconds(self):
        pass
