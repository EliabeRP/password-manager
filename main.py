from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import string
def generate_password():
  password_entry.delete(0, END)
  symbols = string.ascii_letters + string.digits + string.punctuation
  new_password = ''.join(random.choice(symbols) for _ in range(10))
  password_entry.insert(0, new_password)
  pyperclip.copy(new_password)
def save():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()

  if len(website) == 0 or len(email) == 0 or len(password) == 0:
    validation_msg = messagebox.showinfo(title='Error', message='Empty Fields')
  else:
    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n Email: {email}\n'
                                                  f'Password: {password}\n Is it ok to save?')
    if is_ok:
      with open('data.txt', 'a') as f:
        f.write(f'{website} | {email} | {password}\n')
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#Emtries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=3)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = Button(text='Generate', command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
