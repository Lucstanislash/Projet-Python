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

man=2
#========================Calcul de la réponse selon les données==============================
def repEx4(ch,puis,oper):
    if oper=='*':
        rep=ch+'0'*puis
    elif oper=='/':
        rep=ch[:-puis]
    return (rep)

#========================ALEATOIRE MAN=2==========================================
if man==2:
    #========================Données Aléatoires==============================
  

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
    def control2(ch):
        if not CtrlSyntaxe(ch,2,1,35):
            ok=False
            messagebox.showerror("ATTENTION !", "Vérifier la saisie de votre résultat.")

    #========================================================================
    donnee=Alea4()
    op=donnee[2]
    ch=donnee[0]
    p=int(donnee[1])
    def Exo4(l4):
        global op
        global ch
        global p
        verif=2
        base=[2,10]
        rep=repEx4(ch,p,op)
        util=res.get()
        control2(util)
        verif=VerifRep(rep,util)
        if verif==0:
            res1="Réessayer"
            messagebox.showerror("showerror", "Veuillez réessayer")
            res.delete(0, END)
        elif verif==-1:
            B3['state']='disabled' #bloquer le bouton valider ==> Perdu
            res1="Réponse : \n" + rep
            messagebox.showinfo(title="Information",
                                message=" Mauvaise réponse!\n Le résultat est: \n"+rep)
            B2['state']='normal'
        else:
            res1 = "Bravo !"
            messagebox.showinfo(title="Bravo", message="Bravo! Vous pouvez conutinuer.")
            B2['state']='normal'
            B3['state']='disabled'
        l4.config(text=res1)

    
    #========= Reset de l'exo ==================================
    
    def Nouveau():
        B3['state']='normal'
        global op
        global ch
        global p
        donnee=Alea4()
        op=donnee[2]
        p=donnee[1]
        ch=donnee[0]
        nbbin.config(text=ch)
        oper.config(text=op)
        puis.config(text=p)
        res.delete(0,END)
        B2['state']='disabled'
            
    #====================================cadre1=================x 
    
    txt1=Label(fenetre, text="Type d'opération", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    oper=Label(fenetre, text=donnee[2], font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)

    txt2=Label(fenetre, text="Nombre Binaire ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    nbbin=Label(fenetre, text=donnee[0], font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)

    txt3=Label(fenetre, text="Puissance en base de 2 ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    puis=Label(fenetre, text=donnee[1], font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)
    txt4=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    res=Entry(fenetre) 

#==============================================================================================================
#=====================================Manuel===================================================================
#==============================================================================================================

else:
    
    #========================Saisie Manuelle==============================
   
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
        verif=VerifRep(rep,util)
        if verif==0:
            messagebox.showerror("showerror", "Veuillez réessayer")
            res.delete(0, END)
        elif verif==-1:
            B3['state']='disabled' #bloquer le bouton valider ==> Perdu
            res1="Réponse : \n" + rep
            messagebox.showinfo(title="Information",
                                message=" Mauvaise réponse!\n Le résultat est: \n"+rep)
            B2['state']='normal'
        else:
            res1 = "Bravo !"
            messagebox.showinfo(title="Bravo", message="Bravo! Vous pouvez conutinuer.")
            B3['state']='disabled'
            B2['state']='normal'
        l4.config(text=res1)
    
    #========= Reset de l'exo ==================================

    def Nouveau(): #pour la saisie manuel
        B3['state']='normal'
        B2['state']='disabled'
        oper.delete(0,END)
        res.delete(0,END)
        nbbin.delete(0,END)
        puis.delete(0,END)   
    
    #===================================cadre2
    #puissance
    txt1=Label(fenetre, text="Type d'opération", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    oper=Entry(fenetre) 

    txt2=Label(fenetre, text="Nombre Binaire ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    nbbin=Entry(fenetre) 

    txt3=Label(fenetre, text="Puissance en base de 2 ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    puis=Entry(fenetre) 

    txt4=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    res=Entry(fenetre) 
#===========================================================
#========= Contrôl =========================================
#===========================================================
def control(oper,nbbin,puis):
    ok=True
    op=['*','/']
    if oper not in op:
        ok=False
        messagebox.showerror("ATTENTION !", "Operation : Mettre '*' ou '/'")
    if not CtrlSyntaxe(nbbin,2,1,16):
        ok=False
        messagebox.showerror("ATTENTION !", "Mauvaise saisie du nombre binaire")
    if not CtrlSyntaxe(puis,10,1,10,1,8):
        ok=False
        messagebox.showerror("ATTENTION !", "Mauvaise saisie de l'exposant")

#===========================================================
#========= Rappel fenetre ==================================
#===========================================================
def create():
    rappel = Toplevel(fenetre)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')

    txt1=Label(rappel, text="Multiplication :", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="Ajouter des 0 à la fin \n du nombre en base 2 donné", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt3=Label(rappel, text="Division : ", font=("courier", 25, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
    txt4=Label(rappel, text="Supprimer des 0 à la fin \n du nombre en base 2  donné", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

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

     
#======================Cadre 3=================================================
titre=Label(fenetre, text="Opération sans calcul", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.grid(row=1, column=2,columnspan=3) # Placement de l'invite
l4 = Label(fenetre,
               text = "",
               font = "normal 20 bold",
               bg = 'lightskyblue1',
               width = 15
               )
l4.grid(row=2, column=3,columnspan=4,sticky='w',ipady=10)


txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=10)
oper.grid(row=3,column=2,ipadx=100,columnspan=4,ipady=10) # Placement de la zone de saisie
txt2.grid(row=4, column=1,columnspan=2,sticky='w')
nbbin.grid(row=4, column=2,ipadx=100,columnspan=4,ipady=10)
txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=10)
puis.grid(row=5, column=2,ipadx=100,columnspan=4,ipady=10)
txt4.grid(row=6,column=1,columnspan=2,sticky='w',ipady=10)
res.grid(row=6, column=2,ipadx=100,columnspan=4,ipady=10)

    
B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())
B2=Button(fenetre, text="Nouveau",font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Nouveau())
B3=Button(fenetre, text="Valider",command=partial(Exo4, l4), font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, relief="solid")
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=15, height=2)
 

B1.grid(row=7, column=1)
B2.grid(row=7, column=2)
B3.grid(row=7, column=3)
B4.grid(row=7, column=4)
B5.grid(row=7, column=5)
fenetre.mainloop()
