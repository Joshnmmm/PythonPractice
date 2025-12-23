from tkinter import *


window = Tk()
window.title("To Do List Task")
window.minsize(width=300, height= 150)

def newTask():
  user_task = user_input.get()
  if user_task.strip() != "":
    lists.insert(END, user_task)

def deleteTask():
  selection = lists.curselection() #returns a tuple
  if selection:
    lists.delete(selection[0])     # selects the first index of that touple




lists = Listbox()
lists.pack()


input_label = Label(text="Enter Task")
input_label.pack()

user_input = Entry()
user_input.pack()

button = Button(text="Submit", command=newTask)
button.pack()

delete_button = Button(text="Task is Completed", command=deleteTask)
delete_button.pack()

window.mainloop()