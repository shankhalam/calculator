from tkinter import *

root = Tk()
i = 0


def get_numbers(num):
    global i
    display.insert(i, num)
    i += 1


def get_operators(opr):
    global i
    length = len(opr)
    display.insert(i, opr)
    i += length


def clear():
    display.delete(0, END)


# Display
display = Entry(root, width=30)
display.grid(row=2, columnspan=7)

# Number Keys
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        buttons = Button(root, text=button_text, width=3, height=2,
                         command=lambda text=button_text: get_numbers(text))
        buttons.grid(row=x + 3, column=y)
        counter += 1

buttons = Button(root, text="0", width=3, height=2, command=lambda: get_numbers(0))
buttons.grid(row=6, column=1)

# Operator Keys
operator = ['+', '-', '*', '/', '%', '*3.12', '(', ')', '**', '**2']
count = 0
for x in range(4):
    for y in range(3):
        if count < len(operator):
            button_operator = operator[count]
            button = Button(root, text=button_operator, width=3, height=2,
                            command=lambda optr=button_operator: get_operators(optr))
            count += 1
            button.grid(row=x + 3, column=y + 3)
Button(root, text="Clear", width=3, height=2, command=clear).grid(row=6, column=0)

root.mainloop()
