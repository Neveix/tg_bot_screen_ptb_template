import importlib
from pathlib import Path

def load_screens():
    p = Path("src/screen")
    for path in p.rglob("*.py"):
        if path.name.startswith("_"):
            continue
        fullpath = str(path)
        module_name = fullpath[:-3].replace("/", ".").replace("\\", ".")
        importlib.import_module(module_name)