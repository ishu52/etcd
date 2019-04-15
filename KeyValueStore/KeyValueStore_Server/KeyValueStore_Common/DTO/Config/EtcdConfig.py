from KeyValueStore_Server.AptKeyValueStore_Common.DTO.Config.IConfig import IConfigInterface

class EtcdConfig(IConfigInterface):
    def __init__(self,protocol,host,port):
        self.Protocol=protocol
        self.Host=host
        self.Port=port

    def Validate(self):
        pass

    def ConnectionUrl(self):
        return self.Protocol+"://"+self.Host+":"+str(self.Port)
