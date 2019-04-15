import os
import json

class Configuration(object):
    def __init__(self, config):
        self._config = config
        self._CheckFile()

    def _CheckFile(self):
        filePath = os.path.join(os.path.abspath(os.curdir)+'/'+self._config['ConfigPath'])
        print(filePath)
        self._isExist = os.path.isfile(filePath)

    def Config(self):
        try:
            if self._isExist == True:
                filePath = os.path.join(os.path.abspath(os.curdir)+'/'+self._config['ConfigPath'])
            elif self._isExist == False:
                filePath=os.path.join(os.path.abspath(os.curdir)+'/Config/'+self._config['LocalConfigPath'])
                print(filePath)
            print(self._ReadConfigFile(filePath))
            return self._ReadConfigFile(filePath)
        except Exception as e:
            return str(e)

    def _ReadConfigFile(self,file):
        with open(file) as f:
            data = json.load(f)
        return {
            "Protocol" : data['AppConfig']["Protocol"],
            "Host" : data['AppConfig']["HostName"],
            "Port" : data['AppConfig']["Port"],
        }


