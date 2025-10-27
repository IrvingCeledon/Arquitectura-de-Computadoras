# core/settings_manager.py
import json
import os

class SettingsManager:
    def __init__(self, filepath="settings.json"):
        self.filepath = filepath
        self.data = {
            "language": "English",
            "dark_mode": False,
            "32'b_format": True,
            "clean_input": True,
            "clean_output": True,
            "accumulate_results": False
        }
        self.load()

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self.data.update(json.load(f))

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        
    def get_data(self):
        return self.data
