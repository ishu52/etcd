from flask import Blueprint
from flask import Flask, request,jsonify
from flask_restplus import Resource,Api
from flask import current_app as app
from KeyValueStore_Server.KeyValueStore_Provider.KeyValueStore_Provider import EtcdProvider

namespaceapi = Blueprint('namespaceapi',__name__)

class Namespace(Resource):
    def __init__(self,tenantId='',serviceId=''):
        self.__etcdObj= EtcdProvider(app.kvconfig)
        if tenantId == '' or serviceId == '':
            self.__tenantId=request.headers.get('TenantId')
            self.__serviceId=request.headers.get('ServiceId')
        else:
            self.__tenantId=tenantId
            self.__serviceId=serviceId 
        self.__nameSpaceId = self.__etcdObj.Namespaceformat(self.__tenantId,self.__serviceId,request.headers)

    def get(self):
        try:
            responses = self.__etcdObj.GetKey(self.__nameSpaceId,True,'')
            return jsonify(self.__etcdObj.GetNamespaceValues(responses))
        except Exception as e:
            return str(e)
        
    def post(self):
        try:
            responseMsg = self.__etcdObj.SetKey(self.__nameSpaceId)
            return responseMsg
        except Exception as e:
            return str(e)

    def delete(self):
        try:
            responseMsg = self.__etcdObj.DeleteKey(self.__nameSpaceId)
            return responseMsg
        except Exception as e:
            return str(e)

class Namespaces(Resource):
    def __init__(self,tenantId='',serviceId=''):
        self.__etcdObj= EtcdProvider(app.kvconfig)
        if tenantId == '' or serviceId == '':
            self.__tenantId=request.headers.get('TenantId')
            self.__serviceId=request.headers.get('ServiceId')
        else:
            self.__tenantId=tenantId
            self.__serviceId=serviceId 
        self.__nameSpaceId = self.__etcdObj.Namespaceformat(self.__tenantId,self.__serviceId,request.headers)

    def get(self):
        try:
            result=[]
            responses = self.__etcdObj.GetKey(self.__nameSpaceId)
            for response in responses:
                if response.dir == True:
                    result.append(response.key)
            return jsonify(result)
        except Exception as e:
            return str(e)



