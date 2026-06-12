import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
from utils.helpers import ClassProperty
from models.user import User

class Task:
    __tasks = []
    def __init__(self, title, description, due_date, assigned_user_id):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assigned_user_id = assigned_user_id
        self.__id_number = uuid.uuid4()
        Task.__tasks.append(self)
    
    @property
    def id_number(self):
        """Instance property getter - returns the unique id of the instance."""
        return self.__id_number

    @ClassProperty                                  # Class descriptor used to make a class property because stacking the @classmethod and @property has become deprecated 
    def count(cls):
        """Class property getter - returns the number of instances of the class by accessing the private class attribute users and returning its length."""
        return len(cls._Task__tasks)
    
    @classmethod
    def users_list(cls):
        """Class method - returns a list of dictionaries each containing information about a task."""
        return [{task} for task in cls.__tasks]     # Uses list comprehension to elegantly return a list of dictionaries 
    
    def assigned_user_info(self):
        return [user for user in User.users_list() if user.id_number == self.assigned_user_id]

    def __str__(self):
        """Instance dunder method - returns a summarized string representation of the instance."""
        return f"Task info:\n{self.title=},\n{self.description=}, \n{self.due_date=}"
    
    def __repr__(self):
        """Instance dunder method - returns a complete string representation of the instance."""
        return f" Parent class: {self.__class__.__name__}, id_number: {self.id_number}, Title: {self.title}, description: {self.description}, due_date: {self.due_date} "
