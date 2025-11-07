from tkinter import *
# import tkinter -> this imports class so tkinter.Tk() or tkinter.Button etc etc

window = Tk() #main opening
window.title("This is my first GUI NICE")
window.minsize(width=500, height=300) #panel sizing


#Label 

def on_click():
  new_text = input.get()
  var_label["text"] = new_text   #super straightforward, input.get gets userinput then assign it to a variable or smth nice


var_label = Label(text="This is a label", font=("Arial", 24, "italic"))
var_label.pack() # this place it in the screen + center it


var_label["text"] = "New Text"

#button 
button = Button(text ="Click Me", command=on_click)
button.pack()

#Entry  

input = Entry(width=10)
input.pack()



window.mainloop() #main closing

#lesson1 end
#lesson 2 all abt positional arguments 
#lesson 2 summary:
'''
def add(*args):  #this can accept any amount of arguments (this is not pointers)
  for n in args:
    print(n)           # looping all arguments

'''
