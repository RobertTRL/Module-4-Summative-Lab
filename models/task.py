import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import uuid
from utils.helpers import ClassProperty
from models.user import User
from models.project import Project

class Task:
    def __init__(self, title, status, assigned_user_id, project_id):
        self.title = title
        self.status = status
        self.assigned_user_id = assigned_user_id
        self.project_id = project_id
        self.completed = False
        self.__id_number = uuid.uuid4()

    @property
    def id_number(self):
        """Instance property getter - returns the unique id of the instance."""
        return self.__id_number
    
    
    # def assigned_user_info(self):
    #     return any(user for user in User.users_list() if user.id_number == self.id_number)
    
    # def assigned_project_info(self):
    #     return any(project for project in Project.projects_list() if project.id_number == self.project_id)
    
    def __str__(self):
        """Instance dunder method - returns a summarized string representation of the instance."""
        return f"Task info:\n{self.title=},\n{self.status=}, \n{self.assigned_user_id=}, \n{self.project_id=}, \n{self.completed=}, \n{self.id_number=}"
    
    def __repr__(self):
        """Instance dunder method - returns a complete string representation of the instance."""
        return f" Parent class: {self.__class__.__name__}, id_number: {self.id_number}, name: {self.title}, status: {self.status}, completed: {self.completed}, assigned to: {self.assigned_user_id}, project: {self.project_id} "
        
