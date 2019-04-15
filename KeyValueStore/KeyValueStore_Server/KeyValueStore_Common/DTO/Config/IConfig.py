from abc import abstractmethod,ABC

class IConfigInterface(ABC):
    def __init__(self):
        self.__port=2
        self.__host='127.0.0.1'
        self.__protocol='http'
        self.__allowReconnect = True

    @property
    def Port(self):
        return self.__port
    @Port.setter
    def Port(self,port):
        self.__port=port

    @property
    def Host(self):
        return self._host
    @Host.setter
    def Host(self,host):
        self._host=host

    @property
    def Protocol(self):
        return self._protocol
    @Protocol.setter
    def Protocol(self,protocol):
        self._protocol=protocol

    @abstractmethod
    def Validate(self):
        pass