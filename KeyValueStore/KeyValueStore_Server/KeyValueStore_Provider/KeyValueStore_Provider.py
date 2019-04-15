from etcd3 import Client
import KeyValueStore_Server.KeyValueStore_Common as kvscommon
import KeyValueStore_Server.KeyValueStore_Common.DTO.Config.EtcdConfig as r
#from kvscommon import DTO as d
from KeyValueStore_Server.KeyValueStore_Common.DTO.Utility.Serializer import Serializer
from KeyValueStore_Server.KeyValueStore_Common.DTO.Utility.KeyName import KeyName
import ssl
from typing import Dict

#import logger
#from etcd_Common import EtcdConfig as ec

class EtcdProvider:
    def __init__(self,config):
        self.__etcdConfigObj = r.EtcdConfig(config['Protocol'],config['Host'],config['Port'])
        self.__etcdConfigObj.Validate()
        __connectionUrl = self.__etcdConfigObj.ConnectionUrl()
        try:
            self.__Connect()
            self.__dic={}
        except Exception as e:
            raise Exception(str(e))
        #logger = logger.getLogger(__name__)

    #Switch case to get namespace data or file data
    def __GetKeyDetails(self,case,data):
        def GetNamespaceData(data):
            try:
                return data.leaves
            except Exception as e:
                raise Exception(str(e))

        def GetFileData(data):
            try:
                return data.value
            except Exception as e:
                raise Exception(str(e))
        return {
            True: GetNamespaceData(data),
            False: GetFileData(data)
        }.get(case,"Invalid")

    def __Connect(self):
        #self.__client = etcd.Client(host=self.__etcdConfigObj.Host, protocol=self.__etcdConfigObj.Protocol, port=self.__etcdConfigObj.Port)
        self.__client = etcd.Client(host='localhost', protocol='http', port=2379)
   
    def SetKey(self,nameSpaceId : str, keyId : str="",message="",isMultiple=False) -> str:
        try:
            keyName = self.__Keyformat(nameSpaceId,keyId)
            if message =="":
                d=self.CreateDirectory(keyName)
                print(d)
            else:
                self.__client.write(keyName,message)
            return "Success"
        except Exception as e:
            raise Exception(str(e))

    def GetKey(self,nameSpaceId : str,isNamespace=False,keyId : str="") -> etcd.EtcdResult:
        try:
            keyName = self.__Keyformat(nameSpaceId,keyId)
            msg  = self.__client.read(keyName,recursive=isNamespace)
            results : object = self.__GetKeyDetails(msg.dir,msg)
            return results
        except Exception as e:
            raise Exception(str(e))

    def DeleteKey(self,nameSpaceId : str,keyId : str=''):
        try:
            keyName = self.__Keyformat(nameSpaceId,keyId)
            self.__client.delete(keyName)
            return "Key - {} in Namespace - {} is deleted.".format(keyId,keyName)
        except Exception as e:
            raise Exception(str(e))

    def CreateDirectory(self,keyId : str):
        try:
            self.__client.read(keyId)
        except etcd.EtcdKeyNotFound:
            try:
                response = self.__client.write(keyId,None, dir=True)
                return response
            except etcd.EtcdException as e:
                raise Exception(str(e))
        except Exception as e:
            raise Exception(str(e))
        else:
            raise Exception("Namespace - {} already exists".format(keyId))
    
    def Watch(self,key : str):
        try:
            self.__client.write(key,None, dir=True)
        except Exception as e:
            raise Exception(str(e))

    def __Keyformat(self,nameSpaceId,keyId):
        return "{}{}".format(nameSpaceId,keyId)

    def Namespaceformat(self,tenantId,serviceId,nameSpaceName):
        namespaceList : object = self.GetNamespaceHeaderList(nameSpaceName)
        nameSpace = KeyName.GenerateNodeName(tenantId,serviceId,namespaceList)
        return nameSpace

    def GetNamespaceValues(self,responses):
        for response in responses:
            if response.dir != True:
                self.__dic.update({response.key:response.value})
            else:
                for child in response.leaves:
                    self.GetNamespaceValues(child.leaves)
        return self.__dic

    def GetNamespaceHeaderList(self,headers):
        for header in headers:
            if str(header[0]).startswith('Namespace') == True:
                yield header[1]
            
