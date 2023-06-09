from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import string
import json


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
  new_data = {
    website: {
      "email": email,
      "password": password,
    }
  }

  if len(website) == 0 or len(email) == 0 or len(password) == 0:
    messagebox.showinfo(title='Error', message='Empty Fields')
  else:
    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\n Email: {email}\n'
                                                  f'Password: {password}\n Is it ok to save?')
    if is_ok:
      try:
        with open('data.json', 'r') as f:
          data = json.load(f)
      except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open('data.json', 'w') as f:
          json.dump(new_data, f)
      else:
        data.update(new_data)
        with open('data.json', 'w') as f:
          json.dump(data, f)
      finally:
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


def find_website_info():
  try:
    with open('data.json', 'r') as f:
      data = json.load(f)
      website = website_entry.get()
      messagebox.showinfo(title=f'{website}', message=f'Email: {data[website]["email"]}\nPassword: {data[website]["password"]}')
  except (KeyError, FileNotFoundError, json.decoder.JSONDecodeError):
    messagebox.showinfo(title='Error', message='Not Found')


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
website_entry = Entry(width=25)
website_entry.grid(column=1, row=1)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

#Buttons
search_button = Button(text='Search', command=find_website_info)
search_button.grid(column=2, row=1)
generate_password_button = Button(text='Generate', command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
