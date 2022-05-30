from tkinter import *
from random import*
import math
from tkinter import messagebox
from functools import partial
from Outils import*
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


my_scrollbar = Scrollbar(fenetre, orient= VERTICAL) #pour pouvoir se déplacer verticallement

#============================================================================================
#========================Calcul de la réponse selon les données==============================
#============================================================================================
def repEx4(ch,puis,oper):
    if oper=='*':
        rep=ch+'0'*puis
    elif oper=='/':
        rep=ch[:-puis]
    return (rep)
#===========================================================
#========= Contrôl =========================================
#===========================================================
def control(oper,nbbin,puis):
    ok=True
    op=['*','/']
    if oper not in op:
        ok=False
        messagebox.showerror("showerror", "Operation : Mettre '*' ou '/'")
    if not CtrlSyntaxe(nbbin,2,1,16):
        ok=False
        messagebox.showerror("showerror", "Mauvaise saisie du nombre binaire")
    if not CtrlSyntaxe(puis,1,2,1,8):
        ok=False
        messagebox.showerror("showerror", "Mauvaise saisie de l'exposant")
#=====================================================================
#========================Saisie Manuelle==============================
#=====================================================================
def Exo4(l4):
    op=oper.get()
    ch=nbbin.get()
    Raccourcir(ch)
    p=(puis.get())
    control(op,ch,p)
    p=int(puis.get())
    verif=2
    base=[2,10]
    rep=repEx4(ch,p,op)
    util=res.get()
    Raccourcir(res)
    verif=VerifRep(rep,util)
    if verif==0:
        res1="Reessayez"
        res.delete(0, END)
    elif verif==-1:
        res1=rep
    else:
        res1 = "Bravo !"
    l4.config(text=res1)
    
#===========================================================
#========= Reset de l'exo ==================================
#===========================================================

def Nouveau(saisie):
    resu.destroy()
    Valide(saisie)
    
#====================================cadre1
titre=Label(fenetre, text="Opération sans calcul", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.grid(row=1, column=2,columnspan=3)
#soustitre=Label(cadre1, text="Quelques Indications: ", font=("courier", 18), fg='red', bg='lightskyblue1') 
#soustitre.pack(pady= 10, side=LEFT) 
l4 = Label(fenetre,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.grid(row=2, column=2,columnspan=4,sticky='w',ipady=10)
#===================================cadre2
#puissance
txt1=Label(fenetre, text="Type d'opération", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=10)
oper=Entry(fenetre) 
oper.grid(row=3,column=2,ipadx=100,columnspan=4,ipady=10) # Placement de la zone de saisie


txt2=Label(fenetre, text="Nombre Binaire ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt2.grid(row=4, column=1,columnspan=2,sticky='w')
nbbin=Entry(fenetre) 
nbbin.grid(row=4, column=2,ipadx=100,columnspan=4,ipady=10)

txt3=Label(fenetre, text="Puissance en base de 2 ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=10)
puis=Entry(fenetre) 
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

fenetre.mainloop
