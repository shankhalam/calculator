from tkinter import *

root = Tk()

# Display
display = Entry(root, width=30)
display.grid(row=2, columnspan=7)

# Number Keys
counter = 1
for x in range(3):
    for y in range(3):
        buttons = Button(root, text=counter, width=3, height=2)
        buttons.grid(row=x+3, column=y)
        counter += 1

buttons = Button(root, text="0", width=3, height=2)
buttons.grid(row=6, column=1)

# Operator Keys
operator = ['+', '-', '*', '/', '%', '*3.12', '(', ')', '**', '**2']
count = 0
for x in range(4):
    for y in range(3):
        if count < len(operator):
            button = Button(root, text=operator[count], width=3, height=2)
            count += 1
            button.grid(row=x+3, column=y+3)

root.mainloop()
