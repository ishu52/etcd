from flask import Flask, request,jsonify
from flask_restplus import Resource,Api
import KeyValueStore_Server as akvs
from Config.Container import Configs,SetConfiguration 
from NamespaceController import Namespace,namespaceapi,Namespaces


app = Flask(__name__)
app.register_blueprint(namespaceapi)
api = Api(app)

parser = api.parser()
parser.add_argument('TenantId',location='headers')
parser.add_argument('ServiceId',location='headers')
parser.add_argument('Namespace1',location='headers')
@api.header('Content-Type', 'application/json')
@api.expect(parser)
class Key(Resource):
    def __init__(self,tenantId='',serviceId=''):
        self.__etcdObj=akvs.KeyValueStore_Provider.KeyValueStore_Provider.EtcdProvider(app.kvconfig)
        if tenantId == '' or serviceId == '':
            self.__tenantId=request.headers.get('TenantId')
            self.__serviceId=request.headers.get('ServiceId')
        else:
            self.__tenantId=tenantId
            self.__serviceId=serviceId
        self.__nameSpaceId = self.__etcdObj.Namespaceformat(self.__tenantId,self.__serviceId,request.headers)

    def get(self,keyId):
        try:
            msg=self.__etcdObj.GetKey(self.__nameSpaceId,False,keyId)
            return msg
        except Exception as e:
            return str(e)  
        
    def post(self,keyId):
        try:
            message=request.get_json()
            responseMsg = self.__etcdObj.SetKey(self.__nameSpaceId,keyId,message)
            return responseMsg
        except Exception as e:
            return str(e)

    def delete(self,keyId):
        try:
            responseMsg = self.__etcdObj.DeleteKey(self.__nameSpaceId,keyId)
            return responseMsg
        except Exception as e:
            return str(e)

class Keys(Resource):
    def __init__(self,tenantId='',serviceId=''):
        self.__etcdObj=akvs.KeyValueStore_Provider.KeyValueStore_Provider.EtcdProvider(app.kvconfig)
        if tenantId == '' or serviceId == '':
            self.__tenantId=request.headers.get('TenantId')
            self.__serviceId=request.headers.get('ServiceId')
        else:
            self.__tenantId=tenantId
            self.__serviceId=serviceId
        self.__nameSpaceId = self.__etcdObj.Namespaceformat(self.__tenantId,self.__serviceId,request.headers)

    #@api.marshal_list_with(_k, envelope='data')
    def post(self):
        try:
            message=request.get_json()
            responseMsg = self.__etcdObj.SetKey(self.__nameSpaceId,'',message,True)
            return responseMsg
        except Exception as e:
            return str(e)

api.add_resource(Key,'/api/keyvaluestore/key/<string:keyId>')
api.add_resource(Namespace,'/api/keyvaluestore/namespace')
api.add_resource(Namespaces,'/api/keyvaluestore/namespaces')

if __name__ == '__main__':
    Configs.config.override({
        "ConfigPath": "configoverride/keyvaluestore.json",
        "LocalConfigPath": "appsettings.json"
        })
    getconfig = SetConfiguration.configuration()
    app.kvconfig=getconfig.Config()
    app.run(host='0.0.0.0',port=30002)
