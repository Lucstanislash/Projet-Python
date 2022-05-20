from tkinter import *

fenetre=Tk()
fenetre.config(background='lightskyblue1')
OptionsExo1 = [
"base 2",
"base 8",
"base 10",
"base 16"
]

cadre1=Frame(fenetre, bg='lightskyblue1') # création d'un premier cadre
cadre2=Frame(fenetre, bg='lightskyblue1')
cadre3=Frame(fenetre, bg='lightskyblue1')

titre=Label(cadre1, text="Entiers non signées", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.pack(pady= 10, expand=YES) # Placement de l'invite
soustitre=Label(cadre1, text="Quelques Indications: ", font=("courier", 25), fg='red', bg='lightskyblue1') 
soustitre.pack(pady= 10, side=LEFT) 

#Saisie de valeur 1
txt1=Label(cadre2, text="Nombre Binaire 1", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt1.place(x=100, y=100)
saisieVal=Entry(cadre2) 
saisieVal.place(x=700, y=100, width=500, height=48)

val=StringVar() # variable qui récupérera la valeur de la case à cocher
txt2=Label(cadre2, text="Choix d'opération", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt2.place(x=100, y=160)
# Les trois boutons radio correspondant aux trois choix - La variable contenant la valeur
# est val. Les valeurs sont respectivement '+', '-' ou 'x'
choixA=Radiobutton(cadre2, text="Addition  (+)", variable=val, value="+")
choixA.place(x= 700, y= 160)
choixB=Radiobutton(cadre2, text="Soustraction (-)", variable=val, value="-")
choixB.place(x= 700, y= 180)
choixC=Radiobutton(cadre2, text="Multiplication (x)", variable=val, value="x")
choixC.place(x= 700, y= 200)

# Saisie de valeur 2
txt3=Label(cadre2, text="Nombre binaire 2", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt3.place(x= 100, y= 260)
saisieVal=Entry(cadre2) 
saisieVal.place(x=700, y=260, width=500, height=48) # Placement de la zone de saisie


txt4=Label(cadre2, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt4.place(x=100, y= 320)
Résultats=Entry(cadre2) #width= largeur, height= hauteur) # Création de la zone de résultats
Résultats.place(x=700, y=320, width=500, height=48)

B1=Button(cadre3, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='red', bg='#103985', width=20, height=2)
B1.grid(row=0, column=0, pady=10, padx=10)
B2=Button(cadre3, text="Nouveau", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2)
B2.grid(row=0, column=1, pady=10, padx=10)
B3=Button(cadre3, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2)
B3.grid(row=0, column=2, pady=10, padx=10)
B4=Button(cadre3, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2)
B4.grid(row=0, column=3, pady=10, padx=10)
B5=Button(cadre3, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=20, height=2)
B5.grid(row=0, column=4, pady=10, padx=10)  

cadre1.pack(fill=BOTH)
cadre2.pack(fill=BOTH, expand=1)
cadre3.pack(fill=BOTH)
fenetre.mainloop
