import uuid
from utils.helpers import ClassProperty 

class User:
    #TODO: Place dostring
    __count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.__id = uuid.uuid4()
        User.count += 1          

    @property
    def id(self):
        return self.__id

    @ClassProperty
    def count(cls):
        return cls._User__count  

    @count.setter
    def count(cls, value):       
        cls._User__count = value

    
   