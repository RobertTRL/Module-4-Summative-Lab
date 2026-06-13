import sys
import os
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from utils.helpers import ClassProperty
from models.user import User

class UserPersistence:
    # TODO: Make a single Persistence class, and create child classes
    def __init__(self, file_path):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            self.file_path.write_text(json.dumps({"users": []}, indent=4))

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def add_user(self, user):
        data = self._load()
        data["users"].append(user.to_dict())
        self._save(data)

    def count(self):
        return len(self.get_all_users())
    
    def get_all_users(self):
        data = self._load()
        return [User.from_dict(u) for u in data["users"]]

    def get_user_by_id(self, user_id):
        data = self._load()

        for user in data["users"]:
            if user["id_number"] == user_id:
                return User.from_dict(user)

        return None

    def get_user_by_email(self, email):
        data = self._load()

        for user in data["users"]:
            if user["email"] == email:
                return User.from_dict(user)

        return None

    def delete_user(self, user_id):
        data = self._load()

        original_len = len(data["users"])
        data["users"] = [
            u for u in data["users"] if u["id_number"] != user_id
        ]

        if len(data["users"]) == original_len:
            raise ValueError("User not found")

        self._save(data)

    def update_user(self, user_id, name=None, email=None):
        data = self._load()

        for user in data["users"]:
            if user["id_number"] == user_id:
                if name:
                    user["name"] = name
                if email:
                    user["email"] = email
                self._save(data)
                return

        raise ValueError("User not found")
