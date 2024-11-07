import math
import calculator

print(math.__name__)
print(calculator.__name__)

print(__name__)

print(calculator.area(5))


if __name__ == "__main__":
    print("This is the main script file")
    print(calculator.subtract(3,5))
