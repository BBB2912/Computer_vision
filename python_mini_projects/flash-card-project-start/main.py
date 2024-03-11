from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
new_record = {}
flip_timer = None


# _____________________________Flip Mechanism ________________________________#
def next_card():
    global new_record, flip_timer
    window.after_cancel(flip_timer)
    new_record = random.choice(words)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=new_record['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text='English', fill='White')
    canvas.itemconfig(word, text=new_record['English'], fill='White')


# _____________________________Save Progress ________________________________#
def is_known():
    words.remove(new_record)
    data = pd.DataFrame(words)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# _____________________________load the csv data ________________________________#
try:
    data = pd.read_csv('data/words_to_learn.csv')
except pd.errors.EmptyDataError or FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
words = data.to_dict(orient='records')
# _____________________________Capstone Flash card ui set up ____________________#
window = Tk()
# window.minsize(1000,800)
window.title('Flasy')
window.config(background=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')

card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text='', font=('Aerial', 40, 'italic'))
word = canvas.create_text(400, 300, text='', font=('Areal', 60, 'bold'))
next_card()

wrong_but = Button(image=wrong, highlightthickness=0, bd=0, relief='ridge', command=next_card)
wrong_but.grid(column=0, row=1)
right_but = Button(image=right, highlightthickness=0, bd=0, relief='ridge', command=is_known)
right_but.grid(column=1, row=1)

window.mainloop()
