from tkinter import *
from Outils import*
from Exo7 import*
fenetre=Tk()
fenetre.config(background='lightskyblue1')
#def from_to():
##    p=saisie1.get()
##    j=saisie2.get()
##    q=saisie2.get()
##    #n=(float(p)+float(q))/2
##    val3.delete(0, END) # pour vider la fenêtre du début jusqu'à la fin
##    val3.insert(0, n) # insertion de n en début de zone d'affichage

def get():
    entier = saisieVal.get()
    util = Résultats.get()
    formats = BaseEntrée.get()
    if formats=="IEEE":
        rep=Ent_IEEE(entier)

    else:
        rep=IEE_Ent(entier)

    Verif=VerifRep(rep,util)
    
    if Verif == 1:
        B3.destroy() #bloquer le bouton valider ==> Gagner
        resu=Label(cadre1, text="Bonne Réponse, Bravo !! ", font=("courier", 25, "italic"), fg='green', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    elif Verif == -1:
        B3.destroy() #bloquer le bouton valider ==> Perdu
        resu.pack_forget()
        resu=Label(cadre1, text="Vous avez perdu ! Le résultat est : ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    elif Verif == 0:
        resu=Label(cadre1, text="Mauvaise réponse, réessayer ! ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    resu.pack(pady= 10, side=TOP)
    

OptionsExo1 = [
"IEEE",
"Entier"
]

cadre1=Frame(fenetre, bg='lightskyblue1') # création d'un premier cadre
cadre2=Frame(fenetre, bg='lightskyblue1')
cadre3=Frame(fenetre, bg='lightskyblue1')

titre=Label(cadre1, text="Les réels", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.pack(pady= 10, expand=YES) # Placement de l'invite
soustitre=Label(cadre1, text="Quelques Indications: ", font=("courier", 25), fg='red', bg='lightskyblue1') 
soustitre.pack(pady= 10, side=LEFT) 

#Création de menu déroulant d'entrée
txt1=Label(cadre2, text="Réel à convertir:", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt1.place(x=75, y=100)

BaseEntrée = StringVar(cadre2) # width= largeur, height= hauteur) 
BaseEntrée.set(OptionsExo1[0]) # default value
w1 = OptionMenu(cadre2, BaseEntrée, *OptionsExo1)
w1.pack(pady= 10, expand=YES)

# Création de la zone de saisie
txt2=Label(cadre2, text="Convertir au format:", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt2.place(x= 75, y= 200)
saisieVal=Entry(cadre2) 
saisieVal.place(x=800, y=100, width=500, height=48) # Placement de la zone de saisie

txt4=Label(cadre2, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt4.place(x=75, y= 400)
Résultats=Entry(cadre2) #width= largeur, height= hauteur) # Création de la zone de résultats
Résultats.place(x=800, y=400, width=500, height=48)

B1=Button(cadre3, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='red', bg='#103985', width=20, height=2)
B1.grid(row=0, column=0, pady=10, padx=10)
B2=Button(cadre3, text="Nouveau", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2)
B2.grid(row=0, column=1, pady=10, padx=10)
B3=Button(cadre3, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2, command= get)
B3.grid(row=0, column=2, pady=10, padx=10)
B4=Button(cadre3, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2, relief="solid")
B4.grid(row=0, column=3, pady=10, padx=10)
B5=Button(cadre3, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=20, height=2)
B5.grid(row=0, column=4, pady=10, padx=10)  

cadre1.pack(fill=BOTH)
cadre2.pack(fill=BOTH, expand=1)
cadre3.pack(fill=BOTH)
fenetre.mainloop

### Même chose pour la seconde note
##cadre2=Frame(fen)
##message2=Label(cadre2, text="Note2")
##message2.pack(side='left')
##saisie2=Entry(cadre2)
##saisie2.pack(side='right')
##cadre2.pack()
##
##cadre3=Frame(fen) # troisième cadre
##message3=Label(cadre3, text="Moyenne") # Annonce du résultat
##message3.pack(side='left') # Placement de l'annonce
##val3=Entry(cadre3) # Création de la zone d'affichage
##val3.pack(side="right") # Placement de la zone d'affichage
##cadre3.pack() # Placement du cadre
##
### Bouton de lancement du calcul de la moyenne
##bmo=Button(fen, text="calcul moyenne", command=moy) 
##bmo.pack()
##fen.mainloop()
##
### E16 : Classe Listbox
##from tkinter import*
##fen=Tk()
##
##frame1=Frame(fen)
##frame2=Frame(fen)
##frame3=Frame(fen)
##listechoix=Listbox(frame1)
##listechoix.insert(END, "Francais")
##listechoix.insert(END, "Englais")
##listechoix.insert(END, "Deutch")
##listechoix.insert(END, "Hispanica") # END indique que l'insertion se fait en fin de liste
##listechoix.pack()





### convertisseur Euros/Dollars
##import tkinter as tk 
##
##def conversion():
##    print(entry.get())
##    text= entry.get()
##    label['text'] = text
##    
##    
##root = tk.Tk()
##root.title("Convertisseur") 
##root.geometry("140x130")
##frame = tk.Frame(root)
##frame.pack(fill=tk.BOTH, expand=1)
##
##entry = tk.Entry(frame, text="")
##entry.place(x=500, y=400, width=120, height=30)
##bouton = tk.Button(frame, text="Conversion", command=conversion)
##bouton.place(x=10, y=50, width=120, height=30)
##label = tk.Label(frame, text="Salut", fg="blue", bg="yellow")
##label.place(x=10, y=90, width=120, height=30)
##
##
##root.mainloop()


