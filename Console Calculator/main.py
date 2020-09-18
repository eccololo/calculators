from termcolor import colored, cprint
import logging

# Logging config
logging.basicConfig(filename='loges.log', filemode='w',
                    format='%(levelname)s - File: %(filename)s - Line: %(lineno)d '
                           '- Time: %(asctime)s - %(message)s', level=logging.INFO)
email = colored('mstem.net@gmail.com', 'yellow', attrs=['bold'])


def calculate(operation, a, b):
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
    result_str = "{result:.4f}".format(result=a / b)
    return float(result_str)


def multiplicate(a, b):
    return a * b


def modulo(a, b):
    return a % b


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
        "description": "- return what is left from division.",
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
|       {actions_colored[5].ljust(31)}{calculator_objects["quit"]["description"].ljust(40)} |
|       {actions_colored[6].ljust(31)}{calculator_objects["actions"]["description"].ljust(40)} |
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

    a = int(input("First number is: "))
    b = int(input("Second number is: "))

    try:
        result = calculate(convert_str_to_method(action), a, b)
        print(f"{a} {convert_str_to_sympol(action)} {b} = {result}")
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
