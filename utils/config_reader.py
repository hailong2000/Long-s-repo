import json

class ConfigReader:
    def __init__(self, config_file="testsetting.json"):
        with open(config_file, 'r') as f:
            self.config = json.load(f)

    def get_url(self):
        return self.config.get("url")

    def get_username(self):
        return self.config.get("username")

    def get_password(self):
        return self.config.get("password")

    def get_timeouts(self):
        return self.config.get("timeouts")