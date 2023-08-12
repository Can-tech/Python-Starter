from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
window.title("Kiss my Ass!")
window.config(padx=20,pady=20)

my_label = Label(text="Dude, this is a label! I just display smth!")
my_label.grid(column=0, row=0)
my_label.config(padx=50, row=0)

#Button James
james_the_button = Button(text="Click Me")
james_the_button.grid(column=1, row=1)

#Button Clark
Clark_the_button = Button(text="'ey I'm new here!")
Clark_the_button.grid(column=2, row=0)


#Entry
my_input = Entry(width=10)
my_input.grid(column=3, row=2)


window.mainloop()