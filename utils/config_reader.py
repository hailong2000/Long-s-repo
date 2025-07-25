import os
import json
class ConfigReader:
    def __init__(self, config_file='testsetting.json'):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def get_base_url(self):
        return self.config_data.get('base_url')

    def get_credentials(self):
        return self.config_data.get('credentials', {})

    def get_timeouts(self):
        return self.config_data.get('timeouts', {})