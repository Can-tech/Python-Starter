import requests
from tkinter import *

window = Tk()
window.title("Kanye Quote")
window.config(padx=20, pady=20)


data=None
def get_new_data():
    global data
    response=requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    data=response.json()
    quote=data["quote"]
    quote_bg_canvas.itemconfig(quote_text, text=quote)

quote_bg_canvas = Canvas(width=300,height=414, highlightthickness=0)
quote_bg_img = PhotoImage(file="API_ISS/background.png")
quote_bg_canvas.create_image(150,207,image=quote_bg_img)
quote_text = quote_bg_canvas.create_text(150, 207, text="Hit the Kanye :)", width=250,font=("Ariel", 20, "italic"),fill="white")
quote_bg_canvas.grid(row=0,column=0)

kanye_face_img = PhotoImage(file="API_ISS/kanye.png")
kanye_face_button = Button(command=get_new_data,image=kanye_face_img,highlightthickness=0, border=0)
kanye_face_button.grid(row=1,column=0)








window.mainloop()