import json
import os

class SettingsManager:
    def __init__(self, filename="settings.json"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.config_dir = os.path.join(base_dir, "data")
        os.makedirs(self.config_dir, exist_ok=True)
        
        self.filepath = os.path.join(self.config_dir, filename)
        self.data = {
            "language": "en_US",
            "dark_mode": False,
            "32'b_format": True,
            "clean_input": True,
            "clean_output": True,
            "accumulate_results": False,
            "truncate_binaries": True
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