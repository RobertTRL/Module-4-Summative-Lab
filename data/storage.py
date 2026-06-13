import sys
import os
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from datetime import datetime, timedelta
from models.user import User
from models.project import Project
from models.task import Task

class Persistence:
    _entity_key= None
    _from_dict = None

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.file_path.write_text(
                json.dumps({self._entity_key: []}, indent=4)
            )

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def count(self):
        """Return the total number of stored records."""
        return len(self.get_all())

    def get_all(self):
        """Return every record as a list of model instances."""
        data = self._load()
        return [self._from_dict(item) for item in data[self._entity_key]]

    def get_by_id(self, entity_id):
        """Return a single model instance matching *entity_id*, or None."""
        data = self._load()
        for item in data[self._entity_key]:
            if item["id_number"] == entity_id:
                return self._from_dict(item)
        return None

    def add(self, entity):
        """Append *entity* (must implement to_dict()) to the store."""
        data = self._load()
        data[self._entity_key].append(entity.to_dict())
        self._save(data)

    def delete(self, entity_id):
        """Remove the record with *entity_id*. Raises ValueError if no such record exists."""
        data = self._load()
        original_len = len(data[self._entity_key])
        data[self._entity_key] = [
            item for item in data[self._entity_key]
            if item["id_number"] != entity_id
        ]
        if len(data[self._entity_key]) == original_len:
            raise ValueError(f"Record with id '{entity_id}' not found.")
        self._save(data)

    def update(self, entity_id, **fields):
        data = self._load()
        for item in data[self._entity_key]:
            if item["id_number"] == entity_id:
                for key, value in fields.items():
                    if key in item and value is not None:
                        item[key] = value
                self._save(data)
                return
        raise ValueError(f"Record with id '{entity_id}' not found.")

class UserPersistence(Persistence):
    _entity_key = "users"
    _from_dict = staticmethod(User.from_dict)

    def add_user(self, user):
        self.add(user)

    def get_all_users(self):
        return self.get_all()

    def get_user_by_id(self, user_id):
        return self.get_by_id(user_id)

    def delete_user(self, user_id):
        self.delete(user_id)

    def get_user_by_email(self, email):
        """Return the User whose email matches, or None."""
        data = self._load()
        for user in data["users"]:
            if user["email"] == email:
                return User.from_dict(user)
        return None

    def update_user(self, user_id, name=None, email=None):
        """Update a user's name and/or email."""
        self.update(user_id, name=name, email=email)

class ProjectPersistence(Persistence):
    _entity_key = "projects"
    _from_dict = staticmethod(Project.from_dict)

    # Convenience aliases
    def add_project(self, project):
        self.add(project)

    def get_all_projects(self):
        return self.get_all()

    def get_project_by_id(self, project_id):
        return self.get_by_id(project_id)

    def delete_project(self, project_id):
        self.delete(project_id)

    def update_project(self, project_id, title=None, description=None,
                       due_date=None, completed=None):
        """Update writable fields on a project."""
        self.update(project_id, title=title, description=description, due_date=due_date, completed=completed)

    def get_projects_by_user(self, user_id):
        """Return all projects assigned to *user_id*."""
        return [p for p in self.get_all() if p.assigned_user_id == user_id]

    def pending_within_duration(self, duration):
        now = datetime.now().date()
        return [
            p for p in self.get_all()
            if not p.completed and (p.due_date - now) <= duration
        ]

    def assigned_user_info(self, project_id, user_persistence):
        project = self.get_by_id(project_id)
        if project is None:
            raise ValueError(f"Project '{project_id}' not found.")
        return user_persistence.get_user_by_id(project.assigned_user_id)


class TaskPersistence(Persistence):
    _entity_key = "tasks"
    _from_dict = staticmethod(Task.from_dict)

    # Convenience aliases
    def add_task(self, task):
        self.add(task)

    def get_all_tasks(self):
        return self.get_all()

    def get_task_by_id(self, task_id):
        return self.get_by_id(task_id)

    def delete_task(self, task_id):
        self.delete(task_id)

    def update_task(self, task_id, title=None, status=None, completed=None):
        """Update writable fields on a task."""
        self.update(task_id, title=title, status=status, completed=completed)

    def get_tasks_by_project(self, project_id):
        """Return all tasks that belong to *project_id*."""
        return [t for t in self.get_all() if t.project_id == project_id]

    def get_tasks_by_user(self, user_id):
        """Return all tasks assigned to *user_id*."""
        return [t for t in self.get_all() if t.assigned_user_id == user_id]

    def get_tasks_by_status(self, status):
        """Return all tasks matching *status* (case-insensitive)."""
        status_lower = status.lower()
        return [t for t in self.get_all() if t.status.lower() == status_lower]

    def assigned_user_info(self, task_id, user_persistence):
        task = self.get_by_id(task_id)
        if task is None:
            raise ValueError(f"Task '{task_id}' not found.")
        return user_persistence.get_user_by_id(task.assigned_user_id)

    def assigned_project_info(self, task_id, project_persistence):
        task = self.get_by_id(task_id)
        if task is None:
            raise ValueError(f"Task '{task_id}' not found.")
        return project_persistence.get_project_by_id(task.project_id)