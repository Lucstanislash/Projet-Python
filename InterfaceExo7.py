from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
from Exo7 import*


fenetre=tk.Tk()
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
man=1
formats=""
if man ==1 :
    alea=SaisieAllEx7()
    formats=alea[1]
    valeur=alea[0]
    
def get(formats):
    if man==2:
        entier = saisieVal.get()
        util = Resultats.get()
        formats = fenetre.option_var.get()
    else:
        entier=valeur
        util = Resultats.get()
    print(entier)
    print(util)
    print(formats)
    if formats=="IEEE":
        rep=Ent_IEEE(entier)

    else:
        rep=IEE_Ent(entier)
    
    Verif=VerifRep(rep,util)
    
    if Verif == 1:
        B3['state']='disabled' #bloquer le bouton valider ==> Gagner
        resu=Label(fenetre, text="Bonne Réponse, Bravo !! ", font=("courier", 25, "italic"), fg='green', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    elif Verif == -1:
        B3['state']='disabled' #bloquer le bouton valider ==> Perdu
        B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
        resu=Label(fenetre, text="Vous avez perdu ! Le résultat est :", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1')
    elif Verif == 0:
        resu=Label(fenetre, text="Mauvaise réponse, réessayer ! ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    resu.grid(row=5,column=1,columnspan=4,sticky='s')


OptionsExo1 = ("IEEE","entier")


titre=Label(fenetre, text="Les réels", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')  # Placement de l'invite

soustitre=Label(fenetre, text="Quelques Indications: ", font=("courier", 25), fg='darkblue', bg='lightskyblue1') 



txt1=Label(fenetre, text="Réel à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
if man==2:
    
    saisieVal=Entry(fenetre) 
    val=StringVar(fenetre) # variable qui récupérera la valeur de la case à cocher

else:
    saisieVal=Label(fenetre, text=valeur, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)



txt2=Label(fenetre, text="Convertir au format", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
if man==2:
   
    fenetre.option_var= tk.StringVar(fenetre)
    w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo1[0], *OptionsExo1)
else:
    w1=Label(fenetre, text=formats, font=("courier", 15, "italic"), fg='black', bg='white',width=4, height=1)



txt3=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')

Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats


def create():
    rappel = Toplevel(fenetre)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')

    txt1=Label(rappel, text="1 bit de signe", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="8 bits d’exposant biaisé (biaisé de 127)", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt3=Label(rappel, text="23 bits de mantisse", font=("courier", 25, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
    txt4=Label(rappel, text="Ne pas oublier le bit implicite", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

    txt1.grid(row=2, column=3)
    txt2.grid(row=3, column=3)
    txt3.grid(row=4, column=3)
    txt4.grid(row=5, column=3)

    rappel.rowconfigure(1, weight=1)
    rappel.rowconfigure(2, weight=1)
    rappel.rowconfigure(3, weight=1)
    rappel.rowconfigure(4, weight=1)
    rappel.rowconfigure(5, weight=1)
    rappel.rowconfigure(6, weight=1)

    rappel.columnconfigure(1, weight=0)
    rappel.columnconfigure(2, weight=1)
    rappel.columnconfigure(3, weight=1)
    rappel.columnconfigure(4, weight=1)
    rappel.columnconfigure(5, weight=0)    

    def exit_btn():

        rappel.destroy()
        rappel.update()

    btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
    btn.grid(row=6, column=2,columnspan=3,sticky='n')

def nouveau():
    B3['state']='normal'
    B2['state']='disabled'
    if man ==1 :
        alea=SaisieAllEx7()
        formats=alea[1]
        valeur=alea[0]
        saisieVal.config(text=valeur)
        w1.config(text=formats)
        
B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2)

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(formats))
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2)

titre.grid(row=1, column=2,columnspan=3)
soustitre.grid(row=2, column=1,columnspan=3,sticky='w',ipady=40)
txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=40)
saisieVal.grid(row=3, column=2,ipadx=200,columnspan=4,ipady=10)

txt2.grid(row=4, column=1,columnspan=2,sticky='w')
txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=40)
w1.grid(row=4, column=2,ipadx=235,columnspan=4,ipady=10)
Resultats.grid(row=5, column=2,ipadx=200,columnspan=4,ipady=10)



#bouton#
B1.grid(row=6, column=1)
B2.grid(row=6, column=2)
B3.grid(row=6, column=3)
B4.grid(row=6, column=4)
B5.grid(row=6, column=5)

fenetre.mainloop()
