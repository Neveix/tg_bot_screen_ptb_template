from json import dumps, loads
from pathlib import Path
from typing import Any

class ConfigManager:
    def __init__(self, path: str = "config/config.json"):
        self.__path = Path(path)
        self.__json: dict[str, Any]
        self.defaults = {
            "development_mode" : False,
            "admin_list": []
        }
    
    def load(self):
        file_path = self.__path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        defaults = self.defaults
        check_fields = False # Для оптимизации
        if file_path.exists():
            try:
                json = loads(file_path.read_text("utf-8"))
                check_fields = True
            except Exception as e:
                print(f"ConfigManager Error {e!r}")
                json = defaults
        else:
            json = defaults
        
        self.__json = json

        if check_fields:
            for name in defaults:
                if name not in json:
                    json[name] = defaults[name]
            self.dump_to_file()

    def dump_to_file(self):
        self.__path.touch(exist_ok=True)
        self.__path.write_text(
            dumps(self.__json, indent=4, ensure_ascii=False), 
            encoding="utf-8")
    
    @property
    def development_mode(self) -> bool:
        return self.__json["development_mode"]
    
    @property
    def admin_list(self) -> list[int]:
        return self.__json["admin_list"]
        
    