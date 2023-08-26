from tkinter import *
import math
import random
import pandas
import json
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

#<---------------------------- Button Click -------------------------->
try:
    data = pandas.read_csv("./flash_language_card/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./flash_language_card/data/french_words.csv")
data = pandas.DataFrame(data).to_dict("records")
data_copy = pandas.DataFrame(data).to_dict("records")
word=random.choice(data)
back_bg_img=img=PhotoImage(file="./flash_language_card/images/card_back.png")
bg_img=PhotoImage(file="./flash_language_card/images/card_front.png")    

def reveal_translate():
    my_canvas.itemconfig(canvas_current_word, text=word["English"], fill="white")
    my_canvas.itemconfig(canvas_current_image, image=back_bg_img)
    my_canvas.itemconfig(canvas_title, text="English", fill="white")
def wrong_button_click():
    global word, flip_timer
    window.after_cancel(flip_timer)
    window.after_cancel(timer)
    word=random.choice(data)
    my_canvas.itemconfig(canvas_title, text="French", fill="black")
    my_canvas.itemconfig(canvas_current_word, text=word["French"], fill="black" )
    my_canvas.itemconfig(canvas_current_image, image=bg_img)
    timer=window.after(3000, reveal_translate)

def right_button_click():
    global word, flip_timer
    window.after_cancel(flip_timer)
    window.after_cancel(timer)
    data.remove(word)
    my_data=pandas.DataFrame(data)
    my_data.to_csv("./flash_language_card/data/words_to_learn.csv", index=False)
    
    word=random.choice(data)
    my_canvas.itemconfig(canvas_title, text="French", fill="black")
    my_canvas.itemconfig(canvas_current_word, text=word["French"], fill="black" )
    timer=window.after(3000, reveal_translate)
    my_canvas.itemconfig(canvas_current_image, image=bg_img)


flip_timer=window.after(3000, reveal_translate)
#<---------------------------- UI Design ----------------------------->

my_canvas = Canvas(width=800,height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_current_image = my_canvas.create_image(400,262,image=bg_img)
my_canvas.grid(column=0, row=0, columnspan=2)
canvas_title=my_canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_current_word=my_canvas.create_text(400, 263, text=word["French"], font=("Ariel", 60, "bold"))

wrong_img=PhotoImage(file="./flash_language_card/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=wrong_button_click)
wrong_button.grid(column=0,row=1)
right_img=PhotoImage(file="./flash_language_card/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, border=0, command=right_button_click)
right_button.grid(column=1,row=1)


window.mainloop()