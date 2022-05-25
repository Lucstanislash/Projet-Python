from Outils import *
from functools import partial
from tkinter import *


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
        print("erreur de saisie")

    ent2=CtrlSyntaxe(e2,16,1,16)
    if ent2 == True:
        b = e2
    else:
        print("erreur de saisie")
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
        B3.destroy() #bloquer le bouton valider ==> Gagner
        #resu=Label(cadre1, text="Bonne Réponse, Bravo !! ", font=("courier", 25, "italic"), fg='green', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        #resu.pack(pady= 10, side=TOP)
    elif rep == -1:
        
        B3.destroy() #bloquer le bouton valider ==> Perdu
        #resu=Label(cadre1, text="Mauvaise réponse, vous avez perdu ! Le résultat est : ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        #resu.pack(pady= 10, side=TOP)
    elif rep == 0:
        B3.destroy()
        #resu=Label(cadre1, text="Mauvaise réponse, réessayer ! ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        #resu.pack(pady= 10, side=TOP)
    

    
#===========================================================
#========= Fonction de l'exo ===============================
#===========================================================



def Exercice2(saisie, fenetre, cadre5):
    f = fenetre
    f.rowconfigure(1, weight=0)
    f.rowconfigure(2, weight=0)
    f.rowconfigure(3, weight=1)
    f.rowconfigure(4, weight=1)
    f.rowconfigure(5, weight=1)
    f.rowconfigure(6, weight=1)
    f.rowconfigure(7, weight=1)

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
        resu.destroy()
        
    largeur = 25
    hauteur = 2
    
    tExo2 = Label(f, text= "Opérations en binaire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    tExo2.grid(row=1, column = 2, columnspan=3)
    #tExo2.pack(fill=BOTH, pady= 10, expand=YES)
                    
    st=Label(f, text="Quelques Indications: ", font=("courier", 25, "italic"), fg='white', bg='#103985') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    st.grid(row=2, column = 1, columnspan=3)
    #st.pack(fill=BOTH, pady= 10, side=LEFT, expand=NO)
        
    txt1=Label(f, text="Nombre Binaire 1 : ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt1.grid(row=3, column = 1, columnspan=3)
    #txt1.place(x=100, y=100)
    #txt1.pack(fill=BOTH, expand=1)
    saisieB1=Entry(f)
    saisieB1.grid(row=3, column = 2, columnspan=3)
    #saisieB1.place(x=700, y=100, width=500, height=48)
    #saisieB1.pack(fill=BOTH, expand=1)
    
    txt2=Label(f, text="Choix d'opération (+,- ou x) :", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt2.grid(row=4, column = 1, columnspan=3)
    #txt2.place(x=100, y=160)
    #txt2.pack(fill=BOTH, expand=1)
    saisieOper=Entry(f)
    saisieOper.grid(row=4, column = 2, columnspan=3)
    #saisieOper.place(x=700, y=150, width=500, height=48)
    #saisieOper.pack(fill=BOTH, expand=1)

    txt3=Label(f, text="Nombre binaire 2 : ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt3.grid(row=5, column = 1, columnspan=3)
    #txt3.place(x= 100, y= 260)
    #txt3.pack(fill=BOTH, expand=1)
    saisieB2=Entry(f)
    saisieB2.grid(row=5, column = 2, columnspan=3)
    #saisieB2.place(x=700, y=260, width=500, height=48)
    #saisieB2.pack(fill=BOTH, expand=1)

    txt4=Label(f, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt4.grid(row=6, column = 1, columnspan=3)
    #txt4.place(x=100, y= 320)
    #txt4.pack(fill=BOTH, expand=1)
    saisieRep=Entry(f)
    saisieRep.grid(row=6, column = 2, columnspan=3)
    #width= largeur, height= hauteur) # Création de la zone de résultats
    #saisieRep.place(x=700, y=320, width=500, height=48)
    #saisieRep.pack(fill=BOTH, expand=1)

    if saisie == 1:
        sa=AleaValeur()
    else:
        sa=[]
        
    w=20
    h=2

    B1=Button(f, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='red', bg='#103985', width=w, height=h)
    B1.grid(row=7, column=1, pady=10, padx=10)
    B2=Button(f, text="Nouveau", font=("courier", 18, "italic"), fg='white', bg='#103985', width=w, height=h, command=partial(Nouveau,saisie))
    B2.grid(row=7, column=2, pady=10, padx=10)
    B3=Button(f, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=w, height=h, command=partial(Valide,saisie, sa))
    B3.grid(row=7, column=3, pady=10, padx=10)
    B4=Button(f, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=w, height=h)
    B4.grid(row=7, column=4, pady=10, padx=10)
    B5=Button(f, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=w, height=h, command=back)
    B5.grid(row=7, column=5, pady=10, padx=10)

#===========================================================
#========= Reset de l'exo ==================================
#===========================================================

def Nouveau(saisie):
    tExo2.destroy()
    st.destroy()
    resu.destroy()
    Exercice2(saisie)
    #effacer ce qui a été entré

##ca1.pack(fill=BOTH)
##ca2.pack(fill=BOTH, expand=1)
##ca3.pack(fill=BOTH)
        
