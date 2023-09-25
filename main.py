from tkinter import *

root = Tk()

# Display
display = Entry(root)
display.grid(row=1, columnspan=3)

# Keys
counter = 1
for x in range(3):
    for y in range(3):
        buttons = Button(root, text=counter, width=2, height=1)
        buttons.grid(row=x + 2, column=y)
        counter += 1

buttons = Button(root, text="0", width=2, height=1)
buttons.grid(row=5, column=1)
root.mainloop()
