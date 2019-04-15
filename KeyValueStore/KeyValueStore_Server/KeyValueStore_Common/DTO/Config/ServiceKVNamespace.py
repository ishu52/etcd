from KeyValueStore_Server.KeyValueStore_Common.DTO.Config import IKVNamespace,IConfig

class ServiceKVNamespace(IKVNamespace.IKVNamespace):

    def __init__(self,config : IConfig):
        self.__config=config
        self.__globalNS = "__GLOBALNS"

    def GetKVNamespace(self):
        return self.__globalNS +"/"+ self.__config.ServiceId

    def GetTTLSeconds(self):
        pass
