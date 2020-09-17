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
====================================================================
|  Welcome to simple console calculator by Mateusz Hyla.           |
|  Available actions:                                              |
|       actions           - show available actions.                |
|       add               - ads two numbers.                       |
|       subtract          - subrast two numbers.                   |
|       divide            - divide two numbers                     |
|       multiplicate      - multiplicate two numbers               |
|       quit                                                       |
|  Type one of this actions to start                               |
"""

available_actions = ["actions", "add", "subract", "divide", "multiplicate", "quit"]

print(console_gui)

while True:
    action = input("You action is: ")

    if action == "quit" or action == "q":
        print("Thank you for your time. Bye.")
        break

    if action == "actions":
        print(console_gui)
        continue

    a = int(input("First number is: "))
    b = int(input("Second number is: "))

    try:
        result = calculate(action, a, b)
    except TypeError:
        print("Mismatch in types. Contact admin.")
    except NameError:
        print("That action is not allowed.")
    except ZeroDivisionError:
        print("Second number cannot be 0 if you pick division.")


