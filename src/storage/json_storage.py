import json
from datetime import datetime
from storage.base_storage import Storage

class JSONStorage(Storage):
    def __init__(self, file_path):
        self.file_path = file_path

    def save_message(self, user, message):
        conversations = self.load_messages()
        conversations.append({
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "message": message,
        })
        with open(self.file_path, "w") as file:
            json.dump(conversations, file, indent=4)

    def load_messages(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
