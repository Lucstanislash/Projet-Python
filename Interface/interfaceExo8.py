from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox
from Exo8 import *

fenetre=tk.Tk()
fenetre.config(background="lightskyblue1")
fenetre.attributes('-fullscreen', True)

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

Raiponce={}
man=2
donne=""
donne2="Attente des valeurs"

def VerifRaip(rep,util):
    a=0
    "Compare la réponse à l’exercice (rep) avec la réponse de l’utilisateur (util)"
    if rep == util:
        a=1
    else:
        a=0
    return(a)

if man ==1 :
    taille=AleaExAll(10,30,300)
    TailleC=AleaExAll(10,1,30)
    Adresse=AleaExAll(10,1,1000)
    donne=(taille,TailleC,Adresse)

def control():
    if man==2:
        taille = TailleTab.get()
        TailleC = TailleCase.get()
        Adresse = AdPMTab.get()
        if int(taille)*int(TailleC)<950:
            ok=CtrlSyntaxe(str(taille),10,1,10,30,300)
            if ok==False:
                return(1)
        else:
            return(1)
    return(taille,TailleC,Adresse)
    
def get(donne):
    util=[]
    if man==2:
        donne=control()
        if donne==1:
            print('cpt')
            return(1)
        donne2=AleaExAll(10,1,int(donne[1]))
    util+= NbCTab.get()
    util+= NumPTab.get()
    util+= NumDTab.get()
    print(util)
    rep=RepEx8(donne)
    rep2=int(donne[2])+(int(donne2)-1)*int(donne[1])
    util2=MotCase.get()
    rep+=str(rep2)
    util+=str(util2)
    for i in range(4):
        Verif=VerifRaip(rep[i],util[i])
        Raiponce[rep[i]]=Verif
    print(Raiponce)
    print(util)
    print(rep)
    for i in Raiponce:
        print('ta mere')
        #parcourir le dico pour savoir si tout est juste ou tout faut puis renvoyer une valeur en mode je suis verif rep
        #pas oublier message derreur pour chaque rep
        
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

soustitre=Label(fenetre, text="Quelques Indications: La taille du tableau est comprise entre 30 et 300 cases \n                     Taille mot * taille case ne doit pas dépasser 950 mots ",font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

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

if man ==2:
    
    TailleTab=Entry(fenetre,justify='center',borderwidth=3)

    TailleCase=Entry(fenetre,justify='center',borderwidth=3)

    AdPMTab=Entry(fenetre,justify='center',borderwidth=3)

else:
    TailleTab=Label(fenetre, text=taille , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
    TailleCase=Label(fenetre, text=TailleC , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
    AdPMTab=Label(fenetre, text=Adresse , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)

    
NumCase=Label(fenetre, text=donne2 , font=("courier", 15, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken")


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

def nouveau():
    B3['state']='normal'
    B2['state']='disabled'
    donne2="appuyer sur Go"
    
    if man ==1 : 

       taille=AleaExAll(10,30,300)
       TailleC=AleaExAll(10,1,30)
       Adresse=AleaExAll(10,1,1000)

       TailleTab.config(text=taille)
       TailleCase.config(text=TailleC)
       AdPMTab.config(text=Adresse)
       NbCTab.delete(0,END)
       NumPTab.delete(0,END) 
       NumDTab.delete(0,END)
       MotCase.delete(0,END)
       
    else:
        
       TailleTab.delete(0,END)
       TailleCase.delete(0,END)
       AdPMTab.delete(0,END)

       
       NbCTab.delete(0,END)
       NumPTab.delete(0,END) 
       NumDTab.delete(0,END)
       MotCase.delete(0,END)
        
B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(donne))
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,state='disabled')
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fenetre.destroy)

B6=Button(fenetre, text="Go!", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=16, height=0,command=lambda:control())

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
