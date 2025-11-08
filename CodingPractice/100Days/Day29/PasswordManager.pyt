from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=150)

def showPopUp():
  messagebox.showinfo("Warning!", "website / username / password must not be empty")

def saving():
  website = web_input.get()
  username = userN_input.get()
  password = pass_input.get()

  with open("C:/Users/Josh/Documents/Python Practice/CodingPractice/100Days/Day29/password.txt", "a") as file:
    if website != "" and username != "" and password != "":
      file.write(f"Website: {website} | Username: {username} | Password: {password} \n")
      file.close()
      web_input.delete(0, END)
      pass_input.delete(0, END)
    else: 
      showPopUp()

def passwordCreator():
  password = ""
  keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
  length = random.choice([15, 16, 18])
  for i in range(length):
    new_password = random.choice(keys)
    password += new_password
  pass_input.delete(0, END)
  pass_input.insert(0, password)



output_label = Label(text="")
output_label.pack(side=BOTTOM)

website_label = Label(text="Website: ")
website_label.pack()

web_input = Entry(width= 30)
web_input.pack()

user_label = Label(text="Email/Username: ")
user_label.pack()

userN_input = Entry(width= 30)
userN_input.pack()

pass_label = Label(text="Password: ")
pass_label.pack()

pass_input = Entry(width= 30)
pass_input.pack()

add_button = Button(text="Add", command=saving)
add_button.pack()

generate_pass = Button(text="Generate Custom Pass", command=passwordCreator)
generate_pass.pack()



window.mainloop()