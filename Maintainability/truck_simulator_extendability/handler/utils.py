import os
from importlib import import_module

# load file names
operation_files = [f.replace(".json", "") for f in os.listdir('data_files') if
                   f.endswith('.json') and not f.startswith("__")]


def load_roads():
    operations = {}
    for name in operation_files:
        module = import_module(f"data_files.{name}")
        fn = getattr(module, name)
        if callable(fn):
            operations[name] = fn
    return operations
