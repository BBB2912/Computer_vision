import tkinter.messagebox
from tkinter import *
import random
import json

FONT = ('Courier', 15, 'bold')


# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search_credentials():
    website_entry = website_input.get()
    if website_entry:
        try:
            credentials = json.load(open('Mahireddy_passwords.json', 'r'))
            email_or_username_cred = credentials[website_entry]['email/username']
            password_cred = credentials[website_entry]['password']
            tkinter.messagebox.showinfo(website_entry, f'email:{email_or_username_cred}\n'
                                                   f'password:{password_cred}')
        except KeyError as key:
            tkinter.messagebox.showerror('No data found', f'Sorry, "{key}" not found ')
            clear_all_fields()
        except FileNotFoundError:
            tkinter.messagebox.showerror('No data found', f'Sorry,File not found ')
    else:
        tkinter.messagebox.showwarning('Required info', '!..Required website Name..!')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    SYMBOLS = ['@', '#', '$', '%', '&', '*', '<', '>', ',', '.', '?', '!']
    UPPER_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U',
                     'V', 'W', 'X', 'Y', 'Z']
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pass_symbols = random.choices(SYMBOLS, k=random.randint(2, 4))
    pass_uppers = random.choices(UPPER_LETTERS, k=random.randint(2, 4))
    pass_lowers = random.choices(lower_letters, k=random.randint(2, 4))
    pass_digits = random.choices(DIGITS, k=random.randint(2, 4))
    password = pass_symbols + pass_digits + pass_lowers + pass_uppers
    random.shuffle(password)
    password = ''.join(password)
    password_input.delete(0, 'end')
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_all_fields():
    website_input.delete(0, 'end')
    email_or_username_input.delete(0, 'end')
    password_input.delete(0, 'end')
    return 0


def save_passwords():
    website = website_input.get()
    email_or_username = email_or_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email/username': email_or_username,
            'password': password
        }
    }
    if website and email_or_username and password:
        is_ok = tkinter.messagebox.askokcancel('confirmation', f'confirm details \n website:{website} \n '
                                                               f'email/username:{email_or_username}\n Password:{password}')
        if is_ok:
            try:
                with open('Mahireddy_passwords.json', 'r') as pass_file:
                    data = json.load(pass_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open('Mahireddy_passwords.json', 'w') as pass_file:
                    json.dump(new_data, pass_file, indent=5)
            else:
                with open('Mahireddy_passwords.json', 'w') as pass_file:
                    json.dump(data, pass_file, indent=5)
            finally:
                tkinter.messagebox.showinfo('!--Info--!', f'Successfully save your {website} password')
                clear_all_fields()
    else:
        tkinter.messagebox.showinfo('!--Alert--!', 'Required all fields')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('!__MahiReddy Password Manager__')
window.minsize(600, 400)
window.config(padx=20, pady=20)

img = PhotoImage(file='logo.png')
canva = Canvas(width=200, height=190)
canva.create_image(100, 95, image=img)
canva.grid(column=1, row=0, padx=20, pady=20)

website = Label(text='Website:', font=FONT)
website.grid(column=0, row=1, padx=10, pady=10)
email_or_username = Label(text='Email/UserName:', font=FONT)
email_or_username.grid(column=0, row=2, padx=10, pady=10)
password = Label(text='Password:', font=FONT)
password.grid(column=0, row=3, padx=10, pady=10)

website_input = Entry(width=30)
website_input.grid(column=1, row=1, padx=10, pady=10)
email_or_username_input = Entry(width=50)
email_or_username_input.grid(column=1, row=2, columnspan=2, padx=10, pady=10)
password_input = Entry(width=30)
password_input.grid(column=1, row=3, padx=10, pady=10)

genrate_password = Button(text='Generate Password', font=('Courier', 10, 'bold'), command=generate_password)
genrate_password.grid(column=2, row=3, padx=10, pady=10)

save_password = Button(text='Save', font=('Courier', 15, 'bold'), width=40, background='#9bdeac',
                       command=save_passwords)
save_password.grid(column=0, row=4, columnspan=3, padx=10, pady=10)

search = Button(text='Search', font=('Courier', 10, 'bold'), background='#87e7eb', command=search_credentials)
search.grid(column=2, row=1, padx=10, pady=10)

window.mainloop()
