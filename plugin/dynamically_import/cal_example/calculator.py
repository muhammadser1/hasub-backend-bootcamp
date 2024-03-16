import importlib.util
import sys


def import_operation(operation_name):
    try:
        spec = importlib.util.find_spec(operation_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(module)
        return module
    except ImportError:
        print(f"Operation '{operation_name}' not found.")
        sys.exit(1)


if __name__ == "__main__":
    # Ensure that at least two arguments are provided
    if len(sys.argv) < 4:
        print("Usage: python calculator.py <operation> <operand1> <operand2>")
        sys.exit(1)

    # Get the operation and operands from command-line arguments
    operation_name = sys.argv[1]
    operand1 = float(sys.argv[2])
    operand2 = float(sys.argv[3])

    module=import_operation(operation_name)
    operation_function_name = operation_name + "_"

    operation_function = getattr(module,operation_function_name)
    result = operation_function(operand1, operand2)
    print(result)