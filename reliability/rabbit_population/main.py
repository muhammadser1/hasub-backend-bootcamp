import multiprocessing
import sys


def run_package1():
    """
    Function to run the 'rabbit_sensor' package.

    Raises:
        ImportError: If the 'rabbit_sensor' package is not found.
    """
    try:
        import rabbit_sensor
    except ImportError:
        print("Error: rabbit_sensor package not found.")
        sys.exit(1)


def run_package2():
    """
    Function to run the 'backend' package.

    Raises:
        ImportError: If the 'backend' package is not found.
    """
    try:
        import backend
    except ImportError:
        print("Error: backend package not found.")
        sys.exit(1)


if __name__ == "__main__":
    # Create separate processes for running each package
    process1 = multiprocessing.Process(target=run_package1)
    process2 = multiprocessing.Process(target=run_package2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
