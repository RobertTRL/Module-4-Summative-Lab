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

    def __str__(self):
        """Instance dunder method - returns a summarized string representation of the instance."""
        return f"Project info:\n{self.title=},\n{self.description=}, \n{self.due_date=}"
    
    def __repr__(self):
        """Instance dunder method - returns a complete string representation of the instance."""
        return f" Parent class: {self.__class__.__name__}, id_number: {self.id_number}, Title: {self.title}, description: {self.description}, due_date: {self.due_date} "
