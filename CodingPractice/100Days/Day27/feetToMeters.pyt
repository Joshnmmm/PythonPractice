from tkinter import *


window = Tk()
window.title("Feet To Meter Converter")
window.minsize(width=300, height= 150)



def convert():
  digit = float(user_input.get())
  meters = digit / 3.281
  result_label.config(text=f"{meters:.2f} meters")


user_input = Entry()
user_input.pack()

enter_button = Button(text="Enter", command=convert)  
enter_button.pack()

result_label = Label(text="")
result_label.pack()

window.mainloop()