from tkinter import *

Y_SMALL_BTN_SIZE = 18
X_SMALL_BTN_SIZE = 20

def action_result():
    pass


def add():
    pass


def minus():
    pass


def mult():
    pass


def divide():
    pass


root = Tk()

plus_button = Button(root, text="+", command=add, padx=X_SMALL_BTN_SIZE, pady=Y_SMALL_BTN_SIZE)
plus_button.grid(row=4, column=0)

minus_button = Button(root, text="-", command=minus, padx=X_SMALL_BTN_SIZE, pady=Y_SMALL_BTN_SIZE)
minus_button.grid(row=4, column=1)

mult_button = Button(root, text="*", command=mult, padx=X_SMALL_BTN_SIZE, pady=Y_SMALL_BTN_SIZE)
mult_button.grid(row=5, column=2)

divide_button = Button(root, text="/", command=divide, padx=X_SMALL_BTN_SIZE, pady=Y_SMALL_BTN_SIZE)
divide_button.grid(row=6, column=2)

result_button = Button(root, text="=", command=action_result, bg="gray", padx=46, pady=46)
result_button.grid(row=5, column=0, columnspan=2, rowspan=2)

root.mainloop()
