from Outils import *
from functools import partial
from tkinter import *
from tkinter import messagebox


#========================================================================
#========================Données Aléatoires==============================
#========================================================================
def Binaire_aleaEx2():
    a = AleaExAll(2,1,16)
    b = AleaExAll(2,1,16)
    signe = randint(1,3) # pour les 3 opérateurs différents, le +, - et *
    if signe == 1:
        oper = '+'
    elif signe == 2:
        oper = '-'
    elif signe == 3:
        oper = 'x'
    return(a,b,oper)

def getEntryA():
    global util
    util = saisieRep.get()

#=====================================================================
#========================Saisie Manuelle==============================
#=====================================================================
def getEntryM():
    global Entier1
    global Entier2
    global oper
    global util
    Entier1 = saisieB1.get()
    oper = saisieOper.get()
    Entier2 = saisieB2.get()
    util = saisieRep.get()
    print(Entier1)
    print(oper)
    print(Entier2)
    print(util)
    return(Entier1, Entier2, oper, util)

def Binaire_saisEx2(e1, e2, ope):
    op = ope
    ent1=CtrlSyntaxe(e1,16,1,16)
    if ent1 == True:
        a = e1
    else:
        messagebox.showerror("showerror", "Mauvaise saisie")

    ent2=CtrlSyntaxe(e2,16,1,16)
    if ent2 == True:
        b = e2
    else:
        messagebox.showerror("showerror", "Mauvaise saisie")
    return(a,b,op)

#============================================================================================
#========================Calcul de la réponse selon les données==============================
#============================================================================================
def RepExo2 (ch1,ch2,signe):
    if signe == 'x':
      repon = (bin(int(ch1, 2) * int(ch2, 2)).replace('0b',''))
    elif signe == '+':
      repon = (bin(int(ch1, 2) + int(ch2, 2)).replace('0b',''))
    elif signe == '-':
      repon = (bin(int(ch1, 2) - int(ch2, 2)).replace('0b',''))
    return(repon)
#bin permet de faire des calcul entre chiffre binaire mais il rajoute toujours un 0b devant, donc il faut mettre ".replace('0b','')" derrière pour enlever le 0b


def AleaValeur():
    global reponse
    sa= Binaire_aleaEx2()
    saisieB1.insert(END,sa[0])
    saisieOper.insert(END,sa[2])
    saisieB2.insert(END,sa[1])
    return(sa)
    
def Valide(saisie, sa):
    global reponse
    if saisie == 1:
        getEntryA()
        reponse = RepExo2(sa[0],sa[1],sa[2])
        print(reponse)
        rep = VerifRep(reponse,util)
    elif saisie ==2:
        getEntryM()
        sa= Binaire_saisEx2(Entier1, Entier2, oper)
        reponse = RepExo2(sa[0],sa[1],sa[2])
        #========================Vérification==============================
        # (rep => réponse calculé) qui est comparé à (util => réponse de l'utilisateur)
        rep = VerifRep(reponse,util)
    global resu
    
    if rep == 1:
        B3['state']='disabled' #bloquer le bouton valider ==> Gagner
        B2['state']='normal'
        messagebox.showinfo(title="Information",
                            message="Bonne Réponse, Bravo !! ")
    elif rep == -1:
        
        B3['state']='disabled' #bloquer le bouton valider ==> Perdu
        B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
        messagebox.showinfo(title="Information",
                            message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("".join(reponse)))
        
    elif rep == 0:
        messagebox.showinfo(title="Information",
                            message="Mauvaise réponse, réessayer !")
    

    
#===========================================================
#========= Fonction de l'exo ===============================
#===========================================================



