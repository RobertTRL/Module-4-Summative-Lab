import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
from utils.helpers import ClassProperty

class User:
    #TODO: Place docstring
    __users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.__id_number = uuid.uuid4()
        User.__users.append(self)
        
    @property
    def id_number(self):
        return self.__id_number

    @ClassProperty
    def count(cls):
        return len(cls._User__users)  
    
    @classmethod
    def users_list(cls):
        return [{user} for user in cls.__users]
    
    def __str__(self):
        return f"User info:\n{self.name=},\n{self.email=}"
    
    def __repr__(self):
        return f"Parent class: {self.__class__.__name__}, id_number: {self.id_number}, name: {self.name}, email: {self.email}"



u1 = User("Robert", "robert@email.com")
u2 = User("John", "john@email.com")
print(User.count)
print(u1.id_number)
print(u2.id_number)
print(User.users_list())
print(str(u1))




    
   