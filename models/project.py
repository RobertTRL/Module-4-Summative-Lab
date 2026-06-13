import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
from utils.helpers import ClassProperty
from models.user import User
from datetime import datetime

class Project:
    def __init__(self, title, description, due_date, assigned_user_id):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date).date()
        self.assigned_user_id = assigned_user_id
        self.completed = False
        self.__id_number = uuid.uuid4()
    
    @property
    def id_number(self):
        """Instance property getter - returns the unique id of the instance."""
        return self.__id_number

    # @classmethod
    # def projects_list(cls):
    #     """Class method - returns a list of dictionaries each containing information about a project."""
    #     return [{project} for project in cls.__projects]     # Uses list comprehension to elegantly return a list of dictionaries 
    
    # def assigned_user_info(self):
    #     return any(user for user in User.users_list() if user.id_number == self.assigned_user_id)

    # @classmethod
    # def pending_projects_within_duration(cls, duration):
    #     return [d.due_date for d in Project.projects_list if datetime.now() - d.due_date <= duration]
    
    def __str__(self):
        """Instance dunder method - returns a summarized string representation of the instance."""
        return f"Project info:\n{self.title=},\n{self.description=}, \n{self.due_date=}"
    
    def __repr__(self):
        """Instance dunder method - returns a complete string representation of the instance."""
        return f" Parent class: {self.__class__.__name__}, id_number: {self.id_number}, Title: {self.title}, description: {self.description}, due_date: {self.due_date} "
