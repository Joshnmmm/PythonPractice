import tkinter 

window = tkinter.Tk() #main opening
window.title("This is my first GUI NICE")
window.minsize(width=500, height=300) #panel sizing


#Label 


var_label = tkinter.Label(text="This is a label", font=("Arial", 24, "italic"))
var_label.pack(side="bottom") # this place it in the screen + center it








window.mainloop() #main closing

#lesson1 end
#lesson 2 all abt positional arguments 
#lesson 2 summary:
'''
def add(*args):  #this can accept any amount of arguments (this is not pointers)
  for n in args:
    print(n)           # looping all arguments

'''
