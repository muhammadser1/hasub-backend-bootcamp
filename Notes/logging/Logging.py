import logging
import sys

class Calculator:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[logging.StreamHandler(sys.stdout)])
        self.logger = logging.getLogger(__name__)

    def add(self, x, y):
        result = x + y
        self.logger.info(f"Addition: {x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        self.logger.info(f"Subtraction: {x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        self.logger.info(f"Multiplication: {x} * {y} = {result}")
        return result

    def divide(self, x, y):
        if y == 0:
            self.logger.error("Division by zero!")
            raise ValueError("Cannot divide by zero")
        result = x / y
        self.logger.info(f"Division: {x} / {y} = {result}")
        return result

if __name__ == "__main__":
    calculator = Calculator()
    result_add = calculator.add(5, 3)
    result_subtract = calculator.subtract(10, 4)
    result_multiply = calculator.multiply(6, 2)
    result_divide = calculator.divide(10, 1)
