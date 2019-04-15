from KeyValueStore_Server.KeyValueStore_Common.DTO.Config import IKVNamespace,IConfig

class TenantKVNamespace(IKVNamespace.IKVNamespace):

    def __init__(self,config : IConfig):
        self.__config=config

    def GetKVNamespace(self):
        return self.__config.TenantId +"/"+ self.__config.ServiceId

    def GetTTLSeconds(self):
        pass
