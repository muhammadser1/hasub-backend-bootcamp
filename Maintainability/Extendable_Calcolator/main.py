from calcolator import Calculator
import sys

if __name__ == "__main__":
    calc = Calculator()
    num1,num2,operator = sys.argv[1:]
    print(calc.calculate(num1,num2,operator))