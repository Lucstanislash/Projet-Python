from tkinter import *
import tkinter as tk   #pour le menu déroulant
from tkinter import ttk  #pour le menu déroulant


fenetre=Tk()
fenetre.config(background="lightskyblue1")


fenetre.rowconfigure(1, weight=0)
fenetre.rowconfigure(2, weight=0)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=1)

fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=1)


OptionsExo1 = ("IEEE","entier")


titre=Label(fenetre, text="Les réels", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')  # Placement de l'invite

soustitre=Label(fenetre, text="Quelques Indications: ", font=("courier", 25), fg='darkblue', bg='lightskyblue1') 



txt1=Label(fenetre, text="Réel à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
saisieVal=Entry(fenetre) 
val=StringVar(fenetre) # variable qui récupérera la valeur de la case à cocher


txt2=Label(fenetre, text="Convertir au format", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
fenetre.option_var = tk.StringVar(fenetre)
val.set(OptionsExo1[0]) # default value
w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo1[0], *OptionsExo1)


txt3=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')

Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats



B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2)

B2=Button(fenetre, text="Nouveau", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2)

titre.grid(row=1, column=2,columnspan=3)
soustitre.grid(row=2, column=1,columnspan=3,sticky='w',ipady=40)
txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=40)

saisieVal.grid(row=3, column=2,ipadx=200,columnspan=4,ipady=10)

txt2.grid(row=4, column=1,columnspan=2,sticky='w')

w1.grid(row=4, column=2,ipadx=235,columnspan=4,ipady=10)

txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=40)

Resultats.grid(row=5, column=2,ipadx=200,columnspan=4,ipady=10)



#bouton#
B1.grid(row=6, column=1)
B2.grid(row=6, column=2)
B3.grid(row=6, column=3)
B4.grid(row=6, column=4)
B5.grid(row=6, column=5)

fenetre.mainloop()
