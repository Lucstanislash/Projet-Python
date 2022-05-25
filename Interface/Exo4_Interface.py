from tkinter import *
from random import*
import math
from tkinter import messagebox
from functools import partial
from Outils import*
#-------------------

fenetre=Tk()
fenetre.geometry("1500x700")
fenetre.config(background='lightskyblue1')


cadre1=Frame(fenetre, bg='lightskyblue1') # création d'un premier cadre
cadre2=Frame(fenetre, bg='lightskyblue1')
cadre3=Frame(fenetre, bg='lightskyblue1')

my_scrollbar = Scrollbar(cadre2, orient= VERTICAL) #pour pouvoir se déplacer verticallement

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
        messagebox.showerror("showerror", "Mettre '*' ou '/'")
    if not CtrlSyntaxe(nbbin,2,1,16):
        ok=False
        messagebox.showerror("showerror", "Mauvaise saisie du nombre binaire")
    if not CtrlSyntaxe(puis,10,1,16,1,8):
        ok=False
        messagebox.showerror("showerror", "Vérifier votre puissance")
    
#=====================================================================
#========================Saisie Manuelle==============================
#=====================================================================
def Exo4(l4):
    op=oper.get()
    ch=nbbin.get()
    p=int(puis.get())
    control(op,ch,p)
    verif=2
    base=[2,10]
    rep=repEx4(ch,p,op)
    util=res.get()
    verif=VerifRep(rep,util)
    if verif==0:
        res1="reessayez"
        res.delete(0, END)
    elif verif==-1:
        res1=rep
    else:
        res1 = "Gagné"
    l4.config(text=res1)
    
#===========================================================
#========= Reset de l'exo ==================================
#===========================================================

def Nouveau(saisie):
    resu.destroy()
    Valide(saisie)
    
#====================================cadre1
titre=Label(cadre1, text="Opération sans calcul", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.pack(pady= 10, expand=YES) # Placement de l'invite
#soustitre=Label(cadre1, text="Quelques Indications: ", font=("courier", 18), fg='red', bg='lightskyblue1') 
#soustitre.pack(pady= 10, side=LEFT) 
l4 = Label(cadre1,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
#===================================cadre2
#puissance
txt1=Label(cadre2, text="Type d'opération", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt1.place(x=100, y=80)
oper=Entry(cadre2) 
oper.place(x=700, y=80, width=500, height=48) # Placement de la zone de saisie



txt2=Label(cadre2, text="Nombre Binaire ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt2.place(x=100, y=160)
nbbin=Entry(cadre2) 
nbbin.place(x=700, y=160, width=500, height=48)

txt3=Label(cadre2, text="Puissance en base de 2 ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt3.place(x=100, y=240)
puis=Entry(cadre2) 
puis.place(x=700, y=240, width=500, height=48)

txt4=Label(cadre2, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt4.place(x=100, y=320)
res=Entry(cadre2) 
res.place(x=700, y=320, width=500, height=48)
#======================Cadre 3
B1=Button(cadre3, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='red', bg='#103985', width=15, height=2)
B1.grid(row=0, column=0, pady=10, padx=10)
B2=Button(cadre3, text="Nouveau", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
B2.grid(row=0, column=1, pady=10, padx=10)
B3=Button(cadre3, text="Valider",command=partial(Exo4, l4), font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
B3.grid(row=0, column=2, pady=10, padx=10)
B4=Button(cadre3, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, relief="solid")
B4.grid(row=0, column=3, pady=10, padx=10)
B5=Button(cadre3, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=15, height=2)
B5.grid(row=0, column=4, pady=10, padx=10)  

cadre1.pack(fill=BOTH)
cadre2.pack(fill=BOTH, expand=1)
cadre3.pack(fill=BOTH)
fenetre.mainloop