def Exercice2(saisie, fenetre):
    global f
    
    
    f = fenetre
    f.rowconfigure(1, weight=1)
    f.rowconfigure(2, weight=0)
    f.rowconfigure(3, weight=1)
    f.rowconfigure(4, weight=1)
    f.rowconfigure(5, weight=1)
    f.rowconfigure(6, weight=1)
    f.rowconfigure(7, weight=1)

    f.columnconfigure(0, weight=0)
    f.columnconfigure(1, weight=1)
    f.columnconfigure(2, weight=1)
    f.columnconfigure(3, weight=1)
    f.columnconfigure(4, weight=1)
    f.columnconfigure(5, weight=1)
    f.columnconfigure(6, weight=1)
    global saisieB1
    global saisieB2
    global saisieOper
    global saisieRep
    global B3
    global B2
    global tExo2
    global st

    def back():
        
        tExo2.destroy()
        st.destroy()
        txt1.destroy()
        txt2.destroy()
        txt3.destroy()
        txt4.destroy()
        B1.destroy()
        B2.destroy()
        B3.destroy()
        B4.destroy()
        B5.destroy()
        saisieB1.destroy()
        saisieOper.destroy()
        saisieB2.destroy()
        saisieRep.destroy()
        
        
    largeur = 25
    hauteur = 2
    
    tExo2 = Label(f, text= "Opérations en binaire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    tExo2.grid(row=1, column = 2, columnspan=3)
                    
    st=Label(f, text="Quelques Indications: Les entrées des données ne peuvent pas excéder 16 bits", font=("courier", 20, "italic"), fg='darkblue', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    st.grid(row=2, column = 1, columnspan=3, sticky='w', ipady=20)
        
    txt1=Label(f, text="Nombre Binaire 1 : ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt1.grid(row=3, column = 1, columnspan=2, sticky='w')

    saisieB1=Entry(f)
    saisieB1.grid(row=3, column = 3, columnspan=4, ipadx=200, ipady=10)
    
    txt2=Label(f, text="Choix d'opération (+,- ou x) :", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt2.grid(row=4, column = 1, columnspan=2, sticky='w')

    saisieOper=Entry(f)
    saisieOper.grid(row=4, column = 3, columnspan=4, ipadx=200, ipady=10)

    txt3=Label(f, text="Nombre binaire 2 : ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt3.grid(row=5, column = 1, columnspan=2, sticky='w')
    
    saisieB2=Entry(f)
    saisieB2.grid(row=5, column = 3, columnspan=4, ipadx=200, ipady=10)

    txt4=Label(f, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt4.grid(row=6, column = 1, columnspan=2, sticky='w')
    
    saisieRep=Entry(f)
    saisieRep.grid(row=6, column = 3, columnspan=4, ipadx=200, ipady=10)
    

    if saisie == 1:
        sa=AleaValeur()
    else:
        sa=[]
        
    w=20
    h=2
    y=3
    x=10

    B1=Button(f, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='grey', width=w, height=h, command=lambda:create(f))
    B1.grid(row=7, column=1, pady=y, padx=x)
    B2=Button(f, text="Nouveau", state='disabled', font=("bold", 18, "italic"), fg='white', bg='#103985', width=w, height=h, command=lambda:Nouveau(saisie,fenetre))
    B2.grid(row=7, column=2, pady=y, padx=x)
    B3=Button(f, text="Valider", font=("courier", 18, "bold"), fg='white', bg='#103985', width=w, height=h, command=lambda:Valide(saisie, sa))
    B3.grid(row=7, column=3, pady=y, padx=x)
    B4=Button(f, text="Score", font=("courier", 18, "bold"), fg='white', bg='#103985', width=w, height=h)
    B4.grid(row=7, column=4, pady=y, padx=x)
    B5=Button(f, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=w, height=h, command=f.destroy)
    B5.grid(row=7, column=5, pady=y, padx=x)
    

#===========================================================
#========= Reset de l'exo ==================================
#===========================================================

def Nouveau(saisie,fenetre):
    B3['state']='normal'
    B2['state']='disabled'
    tExo2.destroy()
    st.destroy()
    Exercice2(saisie,fenetre )
    #effacer ce qui a été entré

#=========================================================================
#================= Page rappel ===========================================
#=========================================================================

def create(f):
    rappel = Toplevel(f)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')

    txt1=Label(rappel, text="N'oubliez pas que : 1 + 1 = 10", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="N'oubliez pas les retenues", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    

    txt1.grid(row=2, column=3)
    txt2.grid(row=3, column=3)
    

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

    btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2)
    btn.grid(row=6, column=2,columnspan=3,sticky='n')

#=========================================================================
