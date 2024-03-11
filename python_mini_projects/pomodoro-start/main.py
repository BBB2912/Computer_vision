from tkinter import *
import time
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
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer,reps
    window.after_cancel(timer)
    canva.itemconfig(timer_text,text='00:00')
    head_label.config(text='Timer')
    tick.config(text='')
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps,checks
    reps += 1
    WORK_SEC=WORK_MIN*60
    SHORT_BREAK_SEC=SHORT_BREAK_MIN*60
    LONG_BREAK_SEC=LONG_BREAK_MIN*60
    if reps%8==0:
        head_label.config(text='Long Break ')
        count_down(LONG_BREAK_SEC)
    elif reps%2!=0:
        head_label.config(text='Work ')
        count_down(WORK_SEC)
    else:
        head_label.config(text='Short Break ')
        count_down(SHORT_BREAK_SEC)
        tick.config(text='✔' * (reps //  2))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min=int(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec='0'+str(count_sec)
    if count_min<10:
        count_min='0'+str(count_min)
    canva.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.minsize(400,350)
canva=Canvas(width=250,height=250)
tomato=PhotoImage(file='tomato.png')
canva.create_image(125,125,image=tomato)
timer_text=canva.create_text(125,150,text='00:00',font=(FONT_NAME,30,'bold'),fill='#ffffff')
canva.grid(column=2,row=1)

head_label=Label(text='Timer', font=(FONT_NAME,30,'bold'),foreground=RED,background=GREEN)
head_label.grid(column=2,row=0)

start=Button(text='START',background=GREEN,command=start_timer)
start.grid(column=1,row=3)
stop=Button(text='RESET',foreground='black',background=RED,command=reset)
stop.grid(column=3,row=3)
tick=Label(text='',font=(FONT_NAME,25,'bold'),foreground='#004D00',)
tick.grid(column=2,row=4)


window.mainloop()