import importlib
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <Plugin_name>")
        sys.exit(1)

    Plugin_name = sys.argv[1]

    try:
        module = importlib.import_module(Plugin_name)
    except ModuleNotFoundError:
        print(f"Module '{Plugin_name}' not found.")
        sys.exit(1)

    try:
        plg = module.Plugin(5, 2)
        plg.execute(5, 2)
    except AttributeError:
        print(f"Plugin class not found in module '{Plugin_name}'.")
        sys.exit(1)
