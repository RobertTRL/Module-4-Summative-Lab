import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
import json
from utils.helpers import ClassProperty

class User:
    """Class representing a user. Has instance attributes namely name, email and id_number and a class attribute users."""

    def __init__(self, name, email):
        """Constructor method - takes name and email as arguments, generates a unique id for the instance and appends itself to the users list."""
        self.name = name
        self.email = email
        self.__id_number = str(uuid.uuid4())             # Generates a unique id using the uuid module
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
        return cls.__get_users()     # Uses list comprehension to elegantly return a list of dictionaries 
    
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
    def edit_user_details(cls, user_id, name=None, email=None):
        if not name and not email:
            raise ValueError("Enter values to edit user details.")
        
        with open("../data/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            users = data["users"]
            user_details = [user for user in users if user["id_number"] == user_id]
            
        edited_user_details = {
            "id_number": user_id,
            "name": name if name else user_details["name"],
            "email": email if email else user_details["email"]
        }

        index = next((i for i, u in enumerate(users) if u["id_number"] == user_id), None)

        if index is None:
            raise ValueError("User not found.")

        users[index] = edited_user_details

        with open("../data/data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def get_user_by_id(cls, username):
        with open("../data/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        if any(user for user in data["users"] if user["name"] == username):
            return [user for user in data["users"] if user["name"] == username][0]
        else:
            raise ValueError("User not found.")

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





    
   