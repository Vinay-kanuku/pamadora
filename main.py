import math
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
PINK = "pink"
RED = "red"
GREEN = "green"
# YELLOW = "yellow"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER = ""
check_marks = ""
cycles = 0


# ---------------------------- TIMER RESET ------------------------------- #
def Reset_Timer():
    global cycles
    global check_marks
    check_marks = ""
    check_mark.config(text="")
    window.after_cancel(TIMER)
    canvas.itemconfig(text, text="00:00")
    Labels.config(text="TIMER", fg="green")
    cycles = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def detect_click():
    global cycles
    global check_marks
    cycles += 1
    if cycles % 8 == 0:
        check_marks += "✔"
        Labels.config(text="L_BREAK", fg=RED)
        count_do(LONG_BREAK_MIN * 60)
        check_mark.config(text=check_marks)
    elif cycles % 2 == 0:
        Labels.config(text="BREAK", fg=PINK)
        count_do(SHORT_BREAK_MIN * 60)
    else:
        Labels.config(text="WORK", fg=GREEN)
        count_do(math.floor(WORK_MIN * 60))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_do(WORK):
    global TIMER
    global cycles
    Min = math.floor(WORK / 60)
    sec = WORK % 60
    if WORK >= 0:
        if sec < 10 and Min < 10:
            canvas.itemconfig(text, text=f"0{Min}:0{sec}")
        elif sec < 10:
            canvas.itemconfig(text, text=f"{Min}:0{sec}")
        elif Min < 10:
            canvas.itemconfig(text, text=f"0{Min}:{sec}")
        else:
            canvas.itemconfig(text, text=f"{Min}:{sec}")

        time.sleep(0.1)
        TIMER = window.after(1000, count_do, WORK - 1)
    else:
        detect_click()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("welcome")
window.config(padx=30, pady=30, bg=YELLOW)
Labels = Label(text="TIMER", bg=YELLOW, fg="green", highlightthickness=0)
Labels.config(font=(FONT_NAME, 30))
Labels.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
i = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=i)
text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 20))
canvas.grid(column=1, row=1)
start = Button(text="Start", bg=YELLOW, command=detect_click)
start.grid(column=0, row=2)
reset = Button(text="Reset", bg=YELLOW, command=Reset_Timer)
reset.grid(column=2, row=2)
check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=2)
window.mainloop()
