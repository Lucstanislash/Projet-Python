from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox
from Exo8 import *

fenetre=tk.Tk()
fenetre.config(background="lightskyblue1")

fenetre.rowconfigure(1, weight=0)
fenetre.rowconfigure(2, weight=2)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=1)
fenetre.rowconfigure(7, weight=1)
fenetre.rowconfigure(8, weight=1)
fenetre.rowconfigure(9, weight=1)

fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=1)

man=2
donne=""
util=[]
if man ==1 :
    TailleTab=AleaExAll(10,30,300)
    TailleCase=AleaExAll(10,1,30)
    AdTab=AleaExAll(10,1,1000)
    donne2=AleaExAll(10,1,donne[1])
    donne=(TailleTab,TailleCase,Ad1mot)

def control():
    TailleTab = TailleTab.get()
    TailleCase = TailleCase.get()
    AdPMTab = AdPMTab.get()
    if TailleTab*TailleCase<950:
        a=CtrlSyntaxe(str(TailleTab),10,1,10,30,300)
        if ok==False:
            return(1)
    else:
        return(1)
    return(TailleTab,TailleCase,Ad1mot)

def get(donne):
    if man==2:
        donne=control()
        if donne==1:
            return(1)
    util.append = NbCTab.get()
    util.append = NumPTab.get()
    util.append = NumDTab.get()

    rep=RepEx8(donne)
    rep2=donne[2]+(donne2-1)*donne[1]
    Verif=VerifRep(rep,util)
    
    if Verif == 1:
        B3['state']='disabled' #bloquer le bouton valider ==> Gagner
        B2['state']='normal'
        messagebox.showinfo(title="Information",
                            message="Bonne Réponse, Bravo !! ")
    elif Verif == -1:
        B3['state']='disabled' #bloquer le bouton valider ==> Perdu
        B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
        messagebox.showinfo(title="Information",
                            message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("".join(rep)))
    elif Verif == 0:
       messagebox.showinfo(title="Information",
                            message="Mauvaise réponse, réessayer !")
       
## INTERFACE ##########################

       
titre=Label(fenetre, text="Les Tableaux", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  # Placement de l'invite

soustitre=Label(fenetre, text="Quelques Indications:  ", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

txt1=Label(fenetre, text="Taille du tableau", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
txt1a=Label(fenetre, text="(en nombre de case)", font=("courier", 12, "italic"), fg='black', bg='lightskyblue1')

txt2=Label(fenetre, text="Taille d'une case", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
txt2a=Label(fenetre, text="(en nombre de mot)", font=("courier", 12, "italic"), fg='black', bg='lightskyblue1')

txt3=Label(fenetre, text="Adresse 1 mot ", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
txt4=Label(fenetre, text="Numéro de case", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')

txtQ10=Label(fenetre, text="Nombre de mots", font=("courier", 20), fg='black', bg='lightskyblue1')
txtQu1=Label(fenetre, text="Question 1 :", font=("courier", 20, "bold"), fg='black', bg='lightskyblue1')
txtQ11=Label(fenetre, text="Numéro du premier mot", font=("courier", 20), fg='black', bg='lightskyblue1')
txtQ12=Label(fenetre, text="Numéro du dernier mot", font=("courier", 20), fg='black', bg='lightskyblue1')

txtQ2=Label(fenetre, text="Mot contenus dans la case", font=("courier", 20), fg='black', bg='lightskyblue1')
txtQu2=Label(fenetre, text="Question 2 :", font=("courier", 20, "bold"), fg='black', bg='lightskyblue1')

    
TailleTab=Entry(fenetre,justify='center',borderwidth=3)

TailleCase=Entry(fenetre,justify='center',borderwidth=3)

AdPMTab=Entry(fenetre,justify='center',borderwidth=3)


NumCase=Entry(fenetre,justify='center',borderwidth=3)



NbCTab=Entry(fenetre,justify='center')

NumPTab=Entry(fenetre,justify='center') 
NumDTab=Entry(fenetre,justify='center')

MotCase=Entry(fenetre,justify='center') 


def create():
    rappel = Toplevel(fenetre)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='darkblue', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')

    txt1=Label(rappel, text="1 bit de signe", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="8 bits d’exposant biaisé (biaisé de 127)", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt3=Label(rappel, text="23 bits de mantisse", font=("courier", 20, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
    txt4=Label(rappel, text="Ne pas oublier le bit implicite", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

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

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(formats))
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,state='disabled')
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fenetre.destroy)

B6=Button(fenetre, text="Go!", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=16, height=0)

titre.grid(row=1, column=2,columnspan=3)
soustitre.grid(row=2, column=1,columnspan=5,sticky='w')

txt1.grid(row=3, column=1,columnspan=2,sticky='w')
TailleTab.grid(row=3, column=2,ipady=10)

txt1a.grid(row=3, column=1,sticky='s')

txt2.grid(row=3, column=3,columnspan=4,sticky='w')
TailleCase.grid(row=3,column=4,ipady=10)

txt2a.grid(row=3, column=3,sticky='s')

B6.grid(row=4, column=5,sticky='nw')

txt3.grid(row=4, column=1,columnspan=2,sticky='w',ipady=30)
AdPMTab.grid(row=4, column=2,ipady=10)

txt4.grid(row=4,column=3,columnspan=4,sticky='w',ipady=30)
NumCase.grid(row=4, column=4,ipady=10)

txtQ10.grid(row=5, column=2,columnspan=3,sticky='w')
NbCTab.grid(row=5, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

txtQu1.grid(row=5, column=1,sticky='w')

txtQ11.grid(row=6, column=2,columnspan=3,sticky='w')
NumPTab.grid(row=6, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

txtQ12.grid(row=7, column=2,columnspan=3,sticky='w')
NumDTab.grid(row=7, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')


txtQ2.grid(row=8, column=2,columnspan=3,sticky='w')
MotCase.grid(row=8,column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

txtQu2.grid(row=8, column=1,sticky='w')



#bouton#
B1.grid(row=9, column=1)
B2.grid(row=9, column=2)
B3.grid(row=9, column=3)
B4.grid(row=9, column=4)
B5.grid(row=9, column=5)

fenetre.mainloop()
