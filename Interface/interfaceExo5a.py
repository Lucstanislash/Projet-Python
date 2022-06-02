from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox



lis=["SVA","C2"]

def  AleaFormat5(lis):
        """Sort aléatoirement une valeur entre 1 et 2 pour choisir la base dans la liste li"""
        i=randrange(0,2)
        formats=lis[i]
        return(formats)

def AleaEnt5():
        """Génère aléatoirement un entier en base 2, entre 8 et 16 bits"""
        ent=AleaExAll(2,8,16)
        return(ent)

def RepExA5(entier):
        """permet de généré la réponse , signe positif ou négatif"""
        signe=list(entier)

        if signe[0]=='0' :
                
                rep="positif"# positif

        else:
                rep="negatif"# négatif
        
        return(rep)

fenetre=tk.Tk()
fenetre.config(background="lightskyblue1")
##fenetre.attributes('-fullscreen', True)

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

formats=AleaFormat5(lis)
entier=AleaEnt5()


titre=Label(fenetre, text="Déterminer le signe d'un entier", font=("Courier", 30, "italic"), fg='black', bg='lightskyblue1')  # Placement de l'invite

soustitre=Label(fenetre, text="Quelques Indications:  ", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

txt1=Label(fenetre, text="Formats", font=("courier", 30, "italic"), fg='black', bg='lightskyblue1')

formatsAl=Label(fenetre, text=formats, font=("courier", 20, "italic"), fg='black', bg='white',width=10, height=1)


txt2=Label(fenetre, text="Valeur", font=("courier", 30, "italic"), fg='black', bg='lightskyblue1')

val=Label(fenetre, text=entier, font=("courier", 20, "italic"), fg='black', bg='white',width=4, height=1)

choix=StringVar()

signe=Label(fenetre, text="Signe de\nl'entier", font=("courier", 30, "italic"), fg='black', bg='lightskyblue1')
positif=Radiobutton(fenetre, text="Positif",font=("courier", 25), variable=choix, value="positif",fg='black', bg='lightskyblue1',activebackground="lightskyblue1",width=30,)
negatif=Radiobutton(fenetre, text="Négatif", font=("courier",25),variable=choix, value="negatif",fg='black', bg='lightskyblue1',activebackground="lightskyblue1")

def nouveau():
    
    formats=AleaFormat5(lis)
    entier=AleaEnt5()
    B3['state']='normal'
    B2['state']='disabled'
    formatsAl.config(text=formats)
    val.config(text=entier)
 
def RepUtil():
    
        ch=choix.get() # on récupère la valeur de val, donc de la case sélectionnée
        if ch=="positif":
            util="positif"
        elif ch=="negatif":
            util="negatif"

        
        rep=RepExA5(val["text"])
        
        Verif=VerifRep(rep,util)
        
        B3['state']='disabled'
        B2['state']='normal'
        if Verif == 1:
            B3['state']='disabled' #bloquer le bouton valider ==> Gagner
            B2['state']='normal'
            messagebox.showinfo(title="Information",
                            message="Bonne Réponse, Bravo !! ")
        elif Verif == 0:
            B3['state']='disabled' #bloquer le bouton valider ==> Perdu
            B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
            messagebox.showinfo(title="Information",
                            message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("".join(rep)))

def create():
    rappel = Toplevel(fenetre)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')

    txt1=Label(rappel, text="L’entier ne peut pas excéder 16 bits", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="Dans cet exercice, une seule tentative ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt3=Label(rappel, text="sera accordée à l’utilisateur", font=("courier", 25, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
    txt4=Label(rappel, text="", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

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


        
B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda : RepUtil())
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,state='disabled')
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fenetre.destroy)

titre.grid(row=1, column=2,columnspan=4,sticky='w',ipady=40)
soustitre.grid(row=2, column=1,columnspan=5,sticky='w',ipady=40)

txt1.grid(row=3, column=1,ipady=40)
formatsAl.grid(row=3, column=2,ipadx=300,columnspan=4,ipady=10)

txt2.grid(row=4, column=1)
val.grid(row=4, column=2,ipadx=350,columnspan=4,ipady=10)

signe.grid(row=5, column=1,ipady=40)
positif.grid(row=5, column=2,columnspan=3,sticky='w',padx=20, pady=40)
negatif.grid(row=5, column=4,columnspan=5,sticky='w',ipadx=50)




#bouton#
B1.grid(row=6, column=1)
B2.grid(row=6, column=2)
B3.grid(row=6, column=3)
B4.grid(row=6, column=4)
B5.grid(row=6, column=5)

fenetre.mainloop()
