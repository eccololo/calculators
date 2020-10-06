from termcolor import colored, cprint
import math
import logging

# Logging config
logging.basicConfig(filename='loges.log', filemode='w',
                    format='%(levelname)s - File: %(filename)s - Line: %(lineno)d '
                           '- Time: %(asctime)s - %(message)s', level=logging.INFO)
email = colored('mstem.net@gmail.com', 'yellow', attrs=['bold'])


def calculate(operation, a, b):
    if b is None:
        result = round_to_4(operation(a))
        return result
    return operation(a, b)


def convert_str_to_method(str):
    return calculator_objects[str]["method"]


def convert_str_to_sympol(str):
    return calculator_objects[str]["symbol"]


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    result_str = round_to_4(a / b)
    return float(result_str)


def multiplicate(a, b):
    return a * b


def modulo(a, b):
    return a % b


def square_root(a):
    return math.sqrt(a)


def round_to_4(a):
    return "{result:.4f}".format(result=a)


calculator_objects = {
    "add": {
        "method": add,
        "symbol": "+",
        "gui_action": "add",
        "description": "- ads two numbers.",
        "color": "yellow"
    },
    "subtract": {
        "method": subtract,
        "symbol": "-",
        "gui_action": "subtract",
        "description": "- subrast two numbers.",
        "color": "yellow"
    },
    "divide": {
        "method": divide,
        "symbol": "/",
        "gui_action": "divide",
        "description": "- divide two numbers.",
        "color": "yellow"
    },
    "mult": {
        "method": multiplicate,
        "symbol": "*",
        "gui_action": "mult",
        "description": "- multiplicate two numbers.",
        "color": "yellow"
    },
    "mod": {
        "method": modulo,
        "symbol": "%",
        "gui_action": "mod",
        "description": "- returns what is left from division.",
        "color": "yellow"
    },
    "sqrt": {
        "method": square_root,
        "symbol": u'\u221A',
        "gui_action": "sqrt",
        "description": "- returns square root of a number.",
        "color": "yellow"
    },
    "quit": {
        "method": None,
        "symbol": None,
        "gui_action": "quit",
        "description": "- type quit or q to exit.",
        "color": "red"
    },
    "actions": {
        "method": None,
        "symbol": None,
        "gui_action": "actions",
        "description": "- show available actions.",
        "color": "blue"
    }
}

actions_colored = []
for action in calculator_objects.values():
    actions_colored.append(colored(action.get("gui_action"), action.get("color"), attrs=['bold']))

console_gui = f"""
====================================================================
|  Welcome to simple console calculator by Mateusz Hyla.           |
|  Available actions:                                              |
|       {actions_colored[0].ljust(31)}{calculator_objects["add"]["description"].ljust(40)} |
|       {actions_colored[1].ljust(31)}{calculator_objects["subtract"]["description"].ljust(40)} |
|       {actions_colored[2].ljust(31)}{calculator_objects["divide"]["description"].ljust(40)} |
|       {actions_colored[3].ljust(31)}{calculator_objects["mult"]["description"].ljust(40)} |
|       {actions_colored[4].ljust(31)}{calculator_objects["mod"]["description"].ljust(40)} |
|       {actions_colored[5].ljust(31)}{calculator_objects["sqrt"]["description"].ljust(40)} |
|       {actions_colored[6].ljust(31)}{calculator_objects["quit"]["description"].ljust(40)} |
|       {actions_colored[7].ljust(31)}{calculator_objects["actions"]["description"].ljust(40)} |
|  Type one of this actions to start                               |
"""

print(console_gui)

while True:
    action = input("You action is: ")
    action = action.strip()

    action_colored = colored(action, 'red', attrs=['bold'])

    if action == "quit" or action == "q" or action == "exit":
        print("Thank you for your time. Bye.")
        break

    if action == "actions":
        print(console_gui)
        continue

    try:
        if action == "sqrt":
            a = int(input("First number is: "))
            b = None
        else:
            a = int(input("First number is: "))
            b = int(input("Second number is: "))

        result = calculate(convert_str_to_method(action), a, b)  # calculations of operation

        b = "(" + str(b) + ")" if int(b) < 0 else int(b)  # enclosing negative number in ()

        print(f"{a} {convert_str_to_sympol(action)} {b} = {result}") if b is not None \
            else print(f" {convert_str_to_sympol(action)}{a} = {result}") # printing results of operation
    except TypeError:
        print(f"Mismatch in types. Contact admin at {email}.")
        logging.critical("Someone messed with code because this exception should never execute.")
        break
    except NameError:
        print(f"That action is not allowed. For more info contact admin at {email}.")
    except ZeroDivisionError:
        print(f"Second number cannot be 0 if you pick division. For more info contact admin at {email}.")
        logging.warning("Someone tried to divide number 1 by a zero.")
        break
    except KeyError:
        print(f"Internal error of a function. You probably type wrong action:"
              f" {action_colored}. Contact admin at {email}.")
        logging.error("Someone used action which we didn't specify so there is no such key "
                      "in actions dictionary.")
    except ValueError:
        print(f"You typed wrong character, probably a space or something similar instead of a number. "
              f"Contact admin for further explanations at {email}.")
        logging.error("Someone typed a invalid character instead a number.")
