class Namespace:
    @property
    def TenantId(self):
        return self.__tenantId
    @TenantId.setter
    def TenantId(self,tenantId):
        self.__tenantId=tenantId

    @property
    def ServiceId(self):
        return self.__createAppId
    @ServiceId.setter
    def ServiceId(self,serviceId):
        self.__createAppId=serviceId

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,name):
        self.__name=name
