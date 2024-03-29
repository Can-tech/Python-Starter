from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    header_label.config(text="Timer")
    reps=0
    check_marks.config(text=(math.ceil(reps/2))*"✔")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec=WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 7 == 0 and reps != 0:
        count_down(5)#short_break_sec
        reps+=1
        header_label.config(text="LONG BREAK", fg=PINK)

    elif reps % 2 == 0:
        count_down(7)#work_sec
        reps+=1
        header_label.config(text="WORK", fg=GREEN)
    elif reps % 2 == 1:
        count_down(3)##short_break_sec
        reps+=1
        header_label.config(text="BREAK", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if(count>0):
       global timer
       timer = window.after(1000, count_down, count - 1)
    else:
        check_marks.config(text=(math.ceil(reps/2))*"✔")
        start_timer()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)
    

header_label=Label(text="Timer", fg=GREEN, bg=YELLOW,font=(FONT_NAME, 50))
header_label.grid(column=1,row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="pomodoro-28/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(100,130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button= Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()



