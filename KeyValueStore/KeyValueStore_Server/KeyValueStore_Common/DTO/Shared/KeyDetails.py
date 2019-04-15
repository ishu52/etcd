class KeyDetails:
    @property
    def KeyValueEntries(self):
        return self.__keyValueEntries
    @KeyValueEntries.setter
    def KeyValueEntries(self,keyValueEntries : dict):
        self.__keyValueEntries=keyValueEntries