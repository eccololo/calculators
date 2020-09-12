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

result = calculate(add, 5, 5)
print(result)
#
# while True:
#     action = input("You action is: ")
#     a = int(input("First number is: "))
#     b = int(input("second number is: "))
#
#     if action == "quit" or action == "q":
#         print("Thank you for your time. Bye.")
#         break
#
#     try:
#         result = calculate(action, a, b)
#     except TypeError:
#         print("Mismatch in types. Contact admin.")
#       except NameError:
#           print("That action is not allowed.")
