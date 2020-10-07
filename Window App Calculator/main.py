from tkinter import *


def action_result():
    pass


root = Tk()

result_button = Button(root, text="=", command=action_result, bg="gray", padx=40, pady=40)

result_button.grid(row=5, column=0)

root.mainloop()
