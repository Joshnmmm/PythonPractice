from tkinter import *

window = Tk()

window.title("Vowel Or Consonant")
window.minsize(width=200, height=100)


def vowOrCons():
  vowels = "aeiouAEIOU"
  get_input = my_input.get()
  if get_input.isalpha() == True: 
    if get_input in vowels:
      my_label["text"] = "Vowel"
    else: 
      my_label["text"] = "Consonant"
  else:
    my_label["text"] = "Please enter a correct letter"


my_label = Label(text="Vowel Or Consonant", font=("Arial",14))
my_label.pack()

my_input = Entry(width=3)
my_input.pack()

my_button = Button(text="Enter", command=vowOrCons)
my_button.pack()

window.mainloop()