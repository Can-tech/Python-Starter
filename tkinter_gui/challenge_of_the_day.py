# Mile-to-Km Converter
from tkinter import *

window = Tk()
window.title("Converter Mile -> Km")
window.config(padx=30, pady=30)

def handle_calculate():
    km=float(mile_input.get())*1.6
    converted_text_label.config(text=km)



mile_input = Entry()
mile_input.grid(column=1,row=0)
mile_input.focus()
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

converted_text_front_label = Label(text="is equal to:")
converted_text_front_label.grid(column=0, row=1)
converted_text_label = Label(text="none")
converted_text_label.grid(column=1,row=1)
converted_text_end_label = Label(text="Km")
converted_text_end_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=handle_calculate)
calculate_button.grid(column=1, row=2)






window.mainloop()