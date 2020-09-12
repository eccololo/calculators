def calculate(operation, a, b):
    return operation(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiplicate(a, b):
    return a * b

console_gui = """
Welcome to simple console calculator by Mateusz Hyla.
Available actions: add, subtract, divide, multiplicate or quit.
Type one of this actions.
"""

print(console_gui)

while True:
    pass