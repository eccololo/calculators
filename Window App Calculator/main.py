from tkinter import *


def action_result():
    pass


def add():
    pass


root = Tk()

plus_button = Button(root, text="+", command=add, padx=20, pady=20)
plus_button.grid(row=4, column=0)


result_button = Button(root, text="=", command=action_result, bg="gray", padx=40, pady=40)
result_button.grid(row=5, column=0, columnspan=2, rowspan=2)

root.mainloop()
