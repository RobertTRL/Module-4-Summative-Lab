import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
from utils.helpers import ClassProperty
from models.user import User
from models.project import Project

class Task:
    __tasks = []
    def __init__(self, title, status, assigned_user_id, project_id):
        self.title = title
        self.status = status
        self.assigned_user_id = assigned_user_id
        self.project_id = project_id
        self.completed = False
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
    def tasks_list(cls):
        """Class method - returns a list of dictionaries each containing information about a task."""
        return [{task} for task in cls.__tasks]     # Uses list comprehension to elegantly return a list of dictionaries 
    
    def assigned_user_info(self):
        return any(user for user in User.users_list() if user.id_number == self.id_number)
    
    def assigned_project_info(self):
        return any(project for project in Project.projects_list() if project.id_number == self.project_id)
    
    def __str__(self):
        """Instance dunder method - returns a summarized string representation of the instance."""
        return f"Task info:\n{self.title=},\n{self.status=}, \n{self.assigned_user_id=}, \n{self.project_id=}, \n{self.completed=}, \n{self.id_number=}"
    
    def __repr__(self):
        """Instance dunder method - returns a complete string representation of the instance."""
        return f" Parent class: {self.__class__.__name__}, id_number: {self.id_number}, name: {self.title}, status: {self.status}, completed: {self.completed}, assigned to: {self.assigned_user_id}, project: {self.project_id} "
        
