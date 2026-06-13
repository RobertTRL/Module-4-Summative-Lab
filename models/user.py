import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
import json
from utils.helpers import ClassProperty

class User:
    """Class representing a user. Has instance attributes namely name, email and id_number and a class attribute users."""

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.__id_number = str(uuid.uuid4())

    @property
    def id_number(self):
        return self.__id_number
    
    def to_dict(self):
        return {"name": self.name, "email": self.email, "id_number": self.id_number}
        
    def __str__(self):
        """Instance dunder method - returns a summarized string representation of the instance."""
        return f"User info:\n{self.name=},\n{self.email=}"
    
    def __repr__(self):
        """Instance dunder method - returns a complete string representation of the instance."""
        return f" Parent class: {self.__class__.__name__}, id_number: {self.id_number}, name: {self.name}, email: {self.email} "





    
   