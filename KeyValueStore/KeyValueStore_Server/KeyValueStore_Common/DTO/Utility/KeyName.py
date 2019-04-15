class KeyName:
    @staticmethod
    def GenerateNodeName(nodeName : str,folderName: str,nameSpaceName : object) -> str:
        keyName = list()
        keyName.append(nodeName)
        keyName.append('/')
        if folderName != None:
            keyName.append(folderName)
            keyName.append('/')
        for namespace in nameSpaceName:
            keyName.append(namespace)
            keyName.append('/')
        return "".join(keyName)