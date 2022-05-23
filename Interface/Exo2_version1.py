from Outils import *
from functools import partial
from tkinter import *

fenetre=Tk()
fenetre.geometry("1500x700")
fenetre.config(background='lightskyblue1')
cadre1=Frame(fenetre, bg='lightskyblue1')
cadre2=Frame(fenetre, bg='lightskyblue1')
cadre3=Frame(fenetre, bg='lightskyblue1')
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
        oper = '*'
    return(a,b,oper)

#=====================================================================
#========================Saisie Manuelle==============================
#=====================================================================
def getEntry():
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

def Valide(saisie):
    
    if saisie == 1:
        S= Binaire_aleaEx2()
        
    elif saisie ==2:
        getEntry()
        sa= Binaire_saisEx2(Entier1, Entier2, oper)

    reponse = RepExo2(sa[0],sa[1],sa[2])
    #========================Vérification==============================
    # (rep => réponse calculé) qui est comparé à (util => réponse de l'utilisateur)
    rep = VerifRep(reponse,util)
    global resu
    
    if rep == 1:
        B3.destroy() #bloquer le bouton valider ==> Gagner
        resu=Label(cadre1, text="Bonne Réponse, Bravo !! ", font=("courier", 25, "italic"), fg='green', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        resu.pack(pady= 10, side=TOP)
    elif rep == -1:
        
        B3.destroy() #bloquer le bouton valider ==> Perdu
        resu=Label(cadre1, text="Mauvaise réponse, vous avez perdu ! Le résultat est : ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        resu.pack(pady= 10, side=TOP)
    elif rep == 0:
        
        resu=Label(cadre1, text="Mauvaise réponse, réessayer ! ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        resu.pack(pady= 10, side=TOP)
    
def RepExo2 (ch1,ch2,signe):
    if signe == 'x':
      repon = (bin(int(ch1, 2) * int(ch2, 2)).replace('0b',''))
    elif signe == '+':
      repon = (bin(int(ch1, 2) + int(ch2, 2)).replace('0b',''))
    elif signe == '-':
      repon = (bin(int(ch1, 2) - int(ch2, 2)).replace('0b',''))
    return(repon)
#bin permet de faire des calcul entre chiffre binaire mais il rajoute toujours un 0b devant, donc il faut mettre ".replace('0b','')" derrière pour enlever le 0b

#===========================================================
#========= Reset de l'exo ==================================
#===========================================================

def Nouveau(saisie):
    resu.destroy()
    Valide(saisie)
    
#===========================================================
#========= Fonction de l'exo ===============================
#===========================================================



def Exercice2(saisie):
    global saisieB1
    global saisieB2
    global saisieOper
    global saisieRep
    global B3

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
    
    tExo2 = Label(cadre1, text= "Opérations en binaire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    tExo2.pack(pady= 10, expand=YES)
                    
    st=Label(cadre1, text="Quelques Indications: ", font=("courier", 25, "italic"), fg='white', bg='#103985') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    st.pack(pady= 10, side=LEFT)
        
    txt1=Label(cadre2, text="Nombre Binaire 1 : ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt1.place(x=100, y=100)
    saisieB1=Entry(cadre2) 
    saisieB1.place(x=700, y=100, width=500, height=48)
    
    txt2=Label(cadre2, text="Choix d'opération (+,- ou x) :", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt2.place(x=100, y=160)
    saisieOper=Entry(cadre2) 
    saisieOper.place(x=700, y=150, width=500, height=48)

    txt3=Label(cadre2, text="Nombre binaire 2 : ", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt3.place(x= 100, y= 260)
    saisieB2=Entry(cadre2) 
    saisieB2.place(x=700, y=260, width=500, height=48)

    txt4=Label(cadre2, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt4.place(x=100, y= 320)
    saisieRep=Entry(cadre2) #width= largeur, height= hauteur) # Création de la zone de résultats
    saisieRep.place(x=700, y=320, width=500, height=48)


    
    

    B1=Button(cadre3, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='red', bg='#103985', width=20, height=2)
    B1.grid(row=0, column=0, pady=10, padx=10)
    B2=Button(cadre3, text="Nouveau", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2, command=partial(Nouveau,saisie))
    B2.grid(row=0, column=1, pady=10, padx=10)
    B3=Button(cadre3, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2, command=partial(Valide,saisie))
    B3.grid(row=0, column=2, pady=10, padx=10)
    B4=Button(cadre3, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2)
    B4.grid(row=0, column=3, pady=10, padx=10)
    B5=Button(cadre3, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=20, height=2, command=back)
    B5.grid(row=0, column=4, pady=10, padx=10)


cadre1.pack(fill=BOTH)
cadre2.pack(fill=BOTH, expand=1)
cadre3.pack(fill=BOTH)
        
