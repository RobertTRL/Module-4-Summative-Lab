import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
from utils.helpers import ClassProperty

class User:
    """Class representing a user. Has instance attributes namely name, email and id_number and a class attribute users."""
    __users = []                                    # Private class attribute, initialized as an empty list

    def __init__(self, name, email):
        """Constructor method - takes name and email as arguments, generates a unique id for the instance and appends itself to the users list."""
        self.name = name
        self.email = email
        self.__id_number = uuid.uuid4()             # Generates a unique id using the uuid module
        User.__users.append(self)                   # Appends itself to the private class attribute users
        
    @property
    def id_number(self):
        """Instance property getter - returns the unique id of the instance."""
        return self.__id_number

    @ClassProperty                                  # Class descriptor used to make a class property because stacking the @classmethod and @property has become deprecated 
    def count(cls):
        """Class property getter - returns the number of instances of the class by accessing the private class attribute users and returning its length."""
        return len(cls._User__users)  
    
    @classmethod
    def users_list(cls):
        """Class method - returns a list of dictionaries each containing information about a user."""
        return [{user} for user in cls.__users]     # Uses list comprehension to elegantly return a list of dictionaries 
    
    def __str__(self):
        """Instance dunder method - returns a summarized string representation of the instance."""
        return f"User info:\n{self.name=},\n{self.email=}"
    
    def __repr__(self):
        """Instance dunder method - returns a complete string representation of the instance."""
        return f" Parent class: {self.__class__.__name__}, id_number: {self.id_number}, name: {self.name}, email: {self.email} "





    
   