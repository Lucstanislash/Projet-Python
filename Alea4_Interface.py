from tkinter import *
from random import*
import math
from Outils import*
from tkinter import messagebox
from functools import partial
#-------------------
fenetre=Tk()
fenetre.config(background='lightskyblue1')
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
#========================================================================
#========================Données Aléatoires==============================
#========================================================================
def Alea4 ():
    nb=randint(0,1)     #choix de l'opération
    if (nb==1):
        oper="*"    
    else:
        oper="/"
    print("L'operation effectuer ==>",oper)
    p=randint(1,8) #choix de la puissance
    print(p)
    taille =randrange(1,17-p)
    ch='1'
    if oper=='/':
        for i in range (taille-1):
            c=randrange(0,2)
            if c==1:
                ch+='1'
            else:
                ch+='0'
        ch+='0'*p
    else:
        taille =randrange(1,17)
        for g in range (taille):
            c=randrange(0,2)
            if c==1:
                ch+='1'
            else:
                ch+='0'
    print("nombre binaire",ch)
    return ([ch, p, oper])
#===========================================================
#========= Contrôl =========================================
#===========================================================
def control(res):
    ok=True
    if not CtrlSyntaxe(nbbin,2,1,16):
        ok=False
        messagebox.showerror("showerror", "Mauvaise saisie du nombre binaire")
    
    

#========================================================================
#========================Calcul de la réponse selon les données==============================
#============================================================================================
def repEx4(ch,puis,oper):

   
    if oper=='*':
        rep=ch+'0'*puis
    elif oper=='/':
        rep=ch[:-puis]
    return (rep)
#========================================================================
def Exo4(l4):
    
    op=oper.get()
    ch=nbbin.get()
    p=int(puis.get())
    verif=2
    base=[2,10]
    rep=repEx4(ch,p,op)
    util=res.get()
    #control(util)
    verif=VerifRep(rep,util)
    if verif==0:
        messagebox.showerror("showerror", "Veuillez réessayer")
        res.delete(0, END)
    elif verif==-1:
        res1=rep
    else:
        res1 = "Bravo"
    l4.config(text=res1)

#===========================================================
#========= Reset de l'exo ==================================
#===========================================================

def Nouveau(saisie):
    resu.destroy()
    Valide(saisie)

#====================================cadre1=================x 
titre=Label(fenetre, text="Opération sans calcul", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.grid(row=1, column=2,columnspan=3) # Placement de l'invite
l4 = Label(fenetre,text = "",font = "normal 20 bold",bg='lightskyblue1',width = 15 ,borderwidth = 2,
           relief = "solid")
l4.grid(row=2, column=2,columnspan=4,sticky='w',ipady=10)
donnee=Alea4()

txt1=Label(fenetre, text="Type d'opération", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=10)
oper=Entry(fenetre)
oper.insert(END,donnee[2])
oper.grid(row=3,column=2,ipadx=100,columnspan=4,ipady=10) # Placement de la zone de saisie


txt2=Label(fenetre, text="Nombre Binaire ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt2.grid(row=4, column=1,columnspan=2,sticky='w')
nbbin=Entry(fenetre)
nbbin.insert(END,donnee[0])
nbbin.grid(row=4, column=2,ipadx=100,columnspan=4,ipady=10)

txt3=Label(fenetre, text="Puissance en base de 2 ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=10)
puis=Entry(fenetre)
puis.insert(END,donnee[1])
puis.grid(row=5, column=2,ipadx=100,columnspan=4,ipady=10)

txt4=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt4.grid(row=6,column=1,columnspan=2,sticky='w',ipady=10)
res=Entry(fenetre) 
res.grid(row=6, column=2,ipadx=100,columnspan=4,ipady=10)

#======================Cadre 3
B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='red', bg='#103985', width=15, height=2)
B2=Button(fenetre, text="Nouveau", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
B3=Button(fenetre, text="Valider",command=partial(Exo4, l4), font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, relief="solid")
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=15, height=2)
 

B1.grid(row=7, column=1)
B2.grid(row=7, column=2)
B3.grid(row=7, column=3)
B4.grid(row=7, column=4)
B5.grid(row=7, column=5)
fenetre.mainloop()
