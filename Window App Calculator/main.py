from tkinter import *


def action_result():
    pass


def add():
    pass


def minus():
    pass


def mult():
    pass


root = Tk()

plus_button = Button(root, text="+", command=add, padx=20, pady=20)
plus_button.grid(row=4, column=0)

minus_button = Button(root, text="-", command=minus, padx=20, pady=20)
minus_button.grid(row=4, column=1)

mult_button = Button(root, text="*", command=mult, padx=20, pady=20)
mult_button.grid(row=5, column=2)

result_button = Button(root, text="=", command=action_result, bg="gray", padx=46, pady=46)
result_button.grid(row=5, column=0, columnspan=2, rowspan=2)

root.mainloop()
