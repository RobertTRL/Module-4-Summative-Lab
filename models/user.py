import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
import json
from utils.helpers import ClassProperty

class User:
    """Class representing a user. Has instance attributes namely name, email and id_number and a class attribute users."""
    
    with open("../data/data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    def __init__(self, name, email):
        """Constructor method - takes name and email as arguments, generates a unique id for the instance and appends itself to the users list."""
        self.name = name
        self.email = email
        self.__id_number = uuid.uuid4()             # Generates a unique id using the uuid module
        self.__add_user()                   # Appends itself to the private class attribute users
        
    @property
    def id_number(self):
        """Instance property getter - returns the unique id of the instance."""
        return self.__id_number

    @ClassProperty                                  # Class descriptor used to make a class property because stacking the @classmethod and @property has become deprecated 
    def count(cls):
        """Class property getter - returns the number of instances of the class by accessing the private class attribute users and returning its length."""
        return len(cls.__get_users())  
    
    @classmethod
    def users_list(cls):
        """Class method - returns a list of dictionaries each containing information about a user."""
        return [{user} for user in cls.__get_users()]     # Uses list comprehension to elegantly return a list of dictionaries 
    
    def __add_user(self):
        info = {"name": self.name, "email": self.email, "id_number": self.id_number}

        with open("../data/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        data["users"].append(info)

        with open("../data/data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def delete_user(cls, user_id):
        with open("../data/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        remaining_users = [user for user in data["users"] if user["id_number"] != user_id]

        if remaining_users == data["users"]:
            raise ValueError("User not found.")

        with open("../data/data.json", "w", encoding="utf-8") as f:
            data["users"] = remaining_users
            json.dump(data, f, indent=4)
        
    @classmethod
    def __get_users(cls):
        with open("../data/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data["users"]
    
    def __str__(self):
        """Instance dunder method - returns a summarized string representation of the instance."""
        return f"User info:\n{self.name=},\n{self.email=}"
    
    def __repr__(self):
        """Instance dunder method - returns a complete string representation of the instance."""
        return f" Parent class: {self.__class__.__name__}, id_number: {self.id_number}, name: {self.name}, email: {self.email} "





    
   