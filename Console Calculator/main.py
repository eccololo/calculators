from termcolor import colored, cprint

email = colored('mstem.net@gmail.com', 'yellow', attrs=['bold'])


# available_actions = ["actions", "add", "subtract", "divide", "multiplicate", "quit"]
# available_descriptions = [
#     "- show available actions.",
#     "- ads two numbers.",
#     "- subrast two numbers.",
#     "- divide two numbers.",
#     "- multiplicate two numbers.",
#     "- type quit or q to exit."
# ]


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
    "multiplicate": {
        "method": multiplicate,
        "symbol": "*",
        "gui_action": "mult",
        "description": "- multiplicate two numbers.",
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
|       {actions_colored[3].ljust(31)}{calculator_objects["multiplicate"]["description"].ljust(40)} |
|       {actions_colored[4].ljust(31)}{calculator_objects["quit"]["description"].ljust(40)} |
|       {actions_colored[5].ljust(31)}{calculator_objects["actions"]["description"].ljust(40)} |
|  Type one of this actions to start                               |
"""

print(console_gui)

while True:
    action = input("You action is: ")

    action_colored = colored(action, 'red', attrs=['bold'])

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
        print(f"Mismatch in types. Contact admin at {email}.")
    except NameError:
        print(f"That action is not allowed. For more info contact admin at {email}.")
    except ZeroDivisionError:
        print("fSecond number cannot be 0 if you pick division. For more info contact admin at {email}.")
    except KeyError:
        print(
            f"Internal error of a function. You probably type wrong action: {action_colored}. Contact admin at {email}.")
