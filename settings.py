import json


class Settings:
    _instance = None

    CONFIG_PATH = "./config.json"

    LINK = "/"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._open_config(self.CONFIG_PATH)

    def _open_config(self, path: str) -> None:
        try:
            with open(path) as f:
                self._config = json.load(f)
        except Exception as e:
            raise e

    def get(self, key):
        return self._config[key]
