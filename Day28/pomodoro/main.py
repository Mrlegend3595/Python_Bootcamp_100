from tkinter import *
import math
#-------------------Constants----------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

#------------------TIMER RESET--------------#
def reset():
    window.after_cancel(timer)
    title_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    global reps
    reps = 0
#--------------TIMER MECHANISM-------------#
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)


#-------------COUNTDOWN MECHANISM-----------#
def count_down(count):
    count_minute = math.floor(count/60)
    count_seconds = count % 60

    # i want hh:ss
    #dynamic type methode1:
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    #number_formating my_methode2: fstring {num:02d}

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)

#----------------UI SETUP------------------#


window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)

timer_text = canvas.create_text(103, 130,text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)



title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

check_mark_label = Label(bg=YELLOW, fg=GREEN,font=(FONT_NAME, 15, "bold"))
check_mark_label.grid(column=1, row=3)

start_bttn = Button(text="Start",command=start_timer)
reset_bttn = Button(text="Reset", command=reset)
start_bttn.grid(column=0, row=2)
reset_bttn.grid(column=2, row=2)

window.mainloop()