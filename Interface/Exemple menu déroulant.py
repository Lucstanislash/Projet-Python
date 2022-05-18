from tkinter import *

#Ceci est un exemple de menu déroulant (exo 6)

OptionsExo6 = [
"2",
"10"
]

master = Tk()

variable = StringVar(master)
variable.set(OptionsExo6[0]) # default value
variable2 = StringVar(master)
variable2.set(OptionsExo6[0])

w1 = OptionMenu(master, variable, *OptionsExo6)
w2 =  OptionMenu(master, variable2, *OptionsExo6)
w1.pack()
w2.pack()

mainloop()
