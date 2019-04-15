import jsonpickle

class Serializer:

    @staticmethod
    def deserialize(obj):
        return jsonpickle.decode(obj)
        #if type(obj).__name__ =='instance':
           # return jsonpickle.decode(obj)
        #elif type(obj).__name__ =='generator':
         #   for x in obj:
          #      jsonpickle.decode(x)

    @staticmethod
    def serialize(obj):
        return jsonpickle.encode(obj)
