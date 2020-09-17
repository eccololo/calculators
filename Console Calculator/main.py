def calculate(operation, a, b):
    return operation(a, b)


def convert_str_to_method(str):
    methods_dics = {
        "add": add,
        "subtract": subtract,
        "divide": divide,
        "multiplicate": multiplicate,
    }

    return methods_dics[str]


def convert_str_to_sympol(str):
    methods_dics = {
        "add": "+",
        "subract": "-",
        "divide": "/",
        "multiplicate": "*",
    }

    return methods_dics[str]


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
        result = calculate(convert_str_to_method(action), a, b)
        print(f"{a} {convert_str_to_sympol(action)} {b} = {result}.")
    except TypeError:
        print("Mismatch in types. Contact admin.")
    except NameError:
        print("That action is not allowed.")
    except ZeroDivisionError:
        print("Second number cannot be 0 if you pick division.")
    except KeyError:
        print(f"Internal error of a function. You probably type wrong action: {action}. Contact admin.")
