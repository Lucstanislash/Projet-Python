from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from functools import partial
from Outils import *
from random import*
import math

import Chapitre1.Exo3


import Chapitre1.Exo6
import Chapitre1.Exo7
import Chapitre1.Exo8



fenetre=Tk()
fenetre.title("Application Python")
fenetre.geometry("1500x700")
fenetre.minsize(500,600 )
#fenetre.iconbitmap("logo.ico")
fenetre.config(background='lightskyblue1')

fenetre.rowconfigure(1, weight=0)
fenetre.rowconfigure(2, weight=0)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=1)
fenetre.rowconfigure(7, weight=1)

fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=1)
fenetre.columnconfigure(6, weight=1)


#============== Fonctions globales =====================================

#la fonction PageChoix est à répéter 6 fois pour les exercise:
            #les entiés non signées (deja fais)
            #operation en binaire
            #operation sans calcul
            #décimaux
            #les réels
            #les tableaux

def ChapChoix():
    global titre
    global soustitre
    global signe
    global conversion
    global RetourM
    
    
    def back(t):#Retour
        if t== 1:
            titre.destroy()
            RetourM.destroy()
            soustitre.destroy()
            signe.destroy()
            conversion.destroy()
            PageChoix("Entiers signées")
        elif t==2:
            titre.destroy()
            RetourM.destroy()
            soustitre.destroy()
            signe.destroy()
            conversion.destroy()

    def CommandExo(t):
        
        if t == 'Signe':
            back(2)
            Exercice5a(fenetre)
            
        elif t == 'Conversion':
            back(2)
            Exercice5b(fenetre) # j'ai pas trop compris pourquoi on écris 2 fois exo 
        
    titre = Label(fenetre, text= "Entiers signés", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=1, columnspan=5)

    soustitre=Label(fenetre, text= "Choisissez votre exercice", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    soustitre.grid(row=3, column=1, columnspan=5,sticky='s')
            
    signe=Button(fenetre, text="Déterminer \n le signe", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Signe'))
    signe.grid(row=5, column=2, ipady=30, ipadx=140,sticky='e')

    conversion=Button(fenetre, text="Conversion", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Conversion'))
    conversion.grid(row=5, column=4, ipady=30,ipadx=140,sticky='w')

    RetourM=Button(fenetre, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=lambda:back(1))
    RetourM.grid(row=7, column=3,ipady= 15,ipadx=70)

# Command est la fonction produite en cliquant sur chaque exercice
def PageChoix(NomExercice): #======== Fenêtre de demande aléatoire ou manuel ===========
    tExoChap1.destroy() # pour détruire les buttons de la fenetre2= contient la liste des exos du Chap "Codage de l'information"
    Bexo1.destroy()
    Bexo2.destroy()
    Bexo3.destroy()
    Bexo4.destroy()
    Bexo5.destroy()
    Bexo6.destroy()
    Bexo7.destroy()
    Bexo8.destroy()
    Retour.destroy()

    def back(t): #Retour
        if t ==1:
            NomExo.destroy()
            txt3.destroy()
            bManuelle.destroy()
            bAléa.destroy()
            bRetour.destroy()
        elif t == 2:
            NomExo.destroy()
            txt3.destroy()
            bManuelle.destroy()
            bAléa.destroy()
            bRetour.destroy()
            Chap1() #Retour à la page précédente: fenetre des exercices(2eme)
            # Création des buttons de la 3eme fenetre répondant à la QUESTION (saisie manuel ou aléatoire)

    def CommandExo(t):
        if t == 'Aléa':
            if NomExercice == "Entiers non signées":
                Chapitre1.Exo1.Exercice1(1)
            if NomExercice == "Opérations en binaire":
                back(1)
                Exercice2(1, fenetre)
                
            if NomExercice == "Opérations sans calcul":
                back(1)
                Exercice4(fenetre, 2)
            if NomExercice == "Entiers signées":
                back(1)
                ChapChoix()
            if NomExercice == "Les Décimaux":
                back(1)
                Chapitre1.Exo6.Exercice6(fenetre, 1)
            if NomExercice == "Les Réels":
                back(1)
                Exercice7(fenetre, 1)
            if NomExercice == "Les Tableaux":
                back(1)
                Chapitre1.Exo8.Exercice8(fenetre,1)
            
        elif t == 'Manuel':
            if NomExercice == "Entiers non signées":
                Chapitre1.Exo1.Exercice1(2)
            if NomExercice == "Opérations en binaire":
                back(1)
                Exercice2(2, fenetre)
                
##                if Chapitre1.Exo2.Exercice2(2, fenetre) == True:
##                    Chap1()
            if NomExercice == "Opérations sans calcul":
                back(1)
                Exercice4(fenetre, 1)
            if NomExercice == "Entiers signées":
                back(1)
                ChapChoix()
            if NomExercice == "Les Décimaux":
                back(1)
                Chapitre1.Exo6.Exercice6(fenetre, 2)
            if NomExercice == "Les Réels":
                back(1)
                Exercice7(fenetre, 2)
            if NomExercice == "Les Tableaux":
                back(1)
                Chapitre1.Exo8.Exercice8(fenetre,2)
    
        #===== en cours
    NomExo = Label(fenetre, text= NomExercice, font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    NomExo.grid(row=1, column=1, columnspan=5)
    txt3=Label(fenetre, text= "Souhaitez vous une saisie Manuelle ou Aléatoire", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt3.grid(row=3, column=1, columnspan=5,sticky='s')
            
    bManuelle=Button(fenetre, text="Manuel", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(CommandExo,'Manuel'))
    bManuelle.grid(row=5, column=2, ipady=30, ipadx=140,sticky='e')

    bAléa=Button(fenetre, text="Aléatoire", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Aléa'))
    bAléa.grid(row=5, column=4, ipady=30,ipadx=140,sticky='w')

    bRetour=Button(fenetre, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(back,2))
    bRetour.grid(row=7, column=3,ipady= 15,ipadx=70)

def ChoixExo():
    tExoChap1.destroy() # pour détruire les buttons de la fenetre2= contient la liste des exos du Chap "Codage de l'information"
    Bexo1.destroy()
    Bexo2.destroy()
    Bexo3.destroy()
    Bexo4.destroy()
    Bexo5.destroy()
    Bexo6.destroy()
    Bexo7.destroy()
    Bexo8.destroy()
    Retour.destroy()

    Chapitre1.Exo3.Exercice3(fenetre)

#==================================================================================
#==============Menu c'est la fenetre principale contenant les 4 chapitres==========
#==================================================================================
    
def Menu():
    global Chap1
    global Exercice2
    global Exercice4
    global Exercice5a
    global Exercice5b
    global Exercice7
    #============================================================================
    #===================== Chapitre 1 ===========================================
    #============================================================================
    
    def Chap1(): #=====Chap1 est la 2eme fenetre contenant les 8 exercices
        global tExoChap1
        global Bexo1
        global Bexo2
        global Bexo3
        global Bexo4
        global Bexo5
        global Bexo6
        global Bexo7
        global Bexo8
        global Retour
        tMenu.destroy() # pour détruire les buttons de la fênetre 1=Menu
        stMenu.destroy()
        Bchap1.destroy()
        Bchap2.destroy()
        Bchap3.destroy()
        Bchap4.destroy()
        Quitter.destroy()

        def back(): # Retour

            tExoChap1.destroy()
            Bexo1.destroy()
            Bexo2.destroy()
            Bexo3.destroy()
            Bexo4.destroy()
            Bexo5.destroy()
            Bexo6.destroy()
            Bexo7.destroy()
            Bexo8.destroy()
            Retour.destroy()
            Menu() #Retour à la page précédente: fenetre des chapitres(1ere)
            
        # Création des exercices de la 2eme fenetre (c'est la fonction Chap1)
        largeur = 25
        hauteur = 2
      

        tExoChap1 = Label(fenetre, text= "Codage de l'information", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap1.grid(row=1, column=2,columnspan=4,ipady=40)
        
                    
        Bexo1=Button(fenetre, text="Entiers non signées", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        Bexo1.grid(ipady=25, row=2, column=1,columnspan=3,ipadx=50)

        Bexo2=Button(fenetre, text="Opérations en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Opérations en binaire"))
        Bexo2.grid(ipady=25,  row=3, column=1,columnspan=3,ipadx=50)

        Bexo3=Button(fenetre, text="Multiplications en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= ChoixExo)
        Bexo3.grid(ipady=25,  row=4, column=1,columnspan=3,ipadx=50)

        Bexo4=Button(fenetre, text="Opérations sans calcul", font=("courier", 18, "italic"), fg='white', bg='#103985',width=largeur, height=hauteur , command= partial(PageChoix,"Opérations sans calcul"))#command=affich3)
        Bexo4.grid(ipady=25,row=5, column=1,columnspan=3,ipadx=50)

        Bexo5=Button(fenetre, text="Entiers signées", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers signées"))
        Bexo5.grid(ipady=25,  row=2, column=3,columnspan=6,ipadx=50)

        Bexo6=Button(fenetre, text="Les Réels", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Réels"))
        Bexo6.grid(ipady=25,   row=3, column=3,columnspan=5,ipadx=50)

        Bexo7=Button(fenetre, text="Les Décimaux", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Décimaux"))#command=affich3)
        Bexo7.grid(ipady=25,  row=4, column=3,columnspan=5,ipadx=50)

        Bexo8=Button(fenetre, text="Les Tableaux", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Tableaux"))
        Bexo8.grid(ipady=25,row=5, column=3,columnspan=5,ipadx=50)

        Retour=Button(fenetre, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= back)
        Retour.grid(row=7, column=3,columnspan=4,ipadx=10,sticky='w')

#===================================================================================================================================================================================
#=========================================================================================
#===================== Chapitre 1 - Exercice 2 ===========================================
    
        
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
        if ope == '+' or ope == '-' or ope == 'x':
            op = ope
        else:
            messagebox.showerror("showerror", "Mauvaise saisie du signe d'opération")
        
        ent1=CtrlSyntaxe(e1,16,1,16)
        if ent1 == True:
            a = e1
        else:
            messagebox.showerror("showerror", "Mauvaise saisie du Nombre binaire 1")

        ent2=CtrlSyntaxe(e2,16,1,16)
        if ent2 == True:
            b = e2
        else:
            messagebox.showerror("showerror", "Mauvaise saisie du Nombre binaire 2")
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
    #========= Reset de l'exo 2 ==================================
    #===========================================================

    def Nouveau(saisie,fenetre):
        B3['state']='normal'
        B2['state']='disabled'
        tExo2.destroy()
        st.destroy()
        Exercice2(saisie,fenetre )
        #effacer ce qui a été entré

    #=========================================================================
    #================= Page rappel exo2 ===========================================
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
    
#===================================================================================================================================================================================
#=========================================================================================
#===================== Chapitre 1 - Exercice 4 ===========================================
    def Exercice4(f, select):
        fenetre=f
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

        man=select
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
                print("choix de la puissance : ",p)
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
            global op
            global ch
            global p
            donnee=Alea4()
            op=donnee[2]
            ch=donnee[0]
            p=int(donnee[1])
            
            def Exo4():
                
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
                    #res1="Réessayer"
                    messagebox.showerror("showerror", "Mauvaise réponse, veuillez réessayer")
                    res.delete(0, END)
                elif verif==-1:
                    B3['state']='disabled' #bloquer le bouton valider ==> Perdu
                    #res1="Réponse : \n" + rep
                    messagebox.showinfo(title="Information",
                                        message=" Mauvaise réponse!\n Le résultat est: \n"+rep)
                    B2['state']='normal'
                else:
                    #res1 = "Bravo !"
                    messagebox.showinfo(title="Bravo", message="Bravo! Vous pouvez continuer.")
                    B2['state']='normal'
                    B3['state']='disabled'
                #l4.config(text=res1)

            
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
           
            def Exo4():
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
                    messagebox.showerror("showerror", "Mauvaise réponse, veuillez réessayer")
                    res.delete(0, END)
                elif verif==-1:
                    B3['state']='disabled' #bloquer le bouton valider ==> Perdu
                    #res1="Réponse : \n" + rep
                    messagebox.showinfo(title="Information",
                                        message=" Mauvaise réponse!\n Le résultat est: \n"+rep)
                    B2['state']='normal'
                else:
                    #res1 = "Bravo !"
                    messagebox.showinfo(title="Bravo", message="Bravo! Vous pouvez continuer.")
                    B3['state']='disabled'
                    B2['state']='normal'
                #l4.config(text=res1)
            
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
        #========= Contrôle =========================================
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

        #l4 = Label(fenetre, text = "", font = "normal 20 bold", bg = 'lightskyblue1', width = 15)
        #l4.grid(row=2, column=3,columnspan=4,sticky='w',ipady=10)


        txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=10)
        oper.grid(row=3,column=2,ipadx=100,columnspan=4,ipady=10) # Placement de la zone de saisie
        txt2.grid(row=4, column=1,columnspan=2,sticky='w')
        nbbin.grid(row=4, column=2,ipadx=100,columnspan=4,ipady=10)
        txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=10)
        puis.grid(row=5, column=2,ipadx=100,columnspan=4,ipady=10)
        txt4.grid(row=6,column=1,columnspan=2,sticky='w',ipady=10)
        res.grid(row=6, column=2,ipadx=100,columnspan=4,ipady=10)

            
        B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())
        B2=Button(fenetre, text="Nouveau",font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Nouveau(), state='disabled')
        B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Exo4())
        B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, state='disabled')
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=15, height=2,command=fenetre.destroy)
         

        B1.grid(row=7, column=1)
        B2.grid(row=7, column=2)
        B3.grid(row=7, column=3)
        B4.grid(row=7, column=4)
        B5.grid(row=7, column=5)

#===================================================================================================================================================================================
#=========================================================================================
#===================== Chapitre 1 - Exercice 5a ===========================================
    def Exercice5a(f):
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

        fenetre=f
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

        soustitre=Label(fenetre, text="Quelques Indications: voir Rappel ", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

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
                elif Verif == 0 or Verif ==-1 :
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

#===================================================================================================================================================================================
#=========================================================================================
#===================== Chapitre 1 - Exercice 5b ===========================================

    def Exercice5b(f):
        Li=["10","SVA","C2"]

        def  AleaFormatBi5(Li):
                """Sort aléatoirement une valeur entre 0 et 3 pour choisir la base dans la liste li"""
                i=randrange(0,3)
                basedep=Li[i]
                return(basedep)
                
        def AleaFormatBis5(basedep):
                """on a retiré la base choisi aléatoirement puis on retire aléatoirement la base d'arrivé"""
                Libis=Li.copy()
                Libis.remove(basedep)
                i=randrange(0,2)
                basearriv=Libis[i]
                return (basearriv)

        def AleaExB5(basedep):
                """cree un entier aleatoire dans la bse basedep"""
                
                bit=randint(4,16)
                print(bit)
                        
                min= 1-2**(bit-1)
                print(min)
                
                max= 2**(bit-1)-1
                print(max)
                
                if basedep=="SVA" :
                        ent=AleaExAll(2,bit,bit)
                elif basedep=="C2":
                        ent=AleaExAll(2,bit,bit)
                        
                else:
                        ent=AleaExAll(10,min,max)
                                   
                return(ent,bit)



        def C2_ent(C):
                
            """Conversion  C2 vers entier"""

            if C[0]=="0":       
                return int(C,2)
            else:
                return int(C,2)-(1<<len(C))



        def EntierC2(entier):
            """Conversion entier vers C2"""    
            switch=''
            binaire=format(int(entier),'b')
            
            for i in binaire:
                if i == '1':
                    switch+='0'
                else:
                    switch+='1'
            
            rep=(bin(int(str(switch), 2) + int(str(1), 2)).replace("0b",""))
            if int(entier)>0:
                rep='0'+rep
            return(rep)

        def C2_SVA(basedep,entier):
                
                """Conversion C2 vers SVA"""  
                if basedep=="C2":
                        
                        entier=C2_ent(entier)
                        rep=Ent_SVA(entier)
                                        
                else:
                        rep=SVA_Ent(entier)
                        rep=EntierC2(rep)
                        
                return(rep)


                        
        def Ent_SVA(entier):
             """Conversion entier vers SVA"""     
             rep=format(int(entier),'b')
                
             if int(entier)<0:
                rep=rep.replace("-","1")

             else:
                rep='0'+rep
                
             return(rep)

        def SVA_Ent(entier):
              """Conversion SVA vers entier"""                
              rep=int(entier[1:],2)
              
              if entier[0]=="1":
                rep='-'+str(rep)

              return(rep) 

                        
        def RepExB5(basedep,entier,basearriv):
                """exercice global avec choix aléatoire de la base + valeur de la réponse"""

                if basedep=="10":
                        if basearriv=="C2":
                             rep=EntierC2(entier)
                        else:
                             rep=Ent_SVA(entier)
                                
                                                       
                        
                elif basedep=="C2":
                        if basearriv=="10":
                              rep=C2_ent(entier)
                              
                        else:
                              rep=C2_SVA(basedep,entier)
                              
                              
                else:
                        if basearriv=="10":                     
                              rep=SVA_Ent(entier)
                                                     
                        else:
                              rep=C2_SVA(basedep,entier)
                       
                
                return(rep)

        ###############################################################INTERFACE###########################################################################
        fenetre=f
        fenetre.config(background="lightskyblue1")

        fenetre.rowconfigure(1, weight=0)
        fenetre.rowconfigure(2, weight=0)
        fenetre.rowconfigure(3, weight=1)
        fenetre.rowconfigure(4, weight=1)
        fenetre.rowconfigure(5, weight=1)
        fenetre.rowconfigure(6, weight=1)
        fenetre.rowconfigure(7, weight=1)
        fenetre.rowconfigure(8, weight=1)



        fenetre.columnconfigure(0, weight=1)
        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, weight=1)
        fenetre.columnconfigure(3, weight=1)
        fenetre.columnconfigure(4, weight=1)
        fenetre.columnconfigure(5, weight=1)

        man=2

        if man==1:
                based=AleaFormatBi5(Li)
                basea=AleaFormatBis5(based)        

                
        def Validation():

                ok=True
                saisie=control()
                
                if not saisie==1 :

                        Bits=saisie[4]
                        entier=saisie[0]
                        
                        if not Bits=='Appuyer sur Go':
                                rep=RepExB5(saisie[0],saisie[1],saisie[2])
                                
                                for i in range (int(Bits)-len(str(rep))):
                
                                        rep="0"+rep
                                       
                        else:
                                rep=RepExB5(saisie[0],saisie[1],saisie[2])

                        print("voici la rep",rep)
                        util=saisie[3]
                        
                        Verif=VerifRep(str(rep),util)

                        if ok==True:
                                
                                if Verif == 1:
                                        B3['state']='disabled' #bloquer le bouton valider ==> Gagner
                                        B2['state']='normal'
                                        messagebox.showinfo(title="Information",
                                                    message="Bonne Réponse, Bravo !! ")
                                elif Verif == -1:
                                        B3['state']='disabled' #bloquer le bouton valider ==> Perdu
                                        B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
                                        messagebox.showinfo(title="Information",
                                                    message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("".join(str(rep))))
                                elif Verif == 0:
                                       messagebox.showinfo(title="Information",
                                                    message="Mauvaise réponse, réessayer !")
                
        def control():
                
                if man==2:

                        basedep=fenetre.menud.get()
                        basearriv=fenetre.menua.get()
                        entier=Val.get()
                        Bits=Nb.get()
                        util=Resultats.get()

                else :
                        
                        basedep=menuD.get()
                        entier=Val.get()
                        basearriv=menuA.get()
                        Bits='Appuyer sur Go'
                        util=Resultats.get()
                        bit=Nb.get()

                   
                print("ici la base de départ",basedep)
                print("voici la base arrive",basearriv)
                
                if basedep=="SVA" or basedep=="C2":
                        
                        if entier=='' or  util=='' :
                                messagebox.showerror("showerror", "Toutes les valeurs ne sont pas saisie")
                                return(1)
                        else:
                                ctrl=CtrlSyntaxe(entier,2,2,16)

                                if ctrl==True: 
                                        if basearriv=="10":
                                                
                                                Bits='0'
                                                ctrlR=CtrlSyntaxe(util,10,0,5,-99999,99999)

                                                if not ctrlR==True:
                                                        
                                                        messagebox.showerror("showerror", "erreur de syntaxe dans la réponse")
                                                        return(1)
                                        else:
                                        
                                                if man==2:
                                                        ct=CtrlSyntaxe(str(Bits),10,1,10,4,16)
                                                else:
                                                        Bits=bit
                                                        ct=CtrlSyntaxe(str(Bits),10,1,10,4,16)

                                                if ct == True:
                                                
                                                        ctrlR=CtrlSyntaxe(util,2,int(Bits), int(Bits))
                                                        if ctrlR==True:
                                                                
                                                                if not len(str(entier))==len(str(util)):
                                                                   
                                                                        messagebox.showerror("showerror", "Les deux chaines non pas la même longueur")
                                                                        return(1)
                                                        else:
                                                                
                                                                messagebox.showerror("showerror", "erreur de syntaxe dans la réponse,ou ne correspond pas au nombre de bit")
                                                                return(1)
                                                else:
                                                        messagebox.showerror("showerror", "Les bits ne sont pas dans la bonne intervalle")
                                                        return(1)

                                else:                   
                                        
                                        messagebox.showerror("showerror", "erreur de syntaxe sur l'entier de départ")
                                        return(1)


                                        
                elif basedep=="10":
                        
                        if entier=='' or Bits==''  or  util=='':
                                messagebox.showerror("showerror", "Toutes les valeurs ne sont pas saisie")
                                return(1)
                        else:


                                if man==2:
                                        ct=CtrlSyntaxe(str(Bits),10,1,4,4,16)
                                else:
                                        Bits=bit
                                        print(Bits)
                                        ct=CtrlSyntaxe(str(Bits),10,1,4,4,16)
                
                                if ct==True:
                                        min= 1-2**(int(Bits)-1)
                                        max= 2**(int(Bits)-1)-1
         
                                        ctrl=CtrlSyntaxe(str(entier),10,1,10,min,max)
                                  

                                        if ctrl==True:
                                                ctrlR=CtrlSyntaxe(util,2,int(Bits),int(Bits))

                                                if not ctrlR==True:
                                                         messagebox.showerror("showerror", "erreur de syntaxe dans la réponse")
                                                         return(1)
                                                
                                        else:
                                                messagebox.showerror("showerror", "erreur de syntaxe dans l'entier de départ")
                                                return(1)
                                                

                                else:
                                        messagebox.showerror("showerror", "Bits non compris dans l'intervalle")
                                        return(1)                
                    
                        
                return(basedep,entier,basearriv,util,Bits)

        def go(): # permet d'afficher ou non le nombre de bits et de calculer la valeur absolu
                GO['state']='disabled'


                if man==1:                
                        based=menuD.get()
                        basea=menuA.get()
                        donne=AleaExB5(based)
                        val=donne[0]
                        bit=donne[1]
                                
                        print("go base dep",based)
                        print("go base arriv",basea)
                        print("voici l'entier",val)
                        
                        if basea=="SVA"or basea=="C2":
                                if based=="C2" or based=="SVA":

                                        Nb.configure(state="normal")
                                        Nb.delete(0,END)
                                        Nb.insert(0,bit)
                                        
                        
                                elif based=="10":

                                        Nb.configure(state="normal")
                                        Nb.delete(0,END)
                                        Nb.insert(0,bit)

                                       
                        elif basea=="10":
                                Nb.configure(state="normal")
                                Nb.delete(0,END)
                                Nb.insert(0,"Donnée non utile")
                                Nb.configure(state="disabled")
                                        
                        
                        Val.configure(state="normal")
                        Val.delete(0,END)
                        Val.insert(0, val)
                        
                
                if man==2:
                       
                                      
                        if fenetre.menud.get()==fenetre.menua.get():
                                messagebox.showerror("showerror", "La base de départ ne peut pas être identique à la base d'arrivée")
                                GO['state']='normal'

                        else :
                                Val.configure(state="normal")
                                Val.delete(0,END)

                                if fenetre.menua.get()=="10":
                                        
                                        Nb.configure(state="normal")
                                        Nb.delete(0,END)
                                        Nb.insert(0,"Donnée inutile")
                                        Nb.configure(state="disabled")
                                                               
                                else:
                                        
                                        Nb.configure(state="normal")
                                        Nb.delete(0,END)

                                GO['state']='disabled'
                         
                        

        def nouveau():

            B3['state']='normal'
            B2['state']='disabled'
            GO['state']='normal'

            if man ==2 :
                    
                Val.delete(0,END)
                Val.insert(0, "Appuyer sur Go")
                Val.configure(state="readonly")
                
                Nb.configure(state="normal")
                Nb.delete(0,END)
                Nb.insert(0, "Appuyer sur Go")
                Nb.configure(state="readonly")
             
                Resultats.delete(0,END)
                
            elif man==1:
               
                based=AleaFormatBi5(Li)
                basea=AleaFormatBis5(based)
              
                Resultats.delete(0,END)
                
                Val.delete(0,END)
                Val.insert(0, "Appuyer sur Go")
                Val.configure(state="readonly")
                
                Nb.configure(state="normal")
                Nb.delete(0,END)
                Nb.insert(0, "Appuyer sur Go")
                Nb.configure(state="readonly")

                menuA.configure(state="normal")
                menuA.delete(0,END)
                menuA.insert(0, basea)
                menuA.configure(state="readonly")

                menuD.configure(state="normal")
                menuD.delete(0,END)
                menuD.insert(0, based)
                menuD.configure(state="readonly")

                
                
                
        Val=Entry(justify='center',borderwidth=3)
        Val.insert(0, "Appuyer sur Go")
        Val.configure(state="readonly")
        Val.grid(row=6, column=2,ipadx=200,columnspan=4,ipady=15)        

        Nb=Entry(justify='center',borderwidth=3)
        Nb.insert(0, "Appuyer sur Go")
        Nb.configure(state="readonly")

        Nb.grid(row=5, column=2,ipadx=200,columnspan=4,ipady=15)

                        
        titre=Label(fenetre, text="Conversion", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  

        soustitre=Label(fenetre, text="Quelques Indications: valeur 1000000000 impossible à convertir\n Attention pas de virgule mais des points                       \n    La valeur absolue doit être comprise entre 1-2^(n-1) et 2^(n-1)-1.", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

        txt1=Label(fenetre, text="Format de départ", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
           
            fenetre.menud= tk.StringVar(fenetre)
            menuD = ttk.OptionMenu(fenetre,fenetre.menud,Li[0], *Li)
        else:
            menuD=Entry(fenetre,justify='center',borderwidth=3)
            menuD.insert(0, based)
            menuD.configure(state="readonly")


        txt2=Label(fenetre, text="Format d'arrivée", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
           
            fenetre.menua= tk.StringVar(fenetre)
            menuA = ttk.OptionMenu(fenetre,fenetre.menua,Li[0], *Li)
        else:
            menuA=Entry(fenetre,justify='center',borderwidth=3)
            menuA.insert(0, basea)
            menuA.configure(state="readonly")



        txt3=Label(fenetre, text="Nombre de bits\n(entre 4 et 16)", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')


        txt4=Label(fenetre, text="Valeur de départ", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')



        txt5=Label(fenetre, text="Résultats", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')

        Resultats=Entry(fenetre,justify='center',borderwidth=3)



        def create():
            rappel = Toplevel(fenetre)
            rappel.config(background="lightskyblue1")
            titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
            titre.grid(row=1, column=2,columnspan=3,sticky='s')

            txt1=Label(rappel, text="Si l’entier codé en SVA/C2 commence par 1 : \n son signe est négatif.", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
            txt2=Label(rappel, text="Si l’entier codé en SVA/C2 commence par 0 : \n son signe est positif.", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
            txt3=Label(rappel, text="Pour convertir un nombre négatif de C2 vers \n SVA: on soustrait 1,puis on inverse les bits\nen faisant attention au signe.", font=("courier", 25, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
            txt4=Label(rappel, text="Pour coder un entier négatif en C2 :on part \nde la valeur absolue,on inverse les bits puis\n on ajoute 1", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

            txt1.grid(row=2, column=3,ipadx=50,ipady=40)
            txt2.grid(row=3, column=3,ipadx=50,ipady=40)
            txt3.grid(row=4, column=3,ipadx=50,ipady=40)
            txt4.grid(row=5, column=3,ipadx=50,ipady=40)

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
         
        B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Validation())
         
        B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2)
         
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=fenetre.destroy)


        GO=Button(fenetre, text="Go!", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=10, height=0,command=lambda:go())        
        GO.grid(row=4, column=5,sticky='n')

        titre.grid(row=1, column=2,columnspan=3)
        soustitre.grid(row=2, column=1,columnspan=5,sticky='w',ipady=40)

        txt1.grid(row=3, column=1,columnspan=2,sticky='w')
        menuD.grid(row=3, column=2,ipadx=200,columnspan=4,ipady=15)

        txt2.grid(row=4, column=1,columnspan=2,sticky='w')
        menuA.grid(row=4, column=2,ipadx=200,columnspan=4,ipady=15)


        txt3.grid(row=5, column=1,columnspan=2,sticky='w')


        txt4.grid(row=6, column=1,columnspan=2,sticky='w')



        txt5.grid(row=7, column=1,columnspan=2,sticky='w')
        Resultats.grid(row=7, column=2,ipadx=200,columnspan=4,ipady=15)



        #bouton#
        B1.grid(row=8, column=1)
        B2.grid(row=8, column=2)
        B3.grid(row=8, column=3)
        B4.grid(row=8, column=5)
        B5.grid(row=8, column=4)

#===================================================================================================================================================================================
#==========================================================================================
#===================== Chapitre 1 - Exercice 7 ===========================================
    def Exercice7(f, select):
        def Ent_IEEE(floatt):
            """fonction qui transforme un entier en IEEE"""
        ##conversion float vers entier##
            entier=int(float(floatt))
        ## conversion entier vers binaire##
            
            binaire= format(entier,'b')
            if int(entier)<0:
                binaire=binaire.replace("-","")    

        ## on sépare la chaine en 2 le bit implicite dans la première le reste dans l'autre
            ch_imp=binaire[0]
            ch_rest=binaire[1:]

        ## calcul de exposant puis conv vers binaire
            Exp=127+(len(ch_rest))
         
            ExpB= format(Exp,'b')
             
        ## calcul de la taille de la mantisse pour les décimaux
            FMantisse= 32-(len(ExpB)+len(binaire))

        #transforme la partie décimal d'un float en binaire avec pour longueur FMantisse
            ch_dec=""
            dec=str(float(floatt)).replace(str(int(float(floatt))),'0')

            for i in range(FMantisse):
                dec=float(dec)*2
                if int(dec) >= 1:
                    dec-=1
                    ch_dec+='1'
                else:
                    ch_dec+='0'
        ##concaténation des diff chaines 
            IEEE=ch_imp+ExpB+ch_rest+ch_dec
            Hexa=Conv(2,16,IEEE)
            Hexa= Hexa.upper()
            return(Hexa)

        ###IEEE=Ent_IEEE(floatt)


        def IEE_Ent(Hexa):
            """fonction qui transforme un IEEE en entier"""
            IEEE=Conv(16,2,Hexa)
            
        ## récupère  l'exposant en binaire et le bim implicite
            ExpB=IEEE[1:9]
            ch_imp=IEEE[0]
            
        ## conversion en entier puis - 127 pour déterminer l'exposant
            Exp=int(ExpB,2)

            Exp=Exp-127

        ##récupère les bits de la valeur de l'entier
            n=Exp+9
            ch_rest=IEEE[9:n]
            finIEEE=IEEE[n:]

        ## reconstitue la chaine en binaire de l'entier puis conversion de entier
            
            binaire=ch_imp+ch_rest
            entier=int(binaire,2)
            
            if ch_imp[0]=="1":
                entier='-'+str(entier)

            cpt=0
            dec=0
            for i in finIEEE:
                cpt-=1
                if i=='1':
                    dec+=2**cpt
            dec=round(dec,2)
            
            rep=str(dec).replace("0",entier)  
            return(rep)

        lis=["IEEE","entier"]

        def  AleaFormat5(lis):
                """Sort aléatoirement une valeur entre 1 et 2 pour choisir la base dans la liste li"""
                i=randrange(0,2)
                formats=lis[i]
                return(formats)
            
        def AleaEx7Ent():
            entier=random.uniform(-1000,10000)
            entier=round(entier,2)
            return(entier)
           
        def AleaEx7IEEE():   

            Hexa=AleaExAll(16,8,8)
            return(Hexa)

        def SaisieAllEx7():
            formats=AleaFormat5(lis)
            if formats=="entier":
                    valeur=AleaEx7IEEE()
                    
            else:     
                    valeur=AleaEx7Ent()
                    
            return(valeur,formats)

        fenetre=f


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
        
        man=select # variable qui va définir si c'est manuel ou aléatoire
        
        formats=""
        if man ==1 :
            alea=SaisieAllEx7()
            formats=alea[1]
            valeur=alea[0]
            
        def get(formats):
            if man==2:
                entier = saisieVal.get()
                util = Resultats.get()
                formats = fenetre.option_var.get()
            else:
                entier=valeur
                util = Resultats.get()

            if formats=="IEEE":
                ok=CtrlSyntaxe(str(entier),10,1,20,-10000,10000)
                ok2=CtrlSyntaxe(util,16,1,8)
                if ok==False: 
                    messagebox.showerror("showerror", "Erreur de saisie du réel")
                    return(1)
                elif ok2==False:
                    messagebox.showerror("showerror", "Erreur de saisie du résultat")
                    return(1)
            else:
                ok=CtrlSyntaxe(entier,16,1,8)
                ok2=CtrlSyntaxe(util,10,1,20,-10000,10000)
                if ok==False: 
                    messagebox.showerror("showerror", "Erreur de saisie du réel")
                    return(1)
                elif ok2==False:
                    messagebox.showerror("showerror", "Erreur de saisie du résultat")
                    return(1)
            
            if formats=="IEEE":
                rep=Ent_IEEE(entier)

            else:
                rep=IEE_Ent(entier)
            
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


        OptionsExo1 = ("IEEE","entier")


        titre=Label(fenetre, text="Les réels", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  # Placement de l'invite

        soustitre=Label(fenetre, text="Quelques Indications: Les valeurs en base 10 sont compris entre -10 000 et 10 000 \n Attention mettre un . et non , pour les réels à virgule ", font=("courier", 20, "italic"), fg='darkblue', bg='lightskyblue1') 
        ##
        ##indication=Label(fenetre,text="Les valeurs en base 10 sont compris entre -10 000 et 10 000 ", font=("courier", 10), fg='darkblue', bg='lightskyblue1') 

        txt1=Label(fenetre, text="Réel à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
            
            saisieVal=Entry(fenetre) 
            val=StringVar(fenetre) # variable qui récupérera la valeur de la case à cocher

        else:
            saisieVal=Label(fenetre, text=valeur, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)



        txt2=Label(fenetre, text="Convertir au format", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
           
            fenetre.option_var= tk.StringVar(fenetre)
            w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo1[0], *OptionsExo1)
        else:
            w1=Label(fenetre, text=formats, font=("courier", 15, "italic"), fg='black', bg='white',width=4, height=1)



        txt3=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')

        Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats


                
        #=========================================================================
        #================= Page rappel ===========================================
        #=========================================================================

        def create():
            rappel = Toplevel(fenetre)
            rappel.config(background="lightskyblue1")
            titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
            titre.grid(row=1, column=2,columnspan=3,sticky='s')

            txt1=Label(rappel, text="1 bit de signe", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
            txt2=Label(rappel, text="8 bits d’exposant biaisé (biaisé de 127)", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
            txt3=Label(rappel, text="23 bits de mantisse", font=("courier", 25, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
            txt4=Label(rappel, text="Ne pas oublier le bit implicite", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

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

            btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2)
            btn.grid(row=6, column=2,columnspan=3,sticky='n')

        #=========================================================================


        def nouveau():
            B3['state']='normal'
            B2['state']='disabled'
            if man ==1 :
                alea=SaisieAllEx7()
                formats=alea[1]
                valeur=alea[0]
                saisieVal.config(text=valeur)
                w1.config(text=formats)
                Resultats.delete(0,END)
            else:
                
               saisieVal.delete(0,END)
               Resultats.delete(0,END)
                
        B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='grey', width=15, height=2,command=lambda:create())

        B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
         
        B3=Button(fenetre, text="Valider", font=("courier", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(formats))
         
        B4=Button(fenetre, text="Score", font=("courier", 18, "bold"), fg='white', bg='#103985', width=15, height=2,state='disabled')
         
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fenetre.destroy)

        titre.grid(row=1, column=2,columnspan=3)
        soustitre.grid(row=2, column=1,columnspan=5,sticky='w',ipady=40)
        txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=40)
        saisieVal.grid(row=3, column=2,ipadx=200,columnspan=4,ipady=10)

        txt2.grid(row=4, column=1,columnspan=2,sticky='w')
        txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=40)
        w1.grid(row=4, column=2,ipadx=235,columnspan=4,ipady=10)
        Resultats.grid(row=5, column=2,ipadx=200,columnspan=4,ipady=10)



        #bouton#
        B1.grid(row=6, column=1)
        B2.grid(row=6, column=2)
        B3.grid(row=6, column=3)
        B4.grid(row=6, column=4)
        B5.grid(row=6, column=5)
    #============================================================================
    #===================== Chapitre 2 ===========================================
    #============================================================================
    def Chap2():
        tMenu.destroy() # pour détruire les buttons de la fênetre 1=Menu
        stMenu.destroy()
        Bchap1.destroy()
        Bchap2.destroy()
        Bchap3.destroy()
        Bchap4.destroy()
        Quitter.destroy()
        def back(): # Retour
            tExoChap2.destroy()
            st.destroy()
            Retour.destroy()
            Menu()
        tExoChap2 = Label(fenetre, text= "Ordonnancement", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap2.grid(row=1, column=1,columnspan=4)

        st = Label(fenetre, text= "Partie en cours de création", font=("Courier", 28, "italic"), fg='blue4', bg='lightskyblue1')
        st.grid(row=2, column=1,columnspan=4)

        Retour=Button(fenetre, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command= back)
        Retour.grid(row=6, column=2,columnspan=3)


    #============================================================================
    #===================== Chapitre 3 ===========================================
    #============================================================================
        
    def Chap3():
        tMenu.destroy() # pour détruire les buttons de la fênetre 1=Menu
        stMenu.destroy()
        Bchap1.destroy()
        Bchap2.destroy()
        Bchap3.destroy()
        Bchap4.destroy()
        Quitter.destroy()
        def back(): # Retour
            tExoChap3.destroy()
            st.destroy()
            Retour.destroy()
            Menu()
        tExoChap3 = Label(fenetre, text= "Gestion de la mémoire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap3.grid(row=1, column=1,columnspan=4)

        st = Label(fenetre, text= "Partie en cours de création", font=("Courier", 28, "italic"), fg='blue4', bg='lightskyblue1')
        st.grid(row=2, column=1,columnspan=4)

        Retour=Button(fenetre, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command= back)
        Retour.grid(row=6, column=2,columnspan=3)

    #============================================================================
    #===================== Chapitre 4 ===========================================
    #============================================================================

    def Chap4():
        tMenu.destroy() # pour détruire les buttons de la fênetre 1=Menu
        stMenu.destroy()
        Bchap1.destroy()
        Bchap2.destroy()
        Bchap3.destroy()
        Bchap4.destroy()
        Quitter.destroy()
        def back(): # Retour
            tExoChap4.destroy()
            st.destroy()
            Retour.destroy()
            Menu()
        tExoChap4 = Label(fenetre, text= "Gestion de fichier", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap4.grid(row=1, column=1,columnspan=4)

        st = Label(fenetre, text= "Partie en cours de création", font=("Courier", 28, "italic"), fg='blue4', bg='lightskyblue1')
        st.grid(row=2, column=1,columnspan=4)

        Retour=Button(fenetre, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command= back)
        Retour.grid(row=6, column=2,columnspan=3)

        
    #============Création des chapitres de la 1ere fenetre    
    tMenu=Label(fenetre, text= "Bienvenue sur l'application d'entrainement", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    tMenu.grid(row=1, column=2, columnspan=3,ipady=40)
    stMenu=Label(fenetre, text= "Séléctionner le module que vous souhaitez travailler", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    stMenu.grid(row=2, column=2, columnspan=3,ipady=40)
    
    Bchap1=Button(fenetre, text="Codage de l'information", font=("courier", 18, "italic"), fg='white', bg='#103985', command = Chap1)
    Bchap1.grid(row=3, column=3,sticky='ew',ipady=10)

    Bchap2=Button(fenetre, text="Ordonnancement", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap2)#command= Chap2
    Bchap2.grid(row=4, column=3,sticky='ew',ipady=10)

    Bchap3=Button(fenetre, text="Gestion de la mémoire", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap3)#command= Chap3
    Bchap3.grid(row=5, column=3, sticky='ew',ipady=10)

    Bchap4=Button(fenetre, text="Gestion de fichier", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap4) #command= Chap4
    Bchap4.grid(row=6, column=3,sticky='ew',ipady=10)
    
    Quitter=Button(fenetre, text= "Quitter", font=("courier", 18, "italic"), fg='white', bg='#103985', command= fenetre.destroy)
    Quitter.grid(row=7, column=3)




Menu()



fenetre.mainloop()
