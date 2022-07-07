from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from functools import partial
from Outils import *
from random import*
import random
import math

fenetre=Tk()    ## Permet de creer une fenetre

fenetre.title("Application Python")
fenetre.geometry("1250x650")
fenetre.minsize(500,600 )
##fenetre.iconbitmap("logo.ico")
fenetre.config(background='lightskyblue1')

fenetre.rowconfigure(1, weight=0)
fenetre.rowconfigure(2, weight=0)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=1)
fenetre.rowconfigure(7, weight=1)
fenetre.rowconfigure(8, weight=1)
fenetre.rowconfigure(9, weight=1)
fenetre.rowconfigure(10, weight=1)
fenetre.rowconfigure(11, weight=1)
fenetre.rowconfigure(12, weight=1)
fenetre.rowconfigure(13, weight=1)
fenetre.rowconfigure(14, weight=1)
fenetre.rowconfigure(15, weight=1)
fenetre.rowconfigure(16, weight=1)
fenetre.rowconfigure(17, weight=1)
fenetre.rowconfigure(18, weight=1)


fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=0)
fenetre.columnconfigure(6, weight=1)
fenetre.columnconfigure(7, weight=1)
fenetre.columnconfigure(8, weight=1)
fenetre.columnconfigure(9, weight=1)
fenetre.columnconfigure(10, weight=1)
fenetre.columnconfigure(11, weight=1)
fenetre.columnconfigure(12, weight=1)



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
            PageChoix("Entiers signés")
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
            Exercice5b(fenetre,1) 
        
    titre = Label(fenetre, text= "Entiers signés", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=2, column=4, columnspan=5)

    soustitre=Label(fenetre, text= "Choisissez votre exercice", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    soustitre.grid(row=4, column=4, columnspan=5,sticky='s')
            
    signe=Button(fenetre, text="Déterminer \n le signe", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Signe'))
    signe.grid(row=10, column=6, ipady=16, ipadx=140,sticky='nesw')

    conversion=Button(fenetre, text="Conversion", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Conversion'))
    conversion.grid(row=10, column=8, ipady=16,ipadx=140,sticky='nesw')

    RetourM=Button(fenetre, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=lambda:back(1))
    RetourM.grid(row=17, column=4,columnspan=6,ipady= 15,ipadx=70)




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
            if NomExercice == "Entiers non signés":
                back(1)
                Exercice1(fenetre, 1)
            if NomExercice == "Opérations en binaire":
                back(1)
                Exercice2(1, fenetre)
            if NomExercice == "Opérations sans calcul":
                back(1)
                Exercice4(fenetre, 2)
            if NomExercice == "Entiers signés":
                back(1)
                ChapChoix()
            if NomExercice == "Les Décimaux":
                back(1)
                Exercice6(fenetre, 1)
            if NomExercice == "Les Réels":
                back(1)
                Exercice7(fenetre, 1)
            if NomExercice == "Les Tableaux":
                back(1)
                Exercice8(fenetre,1)
            
        elif t == 'Manuel':
            if NomExercice == "Entiers non signés":
                back(1)
                Exercice1(fenetre, 2)
            if NomExercice == "Opérations en binaire":
                back(1)
                Exercice2(2, fenetre)
            if NomExercice == "Opérations sans calcul":
                back(1)
                Exercice4(fenetre, 1)
            if NomExercice == "Entiers signés":
                back(1)
                Exercice5b(fenetre,2)
            if NomExercice == "Les Décimaux":
                back(1)
                Exercice6(fenetre, 2)
            if NomExercice == "Les Réels":
                back(1)
                Exercice7(fenetre, 2)
            if NomExercice == "Les Tableaux":
                back(1)
                Exercice8(fenetre,2)
    
        #===== en cours

    NomExo = Label(fenetre, text= NomExercice, font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    NomExo.grid(row=2, column=4, columnspan=5)
    txt3=Label(fenetre, text= "Souhaitez vous une saisie Manuelle ou Aléatoire", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt3.grid(row=4, column=4, columnspan=5,sticky='s')
            
    bManuelle=Button(fenetre, text="Manuel", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(CommandExo,'Manuel'))
    bManuelle.grid(row=10, column=6, ipady=30, ipadx=140,sticky='nesw')

    bAléa=Button(fenetre, text="Aléatoire", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Aléa'))
    bAléa.grid(row=10, column=8, ipady=30,ipadx=140,sticky='nesw')

    bRetour=Button(fenetre, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(back,2))
    bRetour.grid(row=17, column=4,columnspan=6,ipady= 15,ipadx=70)

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

    Exercice3(fenetre)

#==================================================================================
#==============Menu c'est la fenetre principale contenant les 4 chapitres==========
#==================================================================================
    
def Menu():
    global Chap1
    global Exercice1
    global Exercice2
    global Exercice3
    global Exercice4
    global Exercice5a
    global Exercice5b
    global Exercice6
    global Exercice7
    global Exercice8
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
        tExoChap1.grid(row=1, column=4,columnspan=6,ipady=40)
        
                    
        Bexo1=Button(fenetre, text="Entiers non signés", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signés")) #, command= PageChoix("Entiers non signées")
        Bexo1.grid(ipady=25, row=3, column=2,columnspan=3,ipadx=50,sticky='e')

        Bexo2=Button(fenetre, text="Opérations en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Opérations en binaire"))
        Bexo2.grid(ipady=25,  row=4, column=2,columnspan=3,ipadx=50,sticky='e')

        Bexo3=Button(fenetre, text="Multiplications en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= ChoixExo)
        Bexo3.grid(ipady=25,  row=5, column=2,columnspan=3,ipadx=50,sticky='e')

        Bexo4=Button(fenetre, text="Opérations sans calcul", font=("courier", 18, "italic"), fg='white', bg='#103985',width=largeur, height=hauteur , command= partial(PageChoix,"Opérations sans calcul"))#command=affich3)
        Bexo4.grid(ipady=25,row=6, column=2,columnspan=3,ipadx=50,sticky='e')

        Bexo5=Button(fenetre, text="Entiers signés", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers signés"))
        Bexo5.grid(ipady=25,  row=3, column=5,columnspan=7,ipadx=50)

        Bexo6=Button(fenetre, text="Les Réels", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Réels"))
        Bexo6.grid(ipady=25,   row=4, column=5,columnspan=7,ipadx=50)

        Bexo7=Button(fenetre, text="Les Décimaux", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Décimaux"))#command=affich3)
        Bexo7.grid(ipady=25,  row=5,column=5,columnspan=7,ipadx=50)

        Bexo8=Button(fenetre, text="Les Tableaux", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Tableaux"))
        Bexo8.grid(ipady=25,row=6, column=5,columnspan=7,ipadx=50)

        Retour=Button(fenetre, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= back)
        Retour.grid(row=17, column=4,columnspan=5,ipadx=5)
#===================================================================================================================================================================================
#=========================================================================================
#===================== Chapitre 1 - Exercice 1 ===========================================
        
    def Exercice1(f, select):
        #========================================================================================       
        fen=f
        fen.config(background="lightskyblue1")

        fen.rowconfigure(1, weight=0)
        fen.rowconfigure(2, weight=0)
        fen.rowconfigure(3, weight=1)
        fen.rowconfigure(4, weight=1)
        fen.rowconfigure(5, weight=1)
        fen.rowconfigure(6, weight=1)
        fen.rowconfigure(7, weight=1)
        fen.rowconfigure(8, weight=1)
        fen.rowconfigure(9, weight=1)
        fen.rowconfigure(10, weight=1)
        fen.rowconfigure(11, weight=1)
        fen.rowconfigure(12, weight=1)
        fen.rowconfigure(13, weight=1)
        fen.rowconfigure(14, weight=1)
        fen.rowconfigure(15, weight=1)
        fen.rowconfigure(16, weight=1)
        fen.rowconfigure(17, weight=1)
        fen.rowconfigure(18, weight=1)


        fen.columnconfigure(1, weight=1)
        fen.columnconfigure(2, weight=1)
        fen.columnconfigure(3, weight=1)
        fen.columnconfigure(4, weight=1)
        fen.columnconfigure(5, weight=0)
        fen.columnconfigure(6, weight=1)
        fen.columnconfigure(7, weight=1)
        fen.columnconfigure(8, weight=1)
        fen.columnconfigure(9, weight=1)
        fen.columnconfigure(10, weight=1)
        fen.columnconfigure(11, weight=1)
        fen.columnconfigure(12, weight=1)


        #======================= Rappel =================================
        #https://apcpedagogie.com/rappels-sur-les-nombres-binaires/
        #https://www.iro.umontreal.ca/~monnier/1215/notes-numberbases.pdf
        #https://electrotoile.eu/conversion_numeration.php#:~:text=Pour%20r%C3%A9aliser%20cette%20conversion%20il,%3A%201001%200101(2).

        #======================Aléatoire=================================
        man=select
        entier=''
        basedep=''
        basearr=''
        ko=0
        def alea(man,ko):
            global basedep
            global basearr
            global entier
            global A1
            global A2
            global A3
            global A4
            global A5
            global A6
            global A7
            global A8
            global Esaisie
            if man ==1:
                base=(2,8,10,16)
                basedep=randint(0,3)
                basearr=randint(0,3)
                while basedep==basearr:
                    basedep=randint(0,3)
                    basearr=randint(0,3)
                basedep=base[basedep]
                basearr=base[basearr]
                dicoNb={}
                dicoNb[2]='disabled','normal','disabled','disabled','Gainsboro','salmon','Gainsboro','Gainsboro'
                dicoNb[8]='disabled','disabled','disabled','normal','Gainsboro','Gainsboro','Gainsboro','salmon'
                dicoNb[10]='normal','disabled','disabled','disabled','salmon','Gainsboro','Gainsboro','Gainsboro'
                dicoNb[16]='disabled','disabled','normal','disabled','Gainsboro','Gainsboro','salmon','Gainsboro'
                
                if ko==1:
                    A1.destroy()
                    A2.destroy()
                    A3.destroy()
                    A4.destroy()
                    A5.destroy()
                    A6.destroy()
                    A7.destroy()
                    A8.destroy()
                        
                A1=Radiobutton(fen,text="Décimal",selectcolor=dicoNb[basedep][4],state=dicoNb[basedep][0], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
                A2=Radiobutton(fen,text="Binaire",selectcolor=dicoNb[basedep][5],state=dicoNb[basedep][1], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
                A3=Radiobutton(fen,text="Hexadécimal",selectcolor=dicoNb[basedep][6],state=dicoNb[basedep][2], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
                A4=Radiobutton(fen,text="Octal",selectcolor=dicoNb[basedep][7],state=dicoNb[basedep][3], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
                
                A5=Radiobutton(fen,text="Décimal",selectcolor=dicoNb[basearr][4],state=dicoNb[basearr][0], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
                A6=Radiobutton(fen,text="Binaire",selectcolor=dicoNb[basearr][5],state=dicoNb[basearr][1], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
                A7=Radiobutton(fen,text="Hexadécimal",selectcolor=dicoNb[basearr][6],state=dicoNb[basearr][2], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
                A8=Radiobutton(fen,text="Octal",selectcolor=dicoNb[basearr][7],state=dicoNb[basearr][3], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')

                A1.grid(row = 10, column = 2)
                A2.grid(row = 11, column = 2)
                A3.grid(row = 12, column = 2)
                A4.grid(row = 13, column = 2)
                A5.grid(row = 10, column = 4)
                A6.grid(row =11, column = 4)
                A7.grid(row = 12, column = 4)
                A8.grid(row = 13, column = 4)

                if basedep==2:
                    entier=AleaExAll(2,1,32)
                if basedep==8:
                    entier=AleaExAll(8,1,10)
                if basedep==10:
                    entier=AleaExAll(10,1,10000)
                if basedep==16:
                    entier=AleaExAll(16,1,8)
                if ko==1:
                    Esaisie.destroy()
                Esaisie=Label(fen, text=entier , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
                Esaisie.grid(row=4, column=2,columnspan=3, rowspan=5, ipadx=200,ipady=10,sticky='s')
                return(basedep,basearr,entier)
            else:
                return(0,0,'')
        donne=alea(man,0)
        basedep=donne[0]
        basearr=donne[1]
        entier=donne[2]
        def RepEx1(donne):
            dico={}
            dico[2]='b'
            dico[8]='o'
            dico[16]='x'
            if donne[0] == 10:
                print(dico[donne[1]])
                rep=format(int(donne[2]),dico[donne[1]])
                rep=rep.upper()
            elif donne[1] == 10:
                rep=str(int(donne[2],donne[0]))
            else:
                rep=int(donne[2],donne[0])
                rep=format(rep,dico[donne[1]])
                rep=rep.upper()
            return(rep)

        #==================================Manuel===================    
        def get(basedep,basearr,entier,man):
            util = Résultats.get()
            util=util.upper()
            util=Raccourcir(util)
            if man==2:
                entier = Esaisie.get()
                entier = Raccourcir(entier)
                basedep=basedepart.get()
                basearr=basearrivee.get()
            if entier=='' or basearr==0 or basedep == 0 or util=='':
                messagebox.showerror(title="Information",
                            message="Erreur : Veuillez saisir toutes les valeurs")
                return 1
            Lmax={}
            Lmax[10]=5
            Lmax[2]=32
            Lmax[8]=10
            Lmax[16]=8
            entier=str(entier).upper()
            donnee=(basedep,basearr,entier)
            if  "." in entier or "." in util:
                
                        messagebox.showerror("showerror", "Veuillez saisir un entier ")
                        return(1)
            else:
                ok=CtrlSyntaxe(entier,basedep,1,Lmax[basedep])
                ok2=CtrlSyntaxe(util,basearr,1,Lmax[basearr])
                if ok==False:
                   messagebox.showerror(title="Information",
                            message="Erreur : La syntaxe de l'entier de départ est fausse.")
                   return 1
                elif ok2==False:
                   messagebox.showerror(title="Information",
                            message="Erreur : La syntaxe de la réponse est fausse.")
                   return 1
                elif basedep==basearr:
                    messagebox.showerror(title="Information",
                            message="Erreur : Problème dans la sélection des bases.")
                    return 1
                else:
                    rep=RepEx1(donnee)
                
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
                                        message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("".join(str(rep))))
                elif Verif == 0:
                   messagebox.showinfo(title="Information",
                                        message="Mauvaise réponse, réessayer !")
               
        #===========================INTERFACE===============================
        def back():   
            titre.destroy()
            soustitre.destroy()
            lab1.destroy()
            A1.destroy()
            A2.destroy()
            A3.destroy()
            A4.destroy()
            A5.destroy()
            A6.destroy()
            A7.destroy()
            A8.destroy()
            Esaisie.destroy()
            lab2.destroy()
            lab3.destroy()
            lab4.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Résultats.destroy()
            Chap1()
        def back2():   
            titre.destroy()
            soustitre.destroy()
            lab1.destroy()
            A1.destroy()
            A2.destroy()
            A3.destroy()
            A4.destroy()
            A5.destroy()
            A6.destroy()
            A7.destroy()
            A8.destroy()
            Esaisie.destroy()
            lab2.destroy()
            lab3.destroy()
            lab4.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Résultats.destroy()
            Menu()
            
        titre=Label(fen, text="Entiers non signées", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
        titre.grid(row=1, column=2,columnspan=3,ipady=30)
        soustitre=Label(fen, text="Quelques indications: Base 2 : maximum 32 bits Base 8 : maximum 10 symboles\n                    Base 10 : de 1 à 10000 Base 16 : maximum 8 symboles", font=("courier", 15), fg='blue4', bg='lightskyblue1') 
        soustitre.grid(row=2, column=2,columnspan=4,sticky='w') 

        #Création de menu déroulant d'entrée
        lab1=Label(fen,text="Valeur à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
            lab1.grid(row=4, column=2,columnspan=3, rowspan=2, sticky='s')   #Créé du texte Label(text=''), spécifie la fenêtre concernée, donne une couleur de fond (bg='') et le place dans la fenêtre avec .pack()
        elif man==1:
            lab1.grid(row=3, column=2,columnspan=3, sticky='s')

        if man==2:
            global Esaisie
            global A1
            global A2
            global A3
            global A4
            global A5
            global A6
            global A7
            global A8
            #Définit une variable utilisable dans tout le programme
            Esaisie=Entry(fen)                              #Créé une entrée que l'utilisateur pourra remplir de texte et spécifie la fenêtre concernée
            Esaisie.grid(row=6, column=2,columnspan=3, rowspan=2, ipadx=200,ipady=10,sticky='s')                       
            Esaisie.focus()                                 #focus() permet ici de placer directement le curseur à l'intérieur de la zone de texte
            #Esaisie.insert(INSERT, 'Mettez la valeur à convertir en respectant les contraintes')      #Insert dans la saisie le texte entre guillemets
            Esaisie.selection_range(0, END)                 #Sélectionne le contenu entier de la saisie


            basedepart=IntVar()
            basearrivee=IntVar()#Définit une variable utilisée pour les Radiobuttons
            #Radiobutton créé un bouton qui permet un choix. Il prend comme paramètres un texte, une couleur de fond, une variable et sa valeur. En plus indicatoron change son aspect, width sa largeur, cursor le curseur et activebackground sa couleur quand "cliqué"

            A1=Radiobutton(fen,text="Décimal", fg='#103985', bg='Gainsboro',variable=basedepart,value=10,indicatoron=0,width=26, height=2, cursor='hand2')
            A2=Radiobutton(fen,text="Binaire", fg='#103985', bg='Gainsboro',variable=basedepart,value=2,indicatoron=0,width=26, height=2, cursor='hand2')
            A3=Radiobutton(fen,text="Hexadécimal", fg='#103985', bg='Gainsboro',variable=basedepart,value=16,indicatoron=0,width=26, height=2, cursor='hand2')
            A4=Radiobutton(fen,text="Octal", fg='#103985', bg='Gainsboro',variable=basedepart,value=8,indicatoron=0,width=26, height=2, cursor='hand2')

            A5=Radiobutton(fen,text="Décimal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=10,indicatoron=0,width=26, height=2, cursor='hand2')
            A6=Radiobutton(fen,text="Binaire", fg='#103985', bg='Gainsboro',variable=basearrivee,value=2,indicatoron=0,width=26, height=2, cursor='hand2')
            A7=Radiobutton(fen,text="Hexadécimal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=16,indicatoron=0,width=26, height=2, cursor='hand2')
            A8=Radiobutton(fen,text="Octal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=8,indicatoron=0,width=26, height=2, cursor='hand2')

            A1.grid(row = 10, column = 2)
            A2.grid(row = 11, column = 2)
            A3.grid(row = 12, column = 2)
            A4.grid(row = 13, column = 2)
            A5.grid(row = 10, column = 4)
            A6.grid(row =11, column = 4)
            A7.grid(row = 12, column = 4)
            A8.grid(row = 13, column = 4)



        lab2=Label(fen,text="Base de départ", font=("courier", 17), fg='black', bg='lightskyblue1')
        lab2.grid(row=9, column=2)

        lab3=Label(fen,text="Base d'arrivée", font=("courier", 17), fg='black', bg='lightskyblue1')
        lab3.grid(row = 9, column =4)

        lab4=Label(fen,text="Résultats", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        lab4.grid(row = 13, column = 2, pady=3, columnspan=3, rowspan=2)
        Résultats=Entry(fen) # Création de la zone de résultats
        Résultats.grid(row = 15, column = 2, columnspan=3, ipadx=200, ipady=10)
        Résultats.selection_range(0, END)
        #====================================
        def nouveau(man):
            B2['state']='disabled'
            B3['state']='normal'
            if man==2:
                Esaisie.delete(0,END)
                A1.deselect()
                A2.deselect()
                A3.deselect()
                A4.deselect()
                A5.deselect()
                A6.deselect()
                A7.deselect()
                A8.deselect()
            Résultats.delete(0,END)
            alea(man,1)
            
            
        ##img1=PhotoImage(file="img1.gif")
        ##imag=PhotoImage(file="imag.gif")

        def create():
            rappel = Toplevel(fen, background="lightskyblue1")
            #rappel.config(background="lightskyblue1")
            Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1').grid(row=1, column=1, columnspan=3)

            Label(rappel, text="Dans un système en base X, il faut X symboles différents pour représenter les chiffres de 0 à X-1", font=("Courier", 16), fg='blue4', bg='lightskyblue1').grid(row=2, column=1,columnspan=3,ipady=40)
            ##Label(rappel, image= img1).grid(row=3, column=1,columnspan=3)
        ##    
            i="De base 10 à base 2 :\n"
            a="méthode de la division ou méthode de la soustraction\n"
    
            Label(rappel, text=i, bg='lightskyblue1', fg='darkslateblue', font=('Courier',20,'bold')).grid(row=4, column=1, columnspan=3)                   
            Label(rappel, text=a, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=5, column=1, columnspan=3)
            #Label(rappel, image= img2).grid(row=4, column=2, columnspan=2) 
        ##    
            j="De base 2 à base 8 ou 16 :\n"
            c="méthode de la compression\n"                      
                                
            Label(rappel, text=j, bg='lightskyblue1', fg='darkslateblue', font=('Courier',20,'bold')).grid(row=6, column=1, columnspan=3)                  
            Label(rappel, text=c, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=7, column=1, columnspan=3)
        ##    
            k="De base 8 ou 16 à base 2 :\n"
            m="méthode de l’expansion\n"

            Label(rappel, text=k, bg='lightskyblue1', fg='darkslateblue', font=('Courier',20,'bold')).grid(row=8, column=1, columnspan=3)               
            Label(rappel, text=m, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=9, column=1, columnspan=3)
            #Label(rappel, image= img4).grid(row=7, column=2) 
        ##
            l="De base 8 à base 16 ou réciproquement :\n"
            o="passer par la base 2 en intermédiaire.\n"

            Label(rappel, text=l, bg='lightskyblue1', fg='darkslateblue', font=('Courier',20,'bold')).grid(row=10, column=1, columnspan=3)               
            Label(rappel, text=o, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=11, column=1, columnspan=3)
            ##Label(rappel, image= imag).grid(row=4, column=2, rowspan=8)  

            def exit_btn():

                rappel.destroy()
                rappel.update()

            btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
            btn.grid(row=12, column=1,columnspan=3,sticky='n')
            
            rappel.rowconfigure(1, weight=1)
            rappel.rowconfigure(2, weight=1)
            rappel.rowconfigure(3, weight=1)
            rappel.rowconfigure(4, weight=1)
            rappel.rowconfigure(5, weight=1)
            rappel.rowconfigure(6, weight=1)
            rappel.rowconfigure(7, weight=1)
            rappel.rowconfigure(8, weight=1)
            rappel.rowconfigure(9, weight=1)
            rappel.rowconfigure(10, weight=1)
            rappel.rowconfigure(11, weight=1)
            rappel.rowconfigure(12, weight=1)

            rappel.columnconfigure(1, weight=0)
            rappel.columnconfigure(2, weight=1)
            rappel.columnconfigure(3, weight=0)  

        B1=Button(fen, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2, command=create)
        #B1.grid(row=17, column=1)
        B2=Button(fen, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, command=lambda:(nouveau(man)))
        #B2.grid(row=17, column=2)
        B3=Button(fen, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, command=lambda:(get(basedep,basearr,entier,man)))
        #B3.grid(row=17, column=3)
        B5=Button(fen, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2, command= back2)
        #B4.grid(row=17, column=5)
        B4=Button(fen, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=back)
        #B5.grid(row=17, column=4)

        B1.grid(row=18, column=1)
        B2.grid(row=18, column=2)
        B3.grid(row=18, column=3)
        B4.grid(row=18, column=4)
        B5.grid(row=18, column=8)

        
#===================================================================================================================================================================================
#=========================================================================================
#===================== Chapitre 1 - Exercice 2 ===========================================
    
        
    #========================================================================
    #========================Données Aléatoires==============================
    #========================================================================
    def Binaire_aleaEx2():
        a = AleaExAll(2,2,16)
        b = AleaExAll(2,2,16)
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
        util=Raccourcir(util)

    #=====================================================================
    #========================Saisie Manuelle==============================
    #=====================================================================
    def getEntryM():
        global Entier1
        global Entier2
        global oper
        global util
        Entier1 = saisieB1.get()
        Entier1=Raccourcir(Entier1)
        
        oper = saisieOper.get()
        oper=Raccourcir(oper)
        
        Entier2 = saisieB2.get()
        Entier2=Raccourcir(Entier2)
        
        util = saisieRep.get()
        util=Raccourcir(util)
      
        return(Entier1, Entier2, oper, util)

    def Binaire_saisEx2(e1, e2, ope):

        if e1=='' or e2=='' or ope=='':
             messagebox.showerror("showerror", "Veuillez saisir toutes les valeurs")
             return(1)
        else:
            if "." in e1 or "." in e2 or "." in ope:
                messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                return(1)
            else:
                
                if not ope == '+' or ope == '-' or ope == 'x':
                    messagebox.showerror("showerror", "Mauvaise saisie du signe d'opération")
                    return(1)
                else:
                    
                    op = ope
                    ent1=CtrlSyntaxe(e1,2,1,16)
                    
                    if  ent1 == False:
                        messagebox.showerror("showerror", "Mauvaise saisie du Nombre binaire 1")
                        return(1)
                    else:    
                        a = e1
                        ent2=CtrlSyntaxe(e2,2,1,16)
                        if ent2 == True:
                            b = e2
                        else:
                            messagebox.showerror("showerror", "Mauvaise saisie du Nombre binaire 2")
                            return(1)
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
        saisieB1.config(text=sa[0])
        saisieOper.config(text=sa[2])
        saisieB2.config(text=sa[1])
        return(sa)
        
    def Valide(saisie, sa):
        global reponse
         
        if saisie == 1:
            util = saisieRep.get()
            print(util)
            if util=='':
                messagebox.showerror(title="showerror",
                                message="Veuillez saisir un résultat")
                return(1)
            else:
                if "." in util:
                     messagebox.showerror("showerror", "Erreur de syntaxe les points ne sont pas acceptés")
                     return(1)
                else:
                    
                    ok = CtrlSyntaxe(util,10,1,16,1,1111111111111111)
                    if ok==False:
                         messagebox.showerror(title="showerror",
                                        message="Erreur de syntaxte dans la saisie du résultat")
                         return(1)
                    else:
                       
                        reponse = RepExo2(sa[0],sa[1],sa[2])
                        print(reponse)
                        rep = VerifRep(reponse,util)
            
        elif saisie ==2:
            getEntryM()
            util = saisieRep.get()
            sais=Binaire_saisEx2(Entier1, Entier2, oper)
          
            if not sais==1:
                if "." in util:
                     messagebox.showerror("showerror", "Erreur de syntaxe les points ne sont pas acceptés")
                     return(1)
                else:
                    ok = CtrlSyntaxe(util,10,1,16,1,1111111111111111)
                    if ok==False:
                         messagebox.showerror(title="showerror",
                                        message="Erreur de syntaxte dans la saisie du résultat")
                         return(1)
                    else:
                        
                            reponse = RepExo2(sais[0],sais[1],sais[2])
                            rep = VerifRep(reponse,util)
                            ok=True
            else:
                ok=False
                return(1)
            
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
        f.rowconfigure(1, weight=0)
        f.rowconfigure(2, weight=0)
        f.rowconfigure(3, weight=1)
        f.rowconfigure(4, weight=1)
        f.rowconfigure(5, weight=1)
        f.rowconfigure(6, weight=1)
        f.rowconfigure(7, weight=1)
        f.rowconfigure(8, weight=1)
        f.rowconfigure(9, weight=1)
        f.rowconfigure(10, weight=1)
        f.rowconfigure(11, weight=1)
        f.rowconfigure(12, weight=1)
        f.rowconfigure(13, weight=1)
        f.rowconfigure(14, weight=1)
        f.rowconfigure(15, weight=1)
        f.rowconfigure(16, weight=1)
        f.rowconfigure(17, weight=1)
        f.rowconfigure(18, weight=1)


        f.columnconfigure(1, weight=1)
        f.columnconfigure(2, weight=1)
        f.columnconfigure(3, weight=1)
        f.columnconfigure(4, weight=1)
        f.columnconfigure(5, weight=0)
        f.columnconfigure(6, weight=1)
        f.columnconfigure(7, weight=1)
        f.columnconfigure(8, weight=1)
        f.columnconfigure(9, weight=1)
        f.columnconfigure(10, weight=1)
        f.columnconfigure(11, weight=1)
        f.columnconfigure(12, weight=1)
        
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
            Chap1()
        def back2():   
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
            Menu()
   
        largeur = 25
        hauteur = 2

        tExo2 = Label(f, text= "Opérations en binaire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExo2.grid(row=1, column = 2, columnspan=3)
                        
        st=Label(f, text="Quelques Indications: Les entrées des données ne peuvent pas\n excéder 16 bits ", font=("courier", 20, "italic"), fg='darkblue', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        st.grid(row=2, column=1,columnspan=4,ipady=50,ipadx=50)
            
        txt1=Label(f, text="Nombre Binaire 1 : ", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        txt1.grid(row=4,column=1,columnspan=2,sticky='nsew',ipady=10)
        

        if saisie==2:
            
            saisieB1=Entry(f)
        else:
            saisieB1=Label(f, text="", font=("courier",15, "italic"), fg='black', bg='white',width=10, height=1)
            
        saisieB1.grid(row=4, column=3,ipadx=200,columnspan=4,ipady=10)

        txt2=Label(f, text="Choix d'opération : \n(+,- ou x) ", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        txt2.grid(row=6, column=1,columnspan=2,sticky='nsew',ipady=10)

        if saisie==2:
            
            saisieOper=Entry(f)
        else:
            saisieOper=Label(f, text="", font=("courier",15, "italic"), fg='black', bg='white',width=10, height=1)

        saisieOper.grid(row=6, column=3,ipadx=200,columnspan=4,ipady=10)

        txt3=Label(f, text="Nombre binaire 2 : ", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        txt3.grid(row=8, column=1,columnspan=2,sticky='nsew',ipady=10)
                      
    
        
        if saisie==2:
            saisieB2=Entry(f)
        else:
            saisieB2=Label(f, text="", font=("courier",15, "italic"), fg='black', bg='white',width=10, height=1)

        saisieB2.grid(row=8, column=3,ipadx=200,columnspan=4,ipady=10)

        txt4=Label(f, text="Résultat:          ", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        txt4.grid(row=10,column=1,columnspan=2,sticky='nsew',ipady=10)
        
        saisieRep=Entry(f)
        saisieRep.grid(row=10, column=3,ipadx=200,columnspan=4,ipady=10)
        

        if saisie == 1:
            sa=AleaValeur()
        else:
            sa=[]
            
        w=20
        h=2
        y=3
        x=10

        B1=Button(f, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2, command=lambda:create(f))
        B1.grid(row=18, column=1)
        B2=Button(f, text="Nouveau", state='disabled', font=("bold", 18, "italic"), fg='white', bg='#103985',width=15, height=2, command=lambda:Nouveau(saisie,fenetre))
        B2.grid(row=18, column=2)
        B3=Button(f, text="Valider", font=("courier", 18, "bold"), fg='white', bg='#103985',width=15, height=2, command=lambda:Valide(saisie, sa))
        B3.grid(row=18, column=3)
        B5=Button(f, text="Menu", font=("courier", 18, "bold"), fg='white', bg='grey',width=15, height=2, command=back2)
        B4=Button(f, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985',  width=15, height=2, command=back)
        B4.grid(row=18, column=4)
        B5.grid(row=18, column=5)



    #===========================================================
    #========= Reset de l'exo 2 ==================================
    #===========================================================

    def Nouveau(saisie,fenetre):
        B3['state']='normal'
        B2['state']='disabled'

        if saisie==2:
            saisieB1.delete(0,END)
            saisieOper.delete(0,END)
            saisieB2.delete(0,END)
            saisieRep.delete(0,END)
               #effacer ce qui a été entré
        else:
            
            saisieRep.delete(0,END)
            
            sa= Binaire_aleaEx2()
            saisieB1.config(text=sa[0])
            saisieOper.config(text=sa[2])
            saisieB2.config(text=sa[1])
        
     
    #=========================================================================
    #================= Page rappel exo2 ===========================================
    #=========================================================================

    def create(f):
        rappel = Toplevel(f)
        rappel.config(background="lightskyblue1")
        titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        titre.grid(row=1, column=2,columnspan=3,sticky='s')

        txt1=Label(rappel, text="N'oubliez pas que : 1 + 1 = 10", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
        txt2=Label(rappel, text="N'oubliez pas les retenues", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
        

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

        btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
        btn.grid(row=6, column=2,columnspan=3,sticky='n')

    
#===================================================================================================================================================================================
#==========================================================================================
#===================== Chapitre 1 - Exercice 3 ============================================
    def Exercice3(f):
        fenetre=f
        fenetre.config(background='lightskyblue1')
        fenetre.rowconfigure(1, weight=0)
        fenetre.rowconfigure(2, weight=0)
        fenetre.rowconfigure(3, weight=1)
        fenetre.rowconfigure(4, weight=1)
        fenetre.rowconfigure(5, weight=1)
        fenetre.rowconfigure(6, weight=1)
        fenetre.rowconfigure(7, weight=1)
        fenetre.rowconfigure(8, weight=1)
        fenetre.rowconfigure(9, weight=1)
        fenetre.rowconfigure(10, weight=1)
        fenetre.rowconfigure(11, weight=1)
        fenetre.rowconfigure(12, weight=1)
        fenetre.rowconfigure(13, weight=1)
        fenetre.rowconfigure(14, weight=1)
        fenetre.rowconfigure(15, weight=1)
        fenetre.rowconfigure(16, weight=1)
        fenetre.rowconfigure(17, weight=1)
        fenetre.rowconfigure(18, weight=1)


        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, weight=1)
        fenetre.columnconfigure(3, weight=1)
        fenetre.columnconfigure(4, weight=1)
        fenetre.columnconfigure(5, weight=0)
        fenetre.columnconfigure(6, weight=1)
        fenetre.columnconfigure(7, weight=1)
        fenetre.columnconfigure(8, weight=1)
        fenetre.columnconfigure(9, weight=1)
        fenetre.columnconfigure(10, weight=1)
        fenetre.columnconfigure(11, weight=1)
        fenetre.columnconfigure(12, weight=1)
        
        #===================================================================================================================
        #=======================================FONCTIONS D'EXERCICE 3
        #====================================================================================================================
        def AleaEx3(choix,n,mini,maxi):
            
            #Donne des nombres binaires aléatoires
            ch = '1'        
            if choix == 'quelconque':
                taille = randint(mini,maxi)
                for i in range(taille):
                    a=randint(0,1)
                    ch+=str(a)
            elif choix == 'correct':
                taille = randint(min(mini, n+1), maxi)
                for i in range(taille-n):
                    a=randint(0,1)
                    ch+=str(a)
                ch+='0'*n # += erreur 
            return(ch)

        #=======================================================================================================================
        def List(n):
            liste=[]
            #Crée une liste avec des nombres binaires aléatoires 
            for i in range(7): #génère des nombres binaires aléatoires 
                liste.append(AleaEx3('quelconque',n,1,30))
            for i in range(3):#pour avoir au moins 3 réponses correctes
                liste.append(AleaEx3('correct',n,1,30))
            shuffle(liste) #permet de bien mélanger les suggestions
            return(liste)
        #========================================================================================================================
        def Valid():
            lprop=my_listbox.get('@1,0', END)

            x=[]
            x=t2.get('@1,0', END)
            n=x[3:]
            n=int(n)
            
            #============================Liste des réponses correctes
            def ReponseEx3(lprop, n):
                RepEx3=[]                   #Récupère les bonnes réponses
                seq='0'*n
                for i in lprop:
                    if i[-n:]==seq:         #Remplace le calcul(if int(i,2)% (2**n) == 0:)
                        RepEx3.append(i)
                print(RepEx3)
                    #print(" Mauvaise réponse, vous avez perdu !\n Le résultat est:" + [RepEx3])
                return(RepEx3)

            #============================Liste des réponses d'utilisateur
            def Recup():                    #Récupère les réponses d'utilisateurs
                UtilEx3=[]
                selected_item = StringVar() # on crée une variable StringVar() pour stocker la valeur de l'item sélectionné
                item= my_listbox.curselection() #tous les reponses selectionnées
                for i in item:
                    selected_item = my_listbox.get(i) #pour les récuperer
                    UtilEx3.append(selected_item)
                print(UtilEx3)
                #pour les ajouter à la liste des reponses d'utilisateurs
                
            
                #selected_item.set(UtilEx3)
                #on affecte la valeur de l'item à la variable
                #cela affiche les valeur selectionné sur l'unterface

            #===============================Vérification de la Réponse d'utilisateur
                if UtilEx3==[]:
                   
                    return(1)

                else:
                    
                     return(UtilEx3)
            
            if not Recup()==1:
                vérif = VerifRep(ReponseEx3(lprop, alea),Recup())
           
            #================================Validation Rep
                global resu
                        
                #a=" Mauvaise réponse, vous avez perdu !\n Le résultat est: \n"      
                if vérif == 1:
                    B3['state']='disabled' #bloquer le bouton valider ==> Gagner
                    B2['state']='normal'
                    messagebox.showinfo(title="Information",
                                        message="Bonne Réponse, Bravo !! ")
                   
                elif vérif == -1:
                    B3['state']='disabled' #bloquer le bouton valider ==> Perdu
                    B2['state']='normal'
                    messagebox.showinfo(title="Information",
                                        message=" Mauvaise réponse, vous avez perdu !\n Le résultat est: \n" +("\n".join(ReponseEx3(lprop, alea)))) 
                elif vérif == 0:
                    messagebox.showinfo(title="Information",
                                        message="Mauvaise réponse!")#resu=Label(cadre1, text="Mauvaise réponse, réessayer ! ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
                    #resu.pack(pady= 5, side=TOP)
            else:
                messagebox.showinfo(title="Information",
                                        message="Veuillez sélectionnez au moins 3 réponses ")
            
        #========= Rappel fenetre ==================================
        #===========================================================
        def create():
            rappel = Toplevel(fenetre)
            rappel.config(background="lightskyblue1")
            titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
            titre.grid(row=1, column=2,columnspan=3,sticky='s')

            txt1=Label(rappel, text="Si un entier est multiple d'une puissance (n) de 2 :", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=60, height=2)
            txt2=Label(rappel, text="Il doit se terminer par (n) 0.", font=("courier", 16, "italic"), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
            
            txt1.grid(row=2, column=2, columnspan=4)
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

            btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
            btn.grid(row=6, column=2,columnspan=3,sticky='n')
        #========================================================
        #======== Back ==========================================
        #========================================================
        def back():
            titre.destroy()
            txt1.destroy()
            txt2.destroy()
            t2.destroy()
            txt3.destroy()
            my_listbox.destroy()
            select.destroy()
            delet.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Chap1()
        def back2():
            titre.destroy()
            txt1.destroy()
            txt2.destroy()
            t2.destroy()
            txt3.destroy()
            my_listbox.destroy()
            select.destroy()
            delet.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Menu()
        #=============================================================================================================================================#
                                                        #INTERFACE GRAFIQUE#
        #=============================================================================================================================================#        
        #====================================cadre1
        titre=Label(fenetre, text="Multiplicité en binaire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
        titre.grid(row=1, column=2,columnspan=3) # Placement de l'invite


        #===================================cadre2
        txt1=Label(fenetre, text="QUESTION: Cochez les bonnes réponses", font=("courier", 20, "bold"), fg='black', bg='lightskyblue1')
        txt1.grid(row=2, column=2,columnspan=3,ipady=40)
        #choix aleatoire de la puissance de 2
        
        txt2=Label(fenetre, text="Puissance de 2    ", font=("courier", 25), fg='black', bg='lightskyblue1')
        txt2.grid(row=4,column=1,columnspan=2,ipady=10) # Placement de la zone de saisie
        
        t2 = Text(fenetre,  font=("courier", 15), height = 1, width = 25)
        t2.grid(row=4, column=3,ipadx=100,columnspan=4,ipady=10)
        ch=""
        syn='puissanceExp'
        alea=AleaExAll('puissanceExp',1, 20)
        ch = '2**'+str(alea)
        t2.insert(END, ch)

        #choix aleatoire d'entiers binaire
        txt3=Label(fenetre, text="Entiers en binaire", font=("courier", 25), fg='black', bg='lightskyblue1')
        txt3.grid(row=5, column=1,columnspan=2)

        my_listbox=Listbox(fenetre,font=("courier", 15), width=25, selectmode = MULTIPLE) #(yscrollcommand = my_scrollbar.set, )
        #my_scrollbar.config(command = my_listbox.yview) 
        #my_scrollbar.pack(side = RIGHT, fill=Y)         
        my_listbox.grid(row=5, column=3,ipadx=100,columnspan=4,ipady=10)                

        lprop=List( alea) 
        my_list = lprop

        for i in my_list:
            my_listbox.insert(END, i)


        def select():
            for i in range (10):
                my_listbox.select_set(i)

        select= Button(fenetre, text="selectionner tous", width=5, height=1, command = select)
        select.grid(row=7, column=2,ipadx=100,columnspan=4,ipady=10)

        def delet():
            for i in range (10):
                my_listbox.select_clear(i)

        delet= Button(fenetre, text="supprimer", width=5, height=1, command =delet)
        delet.grid(row=7, column=4,ipadx=100,columnspan=4,ipady=10)

        def Nouveau ():
            global ch
            B3['state']='normal'
            B2['state']='disabled'
            ####Gestion Puissance de 2
            t2.delete('1.0',END)
            alea=AleaExAll('puissanceExp',1, 20)
            ch='2**'+str(alea)
            t2.insert(END,ch)
            ### Gestion liste box
            my_listbox.delete(0,END)
            global lprop
            lprop=List(alea)
            global my_list
            my_list=lprop
            for i in my_list:
                my_listbox.insert(END, i)
            
            
        #======================Cadre 3
        B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())
        B2=Button(fenetre, text="Nouveau",state="disabled",font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Nouveau())
        B3=Button(fenetre, text="Valider",command=Valid, font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
        B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2, command=back2)
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2, command= back)
         

        B1.grid(row=18, column=1)
        B2.grid(row=18, column=2)
        B3.grid(row=18, column=3)
        B4.grid(row=18, column=8)
        B5.grid(row=18, column=4)
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
        fenetre.rowconfigure(7, weight=1)
        fenetre.rowconfigure(8, weight=1)
        fenetre.rowconfigure(9, weight=1)
        fenetre.rowconfigure(10, weight=1)
        fenetre.rowconfigure(11, weight=1)
        fenetre.rowconfigure(12, weight=1)
        fenetre.rowconfigure(13, weight=1)
        fenetre.rowconfigure(14, weight=1)
        fenetre.rowconfigure(15, weight=1)
        fenetre.rowconfigure(16, weight=1)
        fenetre.rowconfigure(17, weight=1)
        fenetre.rowconfigure(18, weight=1)


        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, weight=1)
        fenetre.columnconfigure(3, weight=1)
        fenetre.columnconfigure(4, weight=1)
        fenetre.columnconfigure(5, weight=0)
        fenetre.columnconfigure(6, weight=1)
        fenetre.columnconfigure(7, weight=1)
        fenetre.columnconfigure(8, weight=1)
        fenetre.columnconfigure(9, weight=1)
        fenetre.columnconfigure(10, weight=1)
        fenetre.columnconfigure(11, weight=1)
        fenetre.columnconfigure(12, weight=1)

        

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
                util=res.get()
                util=Raccourcir(util)
                ctl=control(op,ch,p,util)
                
                if not ctl==1:
                    rep=repEx4(ch,p,op)
                    verif=VerifRep(rep,util)
                    if verif==0:
                        #res1="Réessayer"
                        messagebox.showerror("showerror", "Mauvaise réponse, veuillez réessayer")
                        
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
                    
     
            
            txt1=Label(fenetre, text="   Type d'opération", font=("courier", 22, "italic"), fg='black', bg='lightskyblue1')
            oper=Entry(fenetre) 

            txt2=Label(fenetre, text="   Nombre Binaire ", font=("courier", 22, "italic"), fg='black', bg='lightskyblue1')
            nbbin=Entry(fenetre) 

            txt3=Label(fenetre, text="   Puissance en base de 2 ", font=("courier", 22, "italic"), fg='black', bg='lightskyblue1')
            puis=Entry(fenetre) 

            txt4=Label(fenetre, text="   Résultat", font=("courier", 22, "italic"), fg='black', bg='lightskyblue1')
            res=Entry(fenetre)  

        #==============================================================================================================
        #=====================================Manuel===================================================================
        #==============================================================================================================

        else:
            
            #========================Saisie Manuelle==============================
           
            def Exo4():
                op=oper.get()
                op=Raccourcir(op)
                ch=nbbin.get()
                ch=Raccourcir(ch)
                p=(puis.get())
                p=Raccourcir(str(p))
                verif=2
                base=[2,10]
                util=res.get()
                util=Raccourcir(util)

                ctl=control(op,ch,p,util)
                
                
                if not ctl==1:
                    p=int(puis.get())
                    p=Raccourcir(str(p))
                    rep=repEx4(ch,int(p),op)
                    verif=VerifRep(rep,util)
                    if verif==0:
                        messagebox.showerror("showerror", "Mauvaise réponse, veuillez réessayer")

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
            txt1=Label(fenetre, text="   Type d'opération", font=("courier", 22, "italic"), fg='black', bg='lightskyblue1')
            oper=Entry(fenetre) 

            txt2=Label(fenetre, text="   Nombre Binaire ", font=("courier", 22, "italic"), fg='black', bg='lightskyblue1')
            nbbin=Entry(fenetre) 

            txt3=Label(fenetre, text="   Puissance en base de 2 ", font=("courier", 22, "italic"), fg='black', bg='lightskyblue1')
            puis=Entry(fenetre) 

            txt4=Label(fenetre, text="   Résultat", font=("courier", 22, "italic"), fg='black', bg='lightskyblue1')
            res=Entry(fenetre) 
        #===========================================================
        #========= Contrôle =========================================
        #===========================================================
        def control(oper,nbbin,puis,util):
            ok=True
            op=['*','/']

            if man==1:
                if "." in util or "." in nbbin or "." in puis or "." in oper:
                     messagebox.showerror("showerror", "Erreur de syntaxe les points ne sont pas acceptés")
                     return(1)
                else:
                    
                    if oper=='' or nbbin==''or puis==''or util=='':
                        ok=False
                        messagebox.showerror("ATTENTION!","Veuillez saisir toute les valeurs")
                        return(1)
                    else:
            
                        if oper not in op:
                            ok=False
                            messagebox.showerror("ATTENTION !", "Operation : Mettre '*' ou '/'")
                            return(1)
                        else:
                            if not CtrlSyntaxe(nbbin,2,1,16):
                                ok=False
                                messagebox.showerror("ATTENTION !", "Mauvaise saisie du nombre binaire")
                                return(1)
                            else:
                                if not CtrlSyntaxe(puis,10,1,10,1,8):
                                    ok=False
                                    messagebox.showerror("ATTENTION !", "Mauvaise saisie de l'exposant")
                                    return(1)
                                else:                
                                    if not CtrlSyntaxe(util,2,1,35):
                                        ok=False
                                        messagebox.showerror("ATTENTION !", "Vérifier la syntaxe de votre résultat.")
                                        return(1)
                                
            elif man==2:
                if "." in util :
                     messagebox.showerror("showerror", "Erreur de syntaxe dans votre réponse les points ne sont pas acceptés")
                     return(1)
                else:
                    if util=='':
                        ok=False
                        messagebox.showerror("ATTENTION!","Veuillez saisir un résultat")
                        return(1)
                    else:
                         ctrlR=CtrlSyntaxe(util,2,1,35)
                         if ctrlR==False:
                             messagebox.showerror("ATTENTION !", "Vérifier la syntaxe de votre résultat.")
                             return(1)

        #===========================================================
        #========= Rappel fenetre ==================================
        #===========================================================
        def create():
            rappel = Toplevel(fenetre)
            rappel.config(background="lightskyblue1")
            titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
            titre.grid(row=1, column=2,columnspan=3,sticky='s')

            txt1=Label(rappel, text="Multiplication :", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
            txt2=Label(rappel, text="Ajouter des 0 à la fin du nombre en base 2 donné", font=("courier", 16, "italic"), fg='darkslateblue', bg='lightskyblue1',width=60, height=2)
            txt3=Label(rappel, text="Division : ", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg= 'lightskyblue1',width=40, height=2)
            txt4=Label(rappel, text="Supprimer des 0 à la fin du nombre en base 2  donné", font=("courier", 16, "italic"), fg='darkslateblue', bg='lightskyblue1',width=60, height=2)

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

        #======================================================================
        #========================= Back =======================================
        #======================================================================
        def back():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            txt2.destroy()
            txt3.destroy()
            txt4.destroy()
            oper.destroy()
            nbbin.destroy()
            puis.destroy()
            res.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Chap1()
        def back2():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            txt2.destroy()
            txt3.destroy()
            txt4.destroy()
            oper.destroy()
            nbbin.destroy()
            puis.destroy()
            res.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Menu()
       
        titre=Label(fenetre, text="Opération sans calcul", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')  
        titre.grid(row=1, column=2,columnspan=3) 

        soustitre=Label(fenetre, text="Quelques indications :Base 2 => maximum 16 bits en entrée Base 10 => entre 2 et 256 en puissance de 2\nDivision =>Le nombre en base 2 doit se terminer par au moins autant de 0 que l’exposant de la puissance de 2", font=("Courier", 15, "italic"), fg='blue4', bg='lightskyblue1')
        soustitre.grid(row=2, column=1,columnspan=5,ipady=30) 

        txt1.grid(row=5, column=1,columnspan=2,sticky='w',ipady=30)
        oper.grid(row=5,column=2,ipadx=200,columnspan=4,ipady=10) # Placement de la zone de saisie
        
        txt2.grid(row=7, column=1,columnspan=2,sticky='w')
        nbbin.grid(row=7, column=2,ipadx=200,columnspan=4,ipady=10)
        
        txt3.grid(row=9, column=1,columnspan=2,sticky='w',ipady=30)
        puis.grid(row=9, column=2,ipadx=200,columnspan=4,ipady=10)
        
        txt4.grid(row=11,column=1,columnspan=2,sticky='w',ipady=30)
        res.grid(row=11, column=2,ipadx=200,columnspan=4,ipady=10)

            
        B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())
        B2=Button(fenetre, text="Nouveau",font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Nouveau(), state='disabled')
        B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Exo4())
        B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2, command= back2)
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=back)
         

        B1.grid(row=18, column=1)
        B2.grid(row=18, column=2)
        B3.grid(row=18, column=3)
        B4.grid(row=18, column=5)
        B5.grid(row=18, column=4)

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
        fenetre.rowconfigure(7, weight=1)
        fenetre.rowconfigure(8, weight=1)
        fenetre.rowconfigure(9, weight=1)
        fenetre.rowconfigure(10, weight=1)
        fenetre.rowconfigure(11, weight=1)
        fenetre.rowconfigure(12, weight=1)
        fenetre.rowconfigure(13, weight=1)
        fenetre.rowconfigure(14, weight=1)
        fenetre.rowconfigure(15, weight=1)
        fenetre.rowconfigure(16, weight=1)
        fenetre.rowconfigure(17, weight=1)
        fenetre.rowconfigure(18, weight=1)


        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, weight=1)
        fenetre.columnconfigure(3, weight=1)
        fenetre.columnconfigure(4, weight=1)
        fenetre.columnconfigure(5, weight=0)
        fenetre.columnconfigure(6, weight=1)
        fenetre.columnconfigure(7, weight=1)
        fenetre.columnconfigure(8, weight=1)
        fenetre.columnconfigure(9, weight=1)
        fenetre.columnconfigure(10, weight=1)
        fenetre.columnconfigure(11, weight=1)
        fenetre.columnconfigure(12, weight=1)

        formats=AleaFormat5(lis)
        entier=AleaEnt5()

        #======================================================================
        #========================= Back =======================================
        #======================================================================
        def back():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            formatsAl.destroy()
            txt2.destroy()
            val.destroy()
            signe.destroy()
            positif.destroy()
            negatif.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Chap1()
        def back2():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            formatsAl.destroy()
            txt2.destroy()
            val.destroy()
            signe.destroy()
            positif.destroy()
            negatif.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Menu()

        titre=Label(fenetre, text="Déterminer le signe d'un entier", font=("Courier", 30, "italic"), fg='black', bg='lightskyblue1')  # Placement de l'invite

        soustitre=Label(fenetre, text="     Quelques Indications: voir Rappel ", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

        txt1=Label(fenetre, text="   Formats", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')

        formatsAl=Label(fenetre, text=formats, font=("courier", 20, "italic"), fg='black', bg='white',width=10, height=1)


        txt2=Label(fenetre, text=" Valeur", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')

        val=Label(fenetre, text=entier, font=("courier", 20, "italic"), fg='black', bg='white',width=4, height=1)

        choix=IntVar()

        signe=Label(fenetre, text="   Signe de\n  l'entier", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        positif=tk.Radiobutton(fenetre, text="Positif",font=("courier", 25), variable=choix, value=1,fg='black', bg='lightskyblue1',activebackground="lightskyblue1")
        negatif=tk.Radiobutton(fenetre, text="Négatif", font=("courier",25),variable=choix, value=2,fg='black', bg='lightskyblue1',activebackground="lightskyblue1")

        def nouveau():
            
            formats=AleaFormat5(lis)
            entier=AleaEnt5()
            B3['state']='normal'
            B2['state']='disabled'
            formatsAl.config(text=formats)
            val.config(text=entier)
         
        def RepUtil():
                ch=choix.get() # on récupère la valeur de val, donc de la case sélectionnée
                print(ch)
                if ch==0:
                        messagebox.showinfo(title="Information",
                                        message="Veuillez cocher une case ")
                        return(1)
                else:
                    
                    if ch==1:
                        util="positif"
                    elif ch==2:
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

            txt1=Label(rappel, text="L’entier ne peut pas excéder 16 bits", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
            txt2=Label(rappel, text="Dans cet exercice, une seule tentative ", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
            txt3=Label(rappel, text="sera accordée à l’utilisateur", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg= 'lightskyblue1',width=40, height=2)
            txt4=Label(rappel, text="", font=("courier", 25, "italic"), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)

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
         
        B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2,command=back2)
         
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=back)

        titre.grid(row=1, column=2, columnspan=3, ipady=40)
        soustitre.grid(row=2, column=1, columnspan=5, ipady=40)

        txt1.grid(row=3, column=1,ipady=40, columnspan=2)
        formatsAl.grid(row=3, column=3, ipadx=200, columnspan=5, ipady=10)

        txt2.grid(row=4, column=1, columnspan=2)
        val.grid(row=4, column=3, ipadx=250, columnspan=5, ipady=10)

        signe.grid(row=5, column=1, ipady=40, columnspan=2)
        positif.grid(row=5, column=2,columnspan=3)
        negatif.grid(row=5, column=4,columnspan=5)




        #bouton#
        B1.grid(row=18, column=1)
        B2.grid(row=18, column=2)
        B3.grid(row=18, column=3)
        B4.grid(row=18, column=7)
        B5.grid(row=18, column=4)

#===================================================================================================================================================================================
#=========================================================================================
#===================== Chapitre 1 - Exercice 5b ===========================================

    def Exercice5b(f,select):
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
        fenetre.rowconfigure(9, weight=1)
        fenetre.rowconfigure(10, weight=1)
        fenetre.rowconfigure(11, weight=1)
        fenetre.rowconfigure(12, weight=1)
        fenetre.rowconfigure(13, weight=1)
        fenetre.rowconfigure(14, weight=1)
        fenetre.rowconfigure(15, weight=1)
        fenetre.rowconfigure(16, weight=1)
        fenetre.rowconfigure(17, weight=1)
        fenetre.rowconfigure(18, weight=1)


        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, weight=1)
        fenetre.columnconfigure(3, weight=1)
        fenetre.columnconfigure(4, weight=1)
        fenetre.columnconfigure(5, weight=0)
        fenetre.columnconfigure(6, weight=1)
        fenetre.columnconfigure(7, weight=1)
        fenetre.columnconfigure(8, weight=1)
        fenetre.columnconfigure(9, weight=1)
        fenetre.columnconfigure(10, weight=1)
        fenetre.columnconfigure(11, weight=1)
        fenetre.columnconfigure(12, weight=1)

        man=select

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
                        util=Raccourcir(util)
                        
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
                        basedep=Raccourcir(basedep)
                        
                        basearriv=fenetre.menua.get()
                        basearriv=Raccourcir(basearriv)
                        
                        entier=Val.get()
                        entier=Raccourcir(entier)
                        
                        Bits=Nb.get()
                        Bits=Raccourcir(Bits)
                        
                        util=Resultats.get()
                        util=Raccourcir(util)

                else :
                        
                        basedep=menuD.get()
                        basedep=Raccourcir(basedep)
                        
                        entier=Val.get()
                        entier=Raccourcir(entier)
                        
                        basearriv=menuA.get()
                        basearriv=Raccourcir(basearriv)
                        
                        Bits='Appuyer sur Go'
                        util=Resultats.get()
                        util=Raccourcir(util)
                        
                        bit=Nb.get()
                        bit=Raccourcir(bit)

                   
                print("ici la base de départ",basedep)
                print("voici la base arrive",basearriv)
                
                if basedep=="SVA" or basedep=="C2":
                        
                        if "." in entier or "." in util :
                                messagebox.showerror("showerror", "Erreur de syntaxe les points ne sont pas acceptés")
                                return(1)
                        else:
                            
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
                        
                        if "." in entier or "." in util or "." in Bits:
                            
                                messagebox.showerror("showerror", "Erreur de syntaxe les points ne sont pas acceptés")
                                return(1)
                        else:
                            
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
                        based=Raccourcir(based)
                        
                        basea=menuA.get()
                        basea=Raccourcir(basea)
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
                        Val['state']='readonly'
                        Nb.configure(state="readonly")
                        menuD.configure(state="readonly")
                        menuA.configure(state="readonly")
                       
                        
                        
                
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
                                menuD.config(state='disabled')
                                menuA.config(state='disabled')
                                
                         
                        

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

                menuD.config(state='normal')
                menuA.config(state='normal')
                
            elif man==1:
               
                based=AleaFormatBi5(Li)
                basea=AleaFormatBis5(based)
              
                Resultats.delete(0,END)
                
                Val['state']='normal'
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

        soustitre=Label(fenetre, text="Quelques Indications: valeur 1000000000 impossible à convertir\n Pour la base 10 uniquement des entiers                         \n    La valeur absolue doit être comprise entre 1-2^(n-1) et 2^(n-1)-1.", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

        txt1=Label(fenetre, text="   Format de départ", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
           
            fenetre.menud= tk.StringVar(fenetre)
            menuD = ttk.OptionMenu(fenetre,fenetre.menud,Li[0], *Li)
            
        else:
            menuD=Entry(fenetre,justify='center',borderwidth=3)
            menuD.insert(0, based)
            menuD.configure(state="readonly")


        txt2=Label(fenetre, text="   Format d'arrivée", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
           
            fenetre.menua= tk.StringVar(fenetre)
            menuA = ttk.OptionMenu(fenetre,fenetre.menua,Li[0], *Li)
        else:
            menuA=Entry(fenetre,justify='center',borderwidth=3)
            menuA.insert(0, basea)
            menuA.configure(state="readonly")



        txt3=Label(fenetre, text="   Nombre de bits\n  (entre 4 et 16)", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')


        txt4=Label(fenetre, text="   Valeur de départ", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')



        txt5=Label(fenetre, text="   Résultats", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')

        Resultats=Entry(fenetre,justify='center',borderwidth=3)



        def create():
            rappel = Toplevel(fenetre)
            rappel.config(background="lightskyblue1")
            titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
            titre.grid(row=1, column=2,columnspan=3,sticky='s')

            txt1=Label(rappel, text="Si l’entier codé en SVA/C2 commence par 1 :", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=60, height=2)
            txt2=Label(rappel, text="Son signe est négatif.", font=("courier", 16, "italic"), fg='darkslateblue', bg= 'lightskyblue1',width=60, height=2)

            txt3=Label(rappel, text="Si l’entier codé en SVA/C2 commence par 0 :", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=60, height=2)
            txt4=Label(rappel, text="Son signe est positif.", font=("courier", 16, "italic"), fg='darkslateblue', bg= 'lightskyblue1',width=60, height=2)

            txt5=Label(rappel, text="Pour convertir un nombre négatif de C2 vers SVA:", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg= 'lightskyblue1',width=60, height=2)
            txt6=Label(rappel, text="On soustrait 1,puis on inverse les bits en faisant attention au signe.", font=("courier", 16, "italic"), fg='darkslateblue', bg= 'lightskyblue1',width=80, height=2)

            txt7=Label(rappel, text="Pour coder un entier négatif en C2 :", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=60, height=2)
            txt8=Label(rappel, text="On part de la valeur absolue,on inverse les bits puis on ajoute 1", font=("courier", 16, "italic"), fg='darkslateblue', bg= 'lightskyblue1',width=80, height=2)

            txt1.grid(row=2, column=3)
            txt2.grid(row=3, column=2, columnspan=4)
            txt3.grid(row=4, column=3)
            txt4.grid(row=5, column=2, columnspan=4)
            txt5.grid(row=6, column=3)
            txt6.grid(row=7, column=2, columnspan=4)
            txt7.grid(row=8, column=3)
            txt8.grid(row=9, column=2, columnspan=4)
                                                            

            rappel.rowconfigure(1, weight=1)
            rappel.rowconfigure(2, weight=1)
            rappel.rowconfigure(3, weight=1)
            rappel.rowconfigure(4, weight=1)
            rappel.rowconfigure(5, weight=1)
            rappel.rowconfigure(6, weight=1)
            rappel.rowconfigure(7, weight=1)
            rappel.rowconfigure(8, weight=1)
            rappel.rowconfigure(9, weight=1)
            rappel.rowconfigure(10, weight=1)

            rappel.columnconfigure(1, weight=0)
            rappel.columnconfigure(2, weight=1)
            rappel.columnconfigure(3, weight=1)
            rappel.columnconfigure(4, weight=1)
            rappel.columnconfigure(5, weight=1)
            rappel.columnconfigure(6, weight=1)
            rappel.columnconfigure(7, weight=0)  

            def exit_btn():

                rappel.destroy()
                rappel.update()

            btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
            btn.grid(row=10, column=2,columnspan=3,sticky='n')

        def back():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            menuD.destroy()
            txt2.destroy()
            menuA.destroy()
            txt3.destroy()
            txt4.destroy()
            txt5.destroy()
            Resultats.destroy()
            Val.destroy()
            Nb.destroy()
            GO.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Chap1()
        def back2():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            menuD.destroy()
            txt2.destroy()
            menuA.destroy()
            txt3.destroy()
            txt4.destroy()
            txt5.destroy()
            Resultats.destroy()
            Val.destroy()
            Nb.destroy()
            GO.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Menu()

                
        B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

        B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
         
        B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Validation())
         
        B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2, command=back2)
         
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=back)


        GO=Button(fenetre, text="Go!", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=10, height=0,command=lambda:go())        
        GO.grid(row=4, column=5,sticky='n',columnspan=6)

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
        B1.grid(row=18, column=1)
        B2.grid(row=18, column=2)
        B3.grid(row=18, column=3)
        B4.grid(row=18, column=6)
        B5.grid(row=18, column=4)


#===================================================================================================================================================================================
#==========================================================================================
#===================== Chapitre 1 - Exercice 6 ===========================================

    def Exercice6(f,select):
        ###===================================== L'aléatoire =====================================#
        def NumVirgule(formats):
            if formats == '10':
                entier = AleaExAll(2, 1, 27)#32 - 5 = 27 max (Nombre avant la virgule)
                dec = AleaExAll(2, 1, 5)
                entier=str(entier)+'.'+str(dec)
                
            elif formats == '2':
                entier = uniform(1,10000)
                entier = round(entier,3)
            else:
                return(1)
            
                
            return(str(entier))
                
         
        #==========================================================================#
        #Fonction qui permet de convertir les entiers décimaux en binaire décimaux
        def dec_bin(decimal,ApresVirg):

            entier, dec = str(decimal).split('.')
            entier = int(entier)
            dec = '0.' + dec
            dec = float(dec)
            resultat = str(bin(entier).replace("0b",'')+'.')
            print("miaou",ApresVirg)
            ApresVirg = int(ApresVirg)
                # Nombre après la virgule
            for i in range(ApresVirg):
                dec *= 2
                if dec < 1 :
                    resultat += '0'
                else :
                    resultat += '1'
                    dec -= 1
            return (resultat)


        #=========================================================================#
        #Fonction qui permet de convertir les binaires décimaux en entier décimaux      
        def bin_dec(binaire,ApresVirg):
            #on sépare l'entier et le décimal en deux variables distinctes
            entier, dec = str(binaire).split('.')
            entier = int(entier,2)
            resultat = entier
            val = 0.0
            puis = 0.5

            ApresVirg = int(ApresVirg)
            for i in dec: 
                if i =='1':
                    val += puis
                puis /= 2
            resultat += (val)
            resultat = '%.*f' % (ApresVirg, resultat)
            return str(resultat)
            

        #========================================================================================#
        lischoix = [ '10','2']

        def  AleaEx6_Ordre(lischoix):
                #aléatoire de l'ordre
                choix = choice(lischoix)
                return(choix)

        def AleaVirgule(ordre):
                
                if ordre=='2':
                    virgule=randrange(1,6)
                  
                else:
                    virgule=3

                return(virgule)
            
        def AleaEx6():
            ordre=AleaEx6_Ordre(lischoix)
            if ordre=='2':
                    valeur=NumVirgule('2')
            else:     
                    valeur=NumVirgule('10')
                    
            return(valeur,ordre)


        def count_decimaux(nombre,resu,ApresVirg):
            n = nombre[::-1].find('.')
            if resu == 'resultat':
                return(n)
            elif resu == 'ctrlsynth':
                if str(n) == str(ApresVirg) :
                    return(True)
                else:
                    return(False)
            
        #==========================================================================================#
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
        fenetre.rowconfigure(9, weight=1)
        fenetre.rowconfigure(10, weight=1)
        fenetre.rowconfigure(11, weight=1)
        fenetre.rowconfigure(12, weight=1)
        fenetre.rowconfigure(13, weight=1)
        fenetre.rowconfigure(14, weight=1)
        fenetre.rowconfigure(15, weight=1)
        fenetre.rowconfigure(16, weight=1)
        fenetre.rowconfigure(17, weight=1)
        fenetre.rowconfigure(18, weight=1)


        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, weight=1)
        fenetre.columnconfigure(3, weight=1)
        fenetre.columnconfigure(4, weight=1)
        fenetre.columnconfigure(5, weight=0)
        fenetre.columnconfigure(6, weight=1)
        fenetre.columnconfigure(7, weight=1)
        fenetre.columnconfigure(8, weight=1)
        fenetre.columnconfigure(9, weight=1)
        fenetre.columnconfigure(10, weight=1)
        fenetre.columnconfigure(11, weight=1)
        fenetre.columnconfigure(12, weight=1)

        man=select

        ordre = ""

        if man == 1 :
            alea=AleaEx6()
            ordre = alea[1]
            valeur = alea[0]
            virgule=AleaVirgule(ordre)

            
        def controle():


            if man==2:
                entier = saisieVal.get()
                entier=Raccourcir(entier)
                
                ApresVirg = saisieVirg.get()
                bApresVirg=Raccourcir(ApresVirg)
                util = Resultats.get()
                util=Raccourcir(util)
                formats = fenetre.option_var.get()
                print("voici le format:",formats)
                

                if entier=='' or util=='' or ApresVirg=='':
                    messagebox.showerror("showerror", "Veuillez saisir toutes les valeurs")
                    return(1)
                else:
                    if not "." in entier:
                        messagebox.showerror("showerror", "Veuillez saisir un float pour l'entier")
                        return(1)
                    
                    else:
                        if formats=='2':
                            ok = CtrlSyntaxe(entier,10,1,20,1,10000)
                            ok2 = CtrlSyntaxe(util,2,1,32)
                            if not 1<=int(ApresVirg)<=6 :
                                messagebox.showerror("showerror", "Nombre de bits compris entre 1 et 6")
                                return(1)
                            
                                     
                        elif formats=='10':
                            ok = CtrlSyntaxe(str(entier),2,1,32)
                            ok2 = CtrlSyntaxe(util,10,1,20,1,10000)
                            
                            okEnt= count_decimaux(entier, 'resultat','5')
                            
                            if okEnt>5:
                                messagebox.showerror("showerror", "Pas plus de 5 bits après la virgule")
                                return(1)
                            
                        ok3= count_decimaux(util, 'ctrlsynth',ApresVirg)
                        
                        if ok==False:
                            messagebox.showerror("showerror", "Erreur de saisie de la valeur de départ")
                            return(1)
                        else:
            
                            if ok2==True:
                                if ok3==False:
                                        messagebox.showerror("showerror", "Le nombre de chiffre après la virgule ne correspond pas")
                                        return(1)
                            else:
                                messagebox.showerror("showerror", "Erreur de saisie du résultat ")
                                return(1)
                
                
            elif man==1:
                
                entier = valeur
                util = Resultats.get()
                util=Raccourcir(util)
                formats=w1.cget("text")
                ApresVirg=saisieVirg.cget("text")
               

                if util=='':
                    messagebox.showerror("showerror", "Veuillez saisir une valeur")
                    return(1)
                else:
                    
                    if not "." in entier:
                        messagebox.showerror("showerror", "Veuillez saisir un float pour l'entier")
                        return(1)
                    else:
                        
                        ok3= count_decimaux(util, 'ctrlsynth',ApresVirg)
                    
                        if formats=='2':
                            ok2 = CtrlSyntaxe(util,2,1,32)
                            
                        elif formats=='10':

                            ok2 = CtrlSyntaxe(util,10,1,20,1,10000)
                        
                    
                        if ok2==True:
                            if ok3==False:  
                                    messagebox.showerror("showerror", "Le nombre de chiffre après la virgule ne correspond pas ")
                                    return(1)
                        else:
                                messagebox.showerror("showerror", "Erreur de saisie du résultat")
                                return(1)
                    

            return(util,entier,formats,ApresVirg)

        def get():

            ok=True
            saisie=controle()
            
            if not saisie==1 :

                    util=saisie[0]
                    entier=saisie[1]
                    formats=saisie[2]
                    print(formats)
                    ApresVirg=saisie[3]

                            
                    if formats=='10':
                        rep = bin_dec(str(entier),str(ApresVirg))
                    elif formats=='2':
                        rep = dec_bin(entier,ApresVirg)
                            
                    
                    print("voici la rep",rep)
                    Verif=VerifRep(str(rep),util)
                    w1.config(state='disabled')
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
        def nouveau():

            B3['state']='normal'#Valider
            B2['state']='disabled'#Nouveau

            if man==2:

                saisieVal.delete(0,END)
                saisieVirg.delete(0,END)
                Resultats.delete(0,END)
                w1.config(state='normal')
                
            
            elif man==1:

               alea=AleaEx6()
               ordre = alea[1]
               valeur = alea[0]
               virgule=AleaVirgule(ordre)
               
               Resultats.delete(0,END)

               saisieVal.config(text=valeur)
               saisieVirg.config(text=virgule)
               w1.config(text=ordre)
              
                
        #------------------------------------------------------------------------------------------------------------#

        OptionsExo6 = ("2","10")


        titre=Label(fenetre, text="Les Décimaux", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')  # Placement de l'invite

        soustitre=Label(fenetre, text="Quelques Indications: Base de départ 10 valeur --> 0 et 10 000, entre 1 et 6 bits après la virgule \n              Base de départ 2 --> max 5 bits après la virgule , valeur max 32 bits", font=("courier", 13), fg='darkblue', bg='lightskyblue1') 

        if man==1:
            if ordre=='10':    
                txt1=Label(fenetre, text="  Binaire à convertir", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
            else:
                txt1=Label(fenetre, text="  Décimal à convertir", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
            
        else:
                txt1=Label(fenetre, text="  Valeur à convertir", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
               
           
        if man==2:
            saisieVal=Entry(fenetre) 
            val=StringVar(fenetre) # variable qui récupérera la valeur de la case à cocher
        else:
            saisieVal=Label(fenetre, text=valeur, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)


        txt2=Label(fenetre, text="  Convertir au format", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')

       
        if man==2:
            fenetre.option_var= tk.StringVar(fenetre)
            w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo6[0], *OptionsExo6)
        else:
            w1=Label(fenetre, text=ordre, font=("courier", 15, "italic"), fg='black', bg='white',width=4, height=1)

        if man==1:
            if ordre=='10':
                txt3=Label(fenetre, text="  Nombres après la virgule", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
            else:
                txt3=Label(fenetre, text="  Bits après \nla virgule", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        else:
                txt3=Label(fenetre, text="  Nombres après \nla virgule", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')

            
        if man == 2 :
            val = IntVar(fenetre)
            saisieVirg=Entry(fenetre) #ERREUR - faut que ça le lise en tant que integer
        else:
            saisieVirg = Label(fenetre, text=virgule, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)


        txt4=Label(fenetre, text="  Résultat", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
        Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats

        #======================================================================================================================#
        def create():
            rappel = Toplevel(fenetre)
            rappel.config(background="lightskyblue1")
            titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
            titre.grid(row=1, column=2,columnspan=3,sticky='s')

            txt1=Label(rappel, text="Pour obtenir la partie décimale\non utilise la méthode de la multiplication.", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
          
            txt1.grid(row=2, column=3,ipadx=100,ipady=40)
          
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

        #================================================================================================================================================#

        def back():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            saisieVal.destroy()
            txt2.destroy()
            txt3.destroy()
            txt4.destroy()
            w1.destroy()
            Resultats.destroy()
            saisieVirg.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Chap1()
        def back2():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            saisieVal.destroy()
            txt2.destroy()
            txt3.destroy()
            txt4.destroy()
            w1.destroy()
            Resultats.destroy()
            saisieVirg.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Menu()
        
        B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

        B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
         
        B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get())
         
        B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2, command=back2)
         
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=back)

        titre.grid(row=1, column = 2, columnspan=3)
        soustitre.grid(row=2, column=1,columnspan=4,ipady=50,ipadx=50)
        txt1.grid(row=4,column=1,columnspan=2,sticky='w',ipady=10)
        
        saisieVal.grid(row=4, column=2,ipadx=200,columnspan=4,ipady=10)


        txt2.grid(row=6, column=1,columnspan=2,sticky='w',ipady=10)
        w1.grid(row=6, column=2,ipadx=235,columnspan=4,ipady=10)

        txt3.grid(row=8, column=1,columnspan=2,sticky='w',ipady=10)
        saisieVirg.grid(row=8, column=2,ipadx=200,columnspan=4,ipady=10)

        txt4.grid(row=10,column=1,columnspan=2,sticky='w',ipady=10)
        Resultats.grid(row=10, column=2,ipadx=200,columnspan=4,ipady=10)



        #bouton#
        B1.grid(row=18, column=1)
        B2.grid(row=18, column=2)
        B3.grid(row=18, column=3)
        B4.grid(row=18, column=5)
        B5.grid(row=18, column=4)


        
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

        lis=["IEEE","réel"]

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
            if formats=="réel":
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
        fenetre.rowconfigure(7, weight=1)
        fenetre.rowconfigure(8, weight=1)
        fenetre.rowconfigure(9, weight=1)
        fenetre.rowconfigure(10, weight=1)
        fenetre.rowconfigure(11, weight=1)
        fenetre.rowconfigure(12, weight=1)
        fenetre.rowconfigure(13, weight=1)
        fenetre.rowconfigure(14, weight=1)
        fenetre.rowconfigure(15, weight=1)
        fenetre.rowconfigure(16, weight=1)
        fenetre.rowconfigure(17, weight=1)
        fenetre.rowconfigure(18, weight=1)


        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, weight=1)
        fenetre.columnconfigure(3, weight=1)
        fenetre.columnconfigure(4, weight=1)
        fenetre.columnconfigure(5, weight=0)
        fenetre.columnconfigure(6, weight=1)
        fenetre.columnconfigure(7, weight=1)
        fenetre.columnconfigure(8, weight=1)
        fenetre.columnconfigure(9, weight=1)
        fenetre.columnconfigure(10, weight=1)
        fenetre.columnconfigure(11, weight=1)
        fenetre.columnconfigure(12, weight=1)

        man=select # variable qui va définir si c'est manuel ou aléatoire
        
        formats=""
        if man ==1 :
            alea=SaisieAllEx7()
            formats=alea[1]
            valeur=alea[0]
            
        def get(formats):
            if man==2:
                entier = saisieVal.get()
                entier=Raccourcir(entier)
                util = Resultats.get()
                util=Raccourcir(util)
                util=util.upper()
                formats = fenetre.option_var.get()
                formats=Raccourcir(formats)
                w1.config(state='disabled')
            else:
                entier=valeur
                util = Resultats.get()
                util=Raccourcir(util)
                util=util.upper()

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
                    
                ok=CtrlSyntaxe(str(entier),16,1,8)
                ok2=CtrlSyntaxe(util,10,1,20,-10000,10000)
                if ok==False: 
                    messagebox.showerror("showerror", "Erreur de saisie de hexadécimal")
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


        OptionsExo1 = ("IEEE","réel")


        titre=Label(fenetre, text="Les réels", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  # Placement de l'invite

        soustitre=Label(fenetre, text="    Quelques Indications: Les valeurs en base 10 sont compris entre -10 000 et 10 000 \n\n                     Attention mettre un . et non , pour les réels à virgule\n \n                    Conversion en IEEE= Hexadécimal ", font=("courier", 18, "italic"), fg='darkblue', bg='lightskyblue1') 
        
        txt1=Label(fenetre, text="  Réel à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
            
            saisieVal=Entry(fenetre) 
            val=StringVar(fenetre) # variable qui récupérera la valeur de la case à cocher

        else:
            saisieVal=Label(fenetre, text=valeur, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)



        txt2=Label(fenetre, text="  Convertir au\n  format", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        if man==2:
           
            fenetre.option_var= tk.StringVar(fenetre)
            w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo1[0], *OptionsExo1)
        else:
            w1=Label(fenetre, text=formats, font=("courier", 15, "italic"), fg='black', bg='white',width=4, height=1)



        txt3=Label(fenetre, text="  Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')

        Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats


                
        #=========================================================================
        #================= Page rappel ===========================================
        #=========================================================================

        def create():
            rappel = Toplevel(fenetre)
            rappel.config(background="lightskyblue1")
            titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
            titre.grid(row=1, column=2,columnspan=3,sticky='s')

            txt1=Label(rappel, text="1 bit de signe", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
            txt2=Label(rappel, text="8 bits d’exposant biaisé (biaisé de 127)", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
            txt3=Label(rappel, text="23 bits de mantisse", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg= 'lightskyblue1',width=40, height=2)
            txt4=Label(rappel, text="Ne pas oublier le bit implicite", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)

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
               w1.config(state='normal')
               saisieVal.delete(0,END)
               Resultats.delete(0,END)


        def back():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            saisieVal.destroy()
            txt2.destroy()
            txt3.destroy()
            w1.destroy()
            Resultats.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Chap1()
        def back2():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            saisieVal.destroy()
            txt2.destroy()
            txt3.destroy()
            w1.destroy()
            Resultats.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            Menu()
                
        B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

        B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
         
        B3=Button(fenetre, text="Valider", font=("courier", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(formats))
         
        B4=Button(fenetre, text="Menu", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=back2)
         
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=back)

        titre.grid(row=1, column=2,columnspan=3,ipady=20)
        soustitre.grid(row=2, column=1,columnspan=5,sticky='w',ipady=20)
        txt1.grid(row=6, column=1,columnspan=2,sticky='w',ipady=40)
        saisieVal.grid(row=6, column=2,ipadx=200,columnspan=4,ipady=10,pady=20)

        txt2.grid(row=8, column=1,columnspan=2,sticky='w')
        txt3.grid(row=9, column=1,columnspan=2,sticky='w',ipady=40)
        w1.grid(row=8, column=2,ipadx=235,columnspan=4,ipady=10,pady=20)
        Resultats.grid(row=9, column=2,ipadx=200,columnspan=4,ipady=10)



        #bouton#
        B1.grid(row=18, column=1)
        B2.grid(row=18, column=2)
        B3.grid(row=18, column=3)
        B4.grid(row=18, column=6)
        B5.grid(row=18, column=4)

#===================================================================================================================================================================================
#==========================================================================================
#===================== Chapitre 1 - Exercice 8 ============================================
    def Exercice8(f,select):
        fenetre=f
        fenetre.config(background="lightskyblue1")
        #fenetre.attributes('-fullscreen', True)

        fenetre.rowconfigure(1, weight=0)
        fenetre.rowconfigure(2, weight=0)
        fenetre.rowconfigure(3, weight=1)
        fenetre.rowconfigure(4, weight=1)
        fenetre.rowconfigure(5, weight=1)
        fenetre.rowconfigure(6, weight=1)
        fenetre.rowconfigure(7, weight=1)
        fenetre.rowconfigure(8, weight=1)
        fenetre.rowconfigure(9, weight=1)
        fenetre.rowconfigure(10, weight=1)
        fenetre.rowconfigure(11, weight=1)
        fenetre.rowconfigure(12, weight=1)
        fenetre.rowconfigure(13, weight=1)
        fenetre.rowconfigure(14, weight=1)
        fenetre.rowconfigure(15, weight=1)
        fenetre.rowconfigure(16, weight=1)
        fenetre.rowconfigure(17, weight=1)
        fenetre.rowconfigure(18, weight=1)


        fenetre.columnconfigure(1, weight=1)
        fenetre.columnconfigure(2, weight=1)
        fenetre.columnconfigure(3, weight=1)
        fenetre.columnconfigure(4, weight=1)
        fenetre.columnconfigure(5, weight=0)
        fenetre.columnconfigure(6, weight=1)
        fenetre.columnconfigure(7, weight=1)
        fenetre.columnconfigure(8, weight=1)
        fenetre.columnconfigure(9, weight=1)
        fenetre.columnconfigure(10, weight=1)
        fenetre.columnconfigure(11, weight=1)
        fenetre.columnconfigure(12, weight=1)


        Raiponce={}
        man=select
        donne=()
        donne2="Appuyer sur Go!"
        ko=1
        taille=""
        TailleC=""
        Adresse=""
        def VerifRaip(rep,util):
            a=0
            "Compare la réponse à l’exercice (rep) avec la réponse de l’utilisateur (util)"
            if rep == util:
                a=1
            else:
                a=0
            return(a)

        if man ==1 :
            taille=AleaExAll(10,30,190)
            taille=Raccourcir(str(taille))
            TailleC=AleaExAll(10,1,5)
            TailleC=Raccourcir(str(TailleC))
            Adresse=AleaExAll(10,1,1000)
            Adresse=Raccourcir(str(Adresse))
            donne=(taille,TailleC,Adresse)

        def control(donne,ko,taille,TailleC,Adresse):
            global donne2
            B6['state']='disabled'
            
            if man==2:
                taille = TailleTab.get()
                taille=Raccourcir(taille)
                TailleC = TailleCase.get()
                TailleC=Raccourcir(TailleC)
                Adresse = AdPMTab.get()
                Adresse=Raccourcir(Adresse)
                
                if taille=="" or TailleC=="" or Adresse=="":
                    B6['state']='normal'
                    messagebox.showerror(title="Erreur",
                                message="Veuillez saisir toutes les valeurs")
                    return(1)
                else:

                    if "." in taille or "." in TailleC or "."in Adresse:
                        B6['state']='normal'
                        messagebox.showerror(title="Erreur",
                                    message="Erreur les points ne sont pas acceptés")
                        
                        return(1)
                
                    else:
                        
                        ok=CtrlSyntaxe(str(taille),10,1,10,30,300)
                        ok2=CtrlSyntaxe(str(TailleC),10,1,10,1,300)
                        ok3=CtrlSyntaxe(str(Adresse),10,1,100,1,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

                        if ok==False:
                            B6['state']='normal'
                            messagebox.showerror(title="Erreur",
                                        message="Erreur de saisie pour la taille du tableau")
                            return(1)
                        

                        elif ok2==False:
                            B6['state']='normal'
                            messagebox.showerror(title="Erreur",
                                        message="Erreur de saisie pour la taille d'une case")
                            return(1)
                        elif ok3==False:
                            B6['state']='normal'
                            B3['state']='disabled'
                            messagebox.showerror(title="Erreur",
                                        message="Erreur de saisie pour l'adresse du premier mot")
                            return(1)
                        
                        elif int(taille)*int(TailleC)>950:
                            B6['state']='normal'
                            B3['state']='disabled'
                            messagebox.showerror(title="Erreur",
                                        message="Erreur : Taille du tableau * Taille d'une case >950")
                            return(1)
                        else:
                            B3['state']='normal'
                            TailleTab.configure(state="disabled")
                            TailleCase.configure(state="disabled")
                            AdPMTab.configure(state="disabled")
            else:
                B3['state']='normal'
                    
            if ko==1:
                donne2=AleaExAll(10,1,int(taille))
                print(donne2)
            donne3=int(donne2)
            donne=(taille,TailleC,Adresse,donne3)
            NumCase.config(text=donne2)
            return(donne)

        def RepEx8(donne):
            nbmot=int(donne[0])*int(donne[1])
            numdermot=(nbmot+int(donne[2]))-1
            numpremot=donne[2]
            return([str(nbmot),str(numpremot),str(numdermot)])
            
        def get(donne):
            ko=0
            util=[]
            donne=control(donne,ko,taille,TailleC,Adresse)
            if not donne==1:
                donne=list(donne)+list(str(donne2))
                util0=Raccourcir(NbCTab.get())
                util1=Raccourcir(NumPTab.get())
                util2=Raccourcir(NumDTab.get())
                util3=Raccourcir(MotCase.get())
                util3=util3.replace(",","")
                util=(util0,util1,util2,util3)
                rep=RepEx8(donne)
                if man==1:
                    if type(donne[3])==str:
                        print(donne[3])
                       
                        return(1)
                rep2=(str(int(donne[2])+(int(donne[3])-1)*int(donne[1])))
                rep4=rep2
                for i in range(int(donne[1])-1):
                    rep3=int(rep2)+i+1
                    rep4+=","+str(rep3)
                rep5=rep4.replace(",","")
                rep.append(rep5)
                for i in util:
                    if i=='':
                        messagebox.showerror(title="Information",
                                        message="Veuillez saisir les réponses")
                        return(1)
                    else:
                        ok=CtrlSyntaxe(i,10,0,200,0,100000000000000000000000000)
                    if ok==False:
                        messagebox.showerror(title="Information",
                                        message="Erreur de syntaxe")
                        return(1)
                Raiponce={}
                for i in range(4):
                    verif=VerifRaip(rep[i],util[i])
                    Raiponce[rep[i]]=verif
                dico={1:txtQ10,2:txtQ11,3:txtQ12,4:txtQ2}
                nb=0
                Verif=VerifRep(rep,list(util))
                if Verif == 1:
                   B3['state']='disabled' #bloquer le bouton valider ==> Gagner
                   B2['state']='normal'
                   messagebox.showinfo(title="Information",
                                            message="Bonne Réponse, Bravo !! ")
                    
                elif Verif == -1:
                    B3['state']='disabled' #bloquer le bouton valider ==> Perdu
                    B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
                    messagebox.showinfo(title="Information",
                                        message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n\n"
                                        +"Nombres de mots:"
                                        + ("".join(rep[0]))
                                        + "\n\n"
                                        +"Numéro du premier mot: "
                                        + ("".join(rep[1]))
                                        + "\n\n"
                                        +"Numéro du dernier mot: "
                                        + ("".join(rep[2]))
                                        + "\n\n"
                                        +"Mot contenu dans la case: "
                                        + ("".join(str(donne[3])))
                                        +" :"
                                        +("".join(rep4)))
                elif Verif == 0:
                    for i in Raiponce:
                        if Raiponce[i]==0:
                            nb+=1
                            dico[nb].config(fg='red')
                        else:
                            nb+=1
                            dico[nb].config(fg='black')
                    messagebox.showinfo(title="Information",
                                        message="Mauvaise réponse, réessayer !")

            
          
            
               
        ## INTERFACE ##########################

               
               
        titre=Label(fenetre, text="Les Tableaux", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  # Placement de l'invite

        soustitre=Label(fenetre, text="    Quelques Indications: La taille du tableau est comprise entre 30 et 300 cases \n                     Taille mot * taille case ne doit pas dépasser 950 mots ",font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

        txt1=Label(fenetre, text="  Taille du tableau", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
        txt1a=Label(fenetre, text="  (en nombre de case)", font=("courier", 12, "italic"), fg='black', bg='lightskyblue1')

        txt2=Label(fenetre, text="  Taille d'une case", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
        txt2a=Label(fenetre, text="  (en nombre de mot)", font=("courier", 12, "italic"), fg='black', bg='lightskyblue1')

        txt3=Label(fenetre, text="  Adresse 1 mot ", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
        txt4=Label(fenetre, text="  Numéro de case", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')

        txtQ10=Label(fenetre, text="  Nombre de mots", font=("courier", 20), fg='black', bg='lightskyblue1')
        txtQu1=Label(fenetre, text="  Question 1 :", font=("courier", 20, "bold"), fg='black', bg='lightskyblue1')
        txtQ11=Label(fenetre, text="  Numéro du premier mot", font=("courier", 20), fg='black', bg='lightskyblue1')
        txtQ12=Label(fenetre, text="  Numéro du dernier mot", font=("courier", 20), fg='black', bg='lightskyblue1')

        txtQ2=Label(fenetre, text="  Mot contenus dans la case", font=("courier", 20), fg='black', bg='lightskyblue1')
        txtQu2=Label(fenetre, text="  Question 2 :", font=("courier", 20, "bold"), fg='black', bg='lightskyblue1')

        if man ==2:
            
            TailleTab=Entry(fenetre,justify='center',borderwidth=3)

            TailleCase=Entry(fenetre,justify='center',borderwidth=3)

            AdPMTab=Entry(fenetre,justify='center',borderwidth=3)

        else:
            TailleTab=Label(fenetre, text=taille , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
            TailleCase=Label(fenetre, text=TailleC , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
            AdPMTab=Label(fenetre, text=Adresse , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)

            
        NumCase=Label(fenetre, text=donne2 , font=("courier", 12, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken")


        NbCTab=Entry(fenetre,justify='center')

        NumPTab=Entry(fenetre,justify='center') 
        NumDTab=Entry(fenetre,justify='center')

        MotCase=Entry(fenetre,justify='center') 



        def create():
            rappel = Toplevel(fenetre)
            rappel.config(background="lightskyblue1")
            titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='darkblue', bg='lightskyblue1')
            titre.grid(row=1, column=2,columnspan=3,sticky='s')

            txt1=Label(rappel, text="Si a est le premier mot du tableau,", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
            txt2=Label(rappel, text=" et si une case contient n mots :", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
            txt3=Label(rappel, text=" Le premier mot de la case n°k", font=("courier", 16, "italic"), fg='darkslateblue', bg= 'lightskyblue1',width=40, height=2)
            txt4=Label(rappel, text=" est le mot a+(k-1)*n", font=("courier", 16, "italic"), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)

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
            txtQ10.config(fg='black')
            txtQ11.config(fg='black')
            txtQ12.config(fg='black')
            txtQ2.config(fg='black')
            B3['state']='normal'
            B2['state']='disabled'
            donne2="appuyer sur Go"
            NumCase.config(text=donne2)
            B6['state']='normal'
            if man ==1 : 
               B3['state']='disabled'
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

               B3['state']='disabled'
               TailleTab.configure(state="normal")
               TailleCase.configure(state="normal")
               AdPMTab.configure(state="normal")
                     
               TailleTab.delete(0,END)
               TailleCase.delete(0,END)
               AdPMTab.delete(0,END)

               
               NbCTab.delete(0,END)
               NumPTab.delete(0,END) 
               NumDTab.delete(0,END)
               MotCase.delete(0,END)

        def back():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            TailleTab.destroy()
            txt1a.destroy()
            txt2.destroy()
            TailleCase.destroy()
            txt2a.destroy()
            txt3.destroy()
            AdPMTab.destroy()
            txt4.destroy()
            NumCase.destroy()
            txtQ10.destroy()
            NbCTab.destroy()
            txtQu1.destroy()
            txtQ11.destroy()
            NumPTab.destroy()
            txtQ12.destroy()
            NumDTab.destroy()
            txtQ2.destroy()
            MotCase.destroy()
            txtQu2.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            B6.destroy()
            Chap1()
        def back2():
            titre.destroy()
            soustitre.destroy()
            txt1.destroy()
            TailleTab.destroy()
            txt1a.destroy()
            txt2.destroy()
            TailleCase.destroy()
            txt2a.destroy()
            txt3.destroy()
            AdPMTab.destroy()
            txt4.destroy()
            NumCase.destroy()
            txtQ10.destroy()
            NbCTab.destroy()
            txtQu1.destroy()
            txtQ11.destroy()
            NumPTab.destroy()
            txtQ12.destroy()
            NumDTab.destroy()
            txtQ2.destroy()
            MotCase.destroy()
            txtQu2.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()
            B5.destroy()
            B6.destroy()
            Menu()

                
        B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

        B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
         
        B3=Button(fenetre, text="Valider", state='disabled',font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(donne))
         
        B4=Button(fenetre, text="Menu", font=("calibri", 18, "italic"), fg='white', bg='grey', width=15, height=2,command=back2)
         
        B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=back)

        B6=Button(fenetre, text="Go!", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=14, height=0,command=lambda:control(donne,ko,taille,TailleC,Adresse))

        titre.grid(row=1, column=2,columnspan=3)
        soustitre.grid(row=2, column=1,columnspan=5,sticky='w')

        txt1.grid(row=5, column=1,columnspan=2,sticky='w')
        TailleTab.grid(row=5, column=2,ipady=10)

        txt1a.grid(row=6, column=1,sticky='n')

        txt2.grid(row=5, column=3,columnspan=4,sticky='w')
        TailleCase.grid(row=5,column=4,ipady=10)

        txt2a.grid(row=6, column=3,sticky='n')

    

        txt3.grid(row=7, column=1,columnspan=2,sticky='w',ipady=30)
        AdPMTab.grid(row=7, column=2,ipady=10)

        txt4.grid(row=7,column=3,columnspan=4,sticky='w',ipady=30)
        NumCase.grid(row=7, column=4,ipady=10,ipadx=20)

        txtQ10.grid(row=9, column=2,columnspan=3,sticky='w')
        NbCTab.grid(row=9, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

        txtQu1.grid(row=9, column=1,sticky='w')

        txtQ11.grid(row=11, column=2,columnspan=3,sticky='w')
        NumPTab.grid(row=11, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

        txtQ12.grid(row=13, column=2,columnspan=3,sticky='w')
        NumDTab.grid(row=13, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')


        txtQ2.grid(row=11, column=2,columnspan=3,sticky='w')
        MotCase.grid(row=11,column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

        txtQu2.grid(row=11, column=1,sticky='w')



        #bouton#
        B1.grid(row=18, column=1)
        B2.grid(row=18, column=2)
        B3.grid(row=18, column=3)
        B4.grid(row=18, column=5)
        B5.grid(row=18, column=4)
        B6.grid(row=6, column=5,sticky='nw')
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

       
        def back(t): #Retour
            if t ==1:
                tExoChap2.destroy()
                Retour2.destroy()
                txt.destroy()
                Manuelle2.destroy()
                Aléa2.destroy()
                
            elif t == 2:
                tExoChap2.destroy()
                Retour2.destroy()
                txt.destroy()
                Manuelle2.destroy()
                Aléa2.destroy()
                Menu() #Retour à la page précédente: fenetre des exercices(2eme)     

        def CommandExo(t):
            if t == 'Aléa':
                back(1)
                Exercice1(fenetre, 1)    
               
                
            elif t == 'Manuel':
                back(1) 
                Exercice1(fenetre, 2)
              
            
                #===== en cours

        tExoChap2= Label(fenetre, text= "Ordonnancement", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap2.grid(row=2, column=4, columnspan=5)
        txt=Label(fenetre, text= "Souhaitez vous une saisie Manuelle ou Aléatoire", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        txt.grid(row=4, column=4, columnspan=5,sticky='s')
                
        Manuelle2=Button(fenetre, text="Manuel", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(CommandExo,'Manuel'))
        Manuelle2.grid(row=10, column=6, ipady=30, ipadx=140,sticky='nesw')

        Aléa2=Button(fenetre, text="Aléatoire", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Aléa'))
        Aléa2.grid(row=10, column=8, ipady=30,ipadx=140,sticky='nesw')

        Retour2=Button(fenetre, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=lambda:(back(2)))
        Retour2.grid(row=17, column=4,columnspan=6,ipady= 15,ipadx=70)


        def Exercice1(f, select):
        #========================================================================================       
            fenetre=f
            fenetre.config(background="lightskyblue1")
            ##fenetre.attributes('-fullscreen', True)

            fenetre.rowconfigure(1, weight=0)
            fenetre.rowconfigure(2, weight=0)
            fenetre.rowconfigure(3, weight=1)
            fenetre.rowconfigure(4, weight=1)
            fenetre.rowconfigure(5, weight=1)
            fenetre.rowconfigure(6, weight=1)
            fenetre.rowconfigure(7, weight=1)
            fenetre.rowconfigure(8, weight=1)
            fenetre.rowconfigure(9, weight=1)
            fenetre.rowconfigure(10, weight=1)
            fenetre.rowconfigure(11, weight=1)
            fenetre.rowconfigure(12, weight=1)
            fenetre.rowconfigure(13, weight=1)
            fenetre.rowconfigure(14, weight=1)
            fenetre.rowconfigure(15, weight=1)
            fenetre.rowconfigure(16, weight=1)
            fenetre.rowconfigure(17, weight=1)
            fenetre.rowconfigure(18, weight=1)



            fenetre.columnconfigure(1, weight=1)
            fenetre.columnconfigure(2, weight=1)
            fenetre.columnconfigure(3, weight=1)
            fenetre.columnconfigure(4, weight=1)
            fenetre.columnconfigure(5, weight=1)
            fenetre.columnconfigure(6, weight=1)
            fenetre.columnconfigure(7, weight=1)
            fenetre.columnconfigure(8, weight=1)
            fenetre.columnconfigure(9, weight=1)
            fenetre.columnconfigure(10, weight=1)
            fenetre.columnconfigure(11, weight=1)
            fenetre.columnconfigure(12, weight=1)

            man = select
            
            Li=["Tourniquet","FIFO","PCTER","Priorite fixes","Algorithmes multi files FIFO sans migration","Algorithmes multi files FIFO avec migration","Algorithmes multi files TOURNIQUET sans migration","Algorithmes multi files TOURNIQUET avec migration"]
            global Type
            global lp
            global quantum
            global Ltemps
            global vis
            global visi
            vis=0
            visi=0
            quantum=0
            lp=[]
            Type=""
            #====================================================
            def CalculMoy(Ltemps):
                trac=[]
                for i in range(len(Ltemps)):
                    sous=Ltemps[i][1]-Ltemps[i][2]
                    trac.append(sous)
                p1=sum(trac)
                return (p1)
            #====================================================
            def CalculRep(Duree,lp,Type,Quantum):
                global Ltemps
                cpt=0
                pret=[]
                ordo=[]
                execute=[]
                Ltemps=[]
                for t in range(Duree):
                    ici=len(lp)
                    for i in range(len(lp)):
                        if lp[i]["da"]==t:
                            pret.append(lp[i])
                        else:
                            ici=i
                            break
                    if Type=="Tourniquet":
                        if execute!=[]:
                            pret.append(execute[0])
                            execute=[]
                    if Type=="PCTER":
                        pret=sorted(pret, key=lambda x: x["d"])
                    if Type=="Priorite fixes":
                        pret=sorted(pret, key=lambda x: x["prio"])
                    lp=lp[ici: ]
                    if pret==[]:
                        break
                    ordo.append({"temps":t, "nump":pret[0]["n"]})
                    pret[0]["d"]-=1
                    if pret[0]["d"]<=0:
                        Ltemps.append((pret[0]["n"],t+1,pret[0]["da"]))
                        pret=pret[1:]
                        if Type=="Tourniquet":
                            cpt=0
                    else:
                        if Type=="Tourniquet":
                            if cpt==Quantum-1:
                                execute.append(pret[0])
                                pret=pret[1:]
                                cpt=0
                            else:
                                cpt+=1
                print(Ltemps)
                return(ordo)

            def CalculRepFile(Duree,lp,Type):
                global Ltemps
                pretF1=[]
                pretF2=[]
                pretF3=[]
                ordo=[]
                executeF1=[]
                executeF2=[]
                executeF3=[]
                QF2=2
                QF3=3
                cptF2=0
                cptF3=0
                Ltemps=[]
                for t in range(Duree):
                    ici=len(lp)
                    
                    for i in range(len(lp)):
                       
                        if Type=="Algorithmes multi files TOURNIQUET avec migration" or Type=="Algorithmes multi files FIFO avec migration":
                            if lp[i]["da"]==t:
                                pretF1.append(lp[i])
                                print("pretF1",pretF1)
                            else:
                                ici=i
                                break
                        elif Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
                     
                           
                            if lp[i]["da"]==t and lp[i]["prio"]==1:
                                pretF1.append(lp[i])
                            
                            elif lp[i]["da"]==t and lp[i]["prio"]==2:
                                pretF2.append(lp[i])
                               
                            elif lp[i]["da"]==t and lp[i]["prio"]==3:
                                pretF3.append(lp[i])
                                
                            else:
                                ici=i
                                break
                    if Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
                        if executeF1!=[]:
                            pretF1.append(executeF1[0])
                            
                            executeF1=[]
                        if executeF2!=[]:
                            pretF2.append(executeF2[0])
                            
                            executeF2=[]
                    if Type=="Algorithmes multi files TOURNIQUET sans migration" or "Algorithmes multi files TOURNIQUET avec migration":
                        if executeF3!=[]:
                            pretF3.append(executeF3[0])
                            executeF3=[]

                    lp=lp[ici: ]
                    
                    if pretF1!=[]:
                        ordo.append({"temps":t, "nump":pretF1[0]["n"]})
                        pretF1[0]["d"]-=1
                        
                        if pretF1[0]["d"]==0:
                            Ltemps.append((pretF1[0]["n"],t+1,pretF1[0]["da"]))
                            pretF1=pretF1[1:]
                        else:
                            if Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
                                executeF1.append(pretF1[0])
                            else:
                                pretF2.append(pretF1[0])
                            pretF1=pretF1[1:]  
                    elif pretF2!=[]:
                        
                        ordo.append({"temps":t, "nump":pretF2[0]["n"]})
                        pretF2[0]["d"]-=1
                        if pretF2[0]["d"]==0:
                            Ltemps.append((pretF2[0]["n"],t+1,pretF2[0]["da"]))
                            pretF2=pretF2[1:]
                            cptF2=0
                        else:
                            if cptF2==QF2-1:
                                if Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
                                    executeF2.append(pretF2[0])
                                else:
                                    pretF3.append(pretF2[0])
                                pretF2=pretF2[1:]
                                cptF2=0
                            else:
                                cptF2+=1
                    else:
                        if pretF3==[]:
                            break
                        ordo.append({"temps":t, "nump":pretF3[0]["n"]})
                        
                        pretF3[0]["d"]-=1
                        if pretF3[0]["d"]==0:
                            Ltemps.append((pretF3[0]["n"],t+1,pretF3[0]["da"]))
                            pretF3=pretF3[1:]
                            if Type=="Algorithmes multi files TOURNIQUET avec migration" or Type=="Algorithmes multi files TOURNIQUET sans migration":
                                cptF3=0
                        else:
                            if Type=="Algorithmes multi files TOURNIQUET avec migration" or Type=="Algorithmes multi files TOURNIQUET sans migration":
                                if cptF3==QF3-1:
                                    executeF3.append(pretF3[0])
                                    pretF3=pretF3[1:]
                                    cptF3=0
                                else:
                                    cptF3+=1
                print("ordo",ordo)
                return(ordo)
                


            def dicointolist(ordo):
                liste=[]
                for i in range(len(ordo)):
                    liste.append(str(ordo[i]["nump"]))

                return(liste)   


            def Al():
                global prio
            
                
                Type=fenetre.menu.get()

                n=randrange(4,10)
                
                mini=0
                maxi=0
                cpt=0
                listarv=[]
                listdur=[]
                listprio=[]
                listp=[]
                listq=[]
                alea={}
                lp=[]
                
                for i in range (n):
                    duree=randrange(1,10)
                    cpt=cpt+1
                    
                    listdur.append(duree)
                    listp.append(i+1)
                    
                    arv=randint(mini,maxi)
                    listarv.append(arv)
                    
                    mini=arv
                    
                    prio=randrange(1,3)
                    listprio.append(prio)
                    
                    maxi=maxi+duree
                    q=randrange(1,3)
                    quantum=q
                    listq.append(quantum)
                      
                for i in range(len(listp)):
                
                    if Type=='Priorite fixes' or Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
                        lp.append({"n":listp[i],"da":listarv[i],"d":listdur[i],"prio":listprio[i]})
                    else :
                        lp.append({"n":listp[i],"da":listarv[i],"d":listdur[i],"quantum":listq[i]})        
                return(Type,n,lp,quantum)
            
            
              

            def AleaTab(lp,mode,NbProc,n):
                if man==1:
                    global Duree
                    i=0
                    j=0
                    Duree=0
                    if mode == "Tout":
                        nbc=3
                    else:
                        nbc=2
                    while i<NbProc*nbc and j<len(lp):
                        if i+nbc>NbProc*nbc:
                            break
                        else:
                            ListTabl[i].insert(0,lp[j]["da"])
                            ListTabl[i+1].insert(0,lp[j]["d"])
                            Duree+=(lp[j]["d"])
                            print(Duree)
                            
                            if nbc==3:
                                ListTabl[i+2].insert(0,lp[j]["prio"])
                            i+=nbc
                            j+=1

            def listintodico(liste):
                li=[]
                i=0
                cpt=1
            
                if Type=='Priorite fixes' or Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
                    while i<len(liste):
                        if i+3>len(liste):
                            break
                        li.append({"n": int(cpt), "da": int(liste[i]), "d": int(liste[i+1]), "prio": int(liste[i+2])})
                        cpt=cpt+1
                        i=i+3
                else:
                    while i<len(liste):
                        if i+2>len(liste):
                            break
                        li.append({"n": int(cpt), "da": int(liste[i]), "d": int(liste[i+1])})
                        cpt=cpt+1
                        i=i+2
             
                return(li)

            def ctrltab():
                global Ltab
                global ct
                global Duree
                global lp
                Ltab=[]
                err=[]
                ok=True
                ct=0
                synerror=[]

                
                
                for j in range(len(ListTabl)):

                    val=ListTabl[j].get()
                    val=Raccourcir(val)

                    Ltab.append(val) 

                    
                    if Ltab[j]=='' or Ltab[j]=='None' :
                        messagebox.showinfo(title="Information",
                                                               message="Veuillez remplir toutes les cases")
                        ok=False
                        return(1)
                    
                    else :
              
                        if not Ltab[0]=='0':
                            messagebox.showinfo(title="Information",
                                                             message="Premier processus doit arriver à 0 ")
                            return(1)
                       
                           
                        else:
                            if "." in Ltab[j] :
                                messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                                ok=False
                                return(1)
                            else:
                               ctrl=CtrlSyntaxe(str(Ltab[j]),10,1,2,0,100)
                               
                               if ctrl==False:
                                    synerror.append(j)  
                                    ListTabl[j].config(bg= "crimson")
                                    ct =ct+1
                                    ok=False
                            
                               else:
                                    ListTabl[j].config(bg= "white")
                                
                if ct >= 1:
                        messagebox.showinfo(title="Information",
                                        message="Erreur de syntaxe ou d'intervalle ")
                        return(1)
                    
                lp=listintodico(Ltab)
                Duree=0
                i=0
                while i<len(lp):
                    
                    Duree+=int(lp[i]["d"])
                    
                    i=i+1
                   
                            
            def CreaCase():
                global ListNom
                global mycanvas
                global vsb
                global frame_main
                global visi
                
                 
                ok=ctrltab()
                
                if ok!=1:
                    
                    visi=1
                    frame_main = tk.Frame(fenetre, bg="lightskyblue1")
                    frame_main.grid(column=7,row=6,columnspan=11,sticky='nw')
                    # Create a frame for the canvas with non-zero row&column weights
                    frame_canvas = tk.Frame(frame_main)
                    frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
                    frame_canvas.grid_rowconfigure(0, weight=1)
                    frame_canvas.grid_columnconfigure(0, weight=1)
                    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
                    #propagate permet d'adapter la taille du tableau
                    frame_canvas.grid_propagate(False)

                    # Add a canvas in that frame
                    canvas = tk.Canvas(frame_canvas, bg="lightskyblue1")
                    canvas.grid(row=0, column=0, sticky="news")

                    # Link a scrollbar to the canvas
                    vsb = ttk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
                    vsb.grid(row=0, column=1, sticky='ns')
                    
                    canvas.configure(yscrollcommand=vsb.set,highlightcolor='lightskyblue1',highlightbackground='lightskyblue1')

                    # Create a frame to contain the buttons
                    frame_buttons = tk.Frame(canvas, bg="lightskyblue1")
                    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

                    rows = 9
                    columns = 10

                    colmin=0
                    colmax=7
                    lignemin=0
                    col=0
                    ligne=0
                    ListNom=[]
                    for i in range(Duree):
                        Nom=str("a"+str(i))
                        ListNom.append(Nom)
                          
                    for i in range(Duree):
                        ListNom[i]=Entry(frame_buttons,width=10)
                        ListNom[i].grid(row=lignemin+ligne, column=colmin+col, pady=25)
                        ValTemps=(str(i)+"-"+str(i+1))
                        Temps=Label(frame_buttons, text=ValTemps ,font=("courier", 10), fg='black', bg='lightskyblue1')
                        Temps.grid(row=lignemin+ligne, column=colmin+col,sticky='s')
                        
                        if colmin+col>=colmax:
                            col=0
                            ligne+=1
                        else:
                            col+=1

                     

                    # Update buttons frames idle tasks to let tkinter calculate buttons sizes       
                    frame_buttons.update_idletasks()
                    # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
                    if Duree>7:
                        c=7
                    else:
                        c=Duree
                    first5columns_width = sum([ListNom[j].winfo_width() for j in range(0, c)])
                    first5rows_height = sum([ListNom[i].winfo_height() for i in range(0, 1)])
                    frame_canvas.config(width=first5columns_width +vsb.winfo_width(),
                                        height=first5rows_height+200)
                    # Set the canvas scrolling region
                    canvas.config(scrollregion=canvas.bbox("all"))    

                    tmr['state']='normal'
                    affcase['state']='disabled'
                        
            def debloq():
                    global Type
                    global n
                    global lp
                    global quantum
                    
                    
                    if man==1:

                      Alea=Al()
                      n=Alea[1]
                      lp=Alea[2]
                      quantum=Alea[3]

                    Type=fenetre.menu.get()
                   
                    
                    B1['state']='normal'
                    menu.configure(state="disabled")
                    OK['state']='disabled'
                    GO['state']='normal'

                    if man==2:
                        
                        nbprocs['state']='normal'
                    
                    
                        if Type=='Tourniquet' or Type=='Algorithmes multi files TOURNIQUET sans migration' or Type=='Algorithmes multi files TOURNIQUET avec migration':

                            Quantum['state']='normal'
                        else:
                            Quantum['state']='normal'
                            Quantum.insert(0,"Donnée non utile")
                            Quantum['state']='disabled'

                    if man==1:
                        
                    
                        nbprocs.config(text=n)

                        if Type=='Tourniquet':
                            Quantum.config(text=quantum)

                        else : 
                            Quantum.config(text="Données inutiles")

                    
            def CtrlDonnee():
                global quantum
                global nbprocessus
                nbprocessus=nbprocs.get()
                nbprocessus=Raccourcir(nbprocessus)
                quantum=Quantum.get()
                quantum=Raccourcir( quantum)



                if Quantum['state']=='disabled':

                    if nbprocessus=='':
                        messagebox.showerror(title="Information",
                                                                message="Veuillez saisir une réponse")
                        return(1)
                    else:
                        quantum=0
                        if "." in nbprocessus  :
                            messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                            return(1)
                        else:
                            
                            ctrl=CtrlSyntaxe(str(nbprocessus),10,1,2,4,10)
                            if ctrl==False:
                                messagebox.showerror(title="Information",
                                                                    message="Erreur de syntaxe ou intervalle non respectée dans nombre de processus")
                                return(1)
                            else:
                                nbprocs['state']='disabled'
                else:

                    if nbprocessus==''and quantum=="":

                        messagebox.showinfo(title="Information",
                                                                message="Veuillez saisir une réponse")
                        return(1)
                    else:
                        
                        if "." in nbprocessus or "." in quantum :
                            messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                            return(1)
                        else:
                            ctrl=CtrlSyntaxe(str(nbprocessus),10,1,2,4,10)

                            ctrl2=CtrlSyntaxe(str(quantum),10,1,2,1,4)
                            if ctrl==False:
                                messagebox.showerror(title="Information",
                                                                    message="Erreur de syntaxe ou intervalle non respectée dans nombre de processus")
                                return(1)
                            
                            else:
                                if ctrl2==False:
                                    messagebox.showerror(title="Information",
                                                                   message="Erreur de syntaxe ou intervalle non respectée pour quantum")
                                    return(1)
                                else:
                                    nbprocs['state']='disabled'
                                    Quantum['state']='disabled'
                                
            
            def buttonGo(Type):
                global ListTabl
                global Frame_main
                global vis
                
                if man==2:
                    ok=CtrlDonnee()
                   
                else:
                    ok=0
                  
                if ok!=1:
                    vis=1
                    affcase['state']='normal'
                    GO['state']='disabled'   
                    
                    if man==1:
                        NbProc = int(n)
                    else:    
                        NbProc = int(nbprocessus)
                    
                   
                   
                    if Type=='Priorite fixes' or Type=='Algorithmes multi files TOURNIQUET sans migration' or Type=='Algorithmes multi files FIFO sans migration':
                        mode="Tout"
                        NbCaseT = NbProc*3
                        NbCaseL = 3
                    else:
                        mode="None"
                        NbCaseT = NbProc*2
                        NbCaseL = 2
                    
                    Frame_main = tk.Frame(fenetre, bg="lightskyblue1")
                   
                 

                    # Create a frame for the canvas with non-zero row&column weights
                    frame_canvas = tk.Frame(Frame_main)
                    frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
                    frame_canvas.grid_rowconfigure(0, weight=1)
                    frame_canvas.grid_columnconfigure(0, weight=1)
                    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
                    frame_canvas.grid_propagate(False)

                    # Add a canvas in that frame
                    canvas = tk.Canvas(frame_canvas, bg="lightskyblue1")
                    canvas.grid(row=0, column=0, sticky="news")

                    canvas.configure(highlightcolor='lightskyblue1',highlightbackground='lightskyblue1')

                    # Create a frame to contain the buttons
                    frame_buttons = tk.Frame(canvas, bg="lightskyblue1")
                    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

                    # Add 9-by-5 buttons to the frame
                    rows = 9
                    columns = 10

                    colmin=1
                    colmax=NbCaseL+1
                    lignemin=1
                    lignemax=10
                    col=0
                    ligne=0
                    ListTabl=[]
              
                    for i in range(NbCaseT):
                        Process=str("g"+str(i))
                        ListTabl.append(Process)
                       
                    
                    #============titres de colonnes===============
                    ProcT=Label(frame_buttons, text="Processus" ,font=("courier", 9), fg='black', bg='white',width=17)
                    ProcT.grid(row=lignemin-1, column=col,sticky='s')
                    ArrT=Label(frame_buttons, text="Arrivée" ,font=("courier", 9), fg='black', bg='white',width=17)
                    ArrT.grid(row=lignemin-1, column=col+1,sticky='s')
                    DureeT=Label(frame_buttons, text="Durée" ,font=("courier", 9), fg='black', bg='white',width=17)
                    DureeT.grid(row=lignemin-1, column=col+2,sticky='s')
                    if mode == "Tout":
                        PrioT=Label(frame_buttons, text="Priorité initiale" ,font=("courier", 9), fg='black', bg='white',width=17)
                        PrioT.grid(row=lignemin-1, column=col+3,sticky='s')
                    #=================Première colonnes des Processus==========================
                    for i in range(NbProc):
                        Proc=Label(frame_buttons, text="p"+str(i+1) ,font=("courier", 8), fg='black', bg='white',width=17)
                        Proc.grid(row=lignemin+ligne, column=col,sticky='s')

                        if lignemin+ligne>=lignemax:
                            ligne=lignemax
                        else:
                            ligne+=1
                    colmin=1
                    colmax=NbCaseL
                    lignemin=1
                    lignemax=10
                    col=0
                    ligne=0
                        #=================Case vides==========================
                    for i in range(NbCaseT):
                        ListTabl[i]=Entry(frame_buttons,width=20)
                        ListTabl[i].grid(row=lignemin+ligne, column=colmin+col)
                    
                    
                        if colmin+col>=colmax:
                            col=0
                            ligne+=1
                         
                        else:
                            col+=1
                            

                    if NbProc <= 5:
                        
                        Frame_main.grid(column=2,row=6,columnspan=5,sticky='s')
                        frame_canvas.config(width=520,height=150)
                    else:
                        Frame_main.grid(column=2,row=6,columnspan=5)
                        frame_canvas.config(width=520,height=250)
             
                    canvas.config(scrollregion=canvas.bbox("all"))
                    
                    
                if man==1:
                    AleaTab(lp,mode,NbProc,n)
             

                     
                 
                   


            def CtrlCase():
                global Lutil
                global ct
                
                Lutil=[]
                err=[]
                ok=True
                ct=0
                synerror=[]


                for i in range(len(ListNom)):
                    
                    val=ListNom[i].get()
                    val=Raccourcir( val)

                    Lutil.append(val)
                    
                    if Lutil[i]=='':
                        messagebox.showinfo(title="Information",
                                                               message="Veuillez remplir toutes les cases")
                        ok=False
                        return(1)
                           
                    else:
                        if "." in Lutil[i] :
                            messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                            ok=False
                            return(1)
                        else:
                           ctrl=CtrlSyntaxe(str(Lutil[i]),10,1,2,0,10)
                           
                           if ctrl==False:
                                synerror.append(i)  
                                ListNom[i].config(bg= "crimson")
                                ct =ct+1
                                ok=False
                        
                           else:
                                ListNom[i].config(bg= "white")
                                i=i+1
                                
                if ct >= 1:
                        messagebox.showinfo(title="Information",
                                        message="Erreur de syntaxe ou d'intervalle ")
                        return(1)
                  

            def Crepe(Type,Duree):
                for i in range(len(ListTabl)):
                    lp=listintodico(Ltab)
                    
                if Type=="Tourniquet"or Type=="FIFO"or Type=="PCTER"or Type=="Priorite fixes":
                    rep0=CalculRep(Duree,lp,Type,int(quantum))
                 
                    rep=dicointolist(rep0)
                    

                elif Type=="Algorithmes multi files FIFO sans migration" or Type=="Algorithmes multi files FIFO avec migration"or Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files TOURNIQUET avec migration":
                    rep0=CalculRepFile(Duree,lp,Type)
                    
                    rep=dicointolist(rep0)
                    
                print("voici la rep",rep)
                return(rep,Duree)                            
                
            def validerSaisie(Duree):

                rep=[] 
                reponse=Crepe(Type,Duree)
                rep=reponse[0]
                erreur=[]

                controleC=CtrlCase()

                print("voici la rep",rep)
                if  controleC != 1 :
                        Verif=VerifRep(rep,Lutil)

                        if Verif == 1:
                            messagebox.showinfo(title="Information",
                                                message="Bonne Réponse,\n\n Veuillez saisir le temps moyen de réponse !! ")
                            B3['state']='normal'
                            tmr['state']='disabled'
                            deno['state']='normal'
                            numer['state']='normal'
                           
                                    
                        elif Verif == -1:
                            B3['state']='disabled' #bloquer le bouton valider ==> Perdu
                            B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
                            tmr['state']='disabled'
                            messagebox.showinfo(title="Information",
                                                message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("".join(str(rep))))
                        elif Verif == 0:
                            
                            for j in range(Duree):
                               
                                if rep[j]!=Lutil[j]:
                                    erreur.append(j)  
                                    ListNom[j].config(bg= "crimson")                
                                else:
                                    ListNom[j].config(bg= "white")
                                    

                            messagebox.showinfo(title="Information",
                                                message="Mauvaise réponse, réessayer ")


                
            def Valider():
    
                controleTemps=CtrlTmpRep()
                Lutil=[]
                Lrep=[]
                if man==1:
                    nbprocessus=nbprocs.cget("text")
                        
                   
                if man==2:
                    
                    nbprocessus=nbprocs.get()
                    
                if controleTemps!=1:
                    
                    numerateur=CalculMoy(Ltemps)
                   
                    denominateur= nbprocessus
                    
                    print("chiffre du haut",numerateur)
                    print("chiffre du bas",denominateur)
                    
                    denomi=deno.get()
                   
                    numera=numer.get()
                    

                    Lrep=[str(numerateur),str(denominateur)]
                    Lutil=[str(numera),str(denomi)]
                    Verif=VerifRep(Lrep,Lutil)

                    print(Lrep)
                    print(Lutil)
                  

                    if Verif == 1:
                        B3['state']='disabled' 
                        B2['state']='normal'
                        messagebox.showinfo(title="Information",
                                        message="Bonne Réponse, Bravo !! ")
                    elif Verif == -1:
                        B3['state']='disabled' 
                        B2['state']='normal'  
                        messagebox.showinfo(title="Information",
                                            message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n"
                                            +"\nNumérateur: "
                                            +("".join(str(numerateur)))
                                            +"\nDenominateur: "
                                            +("".join(str(denominateur))))
                    elif Verif == 0:
                   
                        messagebox.showinfo(title="Information",
                                            message="Mauvaise réponse dans la fraction, réessayer ")  
          

                
            def CtrlTmpRep():
                global numera
                global denomi

                denomi=deno.get()
                numera=numer.get()
                
                if numera =='' or denomi=='':
                    
                        messagebox.showinfo(title="Information",
                                                           message="Veuillez remplir la fraction")
                        return(1)
                           
                else:
                        if "." in numera or "." in  denomi :
                            messagebox.showerror("showerror", "Erreur pas de points dans la fraction")
                            return(1)
                        else:
                           ctrl2=CtrlSyntaxe(str(denomi),10,1,10,0,20)
                           ctrl1=CtrlSyntaxe(str(numera),10,1,10,0,1000)
                           
                           if ctrl1==False:
                                messagebox.showerror("showerror", "Erreur dans le numerateur")
                                return(1)
                           elif ctrl2==False:
                                messagebox.showerror("showerror", "Erreur dans le denominateur")
                                return(1)
                                
                            
            def nouveau():

                deno['state']='normal'
                deno.delete(0,END)
                deno['state']='disabled'
                
                numer['state']='normal'
                numer.delete(0,END)
                numer['state']='disabled'

                B1['state']='disabled'
                B2['state']='disabled'
                B3['state']='disabled'

                Frame_main.destroy()

                frame_main.destroy()
                
                menu.configure(state="normal")
                OK['state']='normal'
                
                if man==2:
                    
                    
                    
                    nbprocs['state']='normal'
                    nbprocs.delete(0,END)
                    nbprocs['state']='disabled'
                    
                    Quantum['state']='normal'
                    Quantum.delete(0,END)
                    Quantum['state']='disabled'  
                   

                if man==1:

                    
                    nbprocs.config(text="")
                    
                    Quantum.config(text="")

                    


                              
            fenetre.menu= tk.StringVar(fenetre)
            menu= ttk.OptionMenu(fenetre,fenetre.menu,Li[6], *Li)
            menu.grid(row=4, column=3,columnspan=3,sticky='nsew',pady=10,padx=20,ipady=9
                      )

            def back():

                tmr.destroy()
                menu.destroy()
                deno.destroy()
                numer.destroy()
                ligne.destroy()
                tmrs.destroy()
                ttmenu.destroy()
                tt.destroy()
               
                OK.destroy()
                    
                ttprocs.destroy()
                nbprocs.destroy()
                ttQuantum.destroy()
                Quantum.destroy()
                affcase.destroy()
                titre.destroy()
                soustitre.destroy()
                GO.destroy()
                B1.destroy()
                B2.destroy()
                B3.destroy()
                B4.destroy()
                B5.destroy()
               
                if vis==1:
                    Frame_main.destroy()
                if visi==1:
                    frame_main.destroy()
                
                Chap2()

            def back2():

                tmr.destroy()
                menu.destroy()
                deno.destroy()
                numer.destroy()
                ligne.destroy()
                tmrs.destroy()
                ttmenu.destroy()
                tt.destroy()
                
                OK.destroy()
                ttprocs.destroy()
                nbprocs.destroy()
                ttQuantum.destroy()
                Quantum.destroy()
                affcase.destroy()
                titre.destroy()
                soustitre.destroy()
                GO.destroy()
                B1.destroy()
                B2.destroy()
                B3.destroy()
                B4.destroy()
                B5.destroy()
                
                if vis==1:
                    Frame_main.destroy()
                    
                if visi==1:
                    frame_main.destroy()
                
                Menu()
          
                      
            tmrs=Label(fenetre, text="Temps moyen de réponse", font=("Courier", 12), fg='black', bg='lightskyblue1')
            tmrs.grid(row=8, column=6,columnspan=7,sticky='w')

            deno=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le nombre de processus
            deno.grid(row=9,column=6,columnspan=7,sticky='n',ipady=7)

            numer=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le nombre de processus
            numer.grid(row=7,column=6,columnspan=7,sticky='n',ipady=7)

            ligne=Label(fenetre, text="—————————", font=("cadratin", 12), fg='black', bg='lightskyblue1')

            ligne.grid(row=8, column=6,columnspan=7,sticky='n',ipady=1)

            tmr=Button(fenetre, text="Valider\n saisie ", state='disabled',font=("calibri", 15,"bold",), fg='white', bg='steelblue', width=13, height=0,command=lambda:validerSaisie(Duree))
            tmr.grid(row=6, column=11,sticky='e')

            ttmenu=Label(fenetre, text="    Sélectionner le type d'ordonnancement \n     voulue", font=("Courier", 15, "italic"), fg='black', bg='lightskyblue1')
            ttmenu.grid(row=3, column=3,columnspan=3,sticky='w')


            tt=Label(fenetre, text="", font=("Courier", 20), fg='black', bg='lightskyblue1', width=33 ,height=7)
            tt.grid(column=2,row=6,columnspan=5,sticky='s')


            ##if man ==2:
                
            OK=Button(fenetre, text="Débloquer données", font=("calibri", 15, "bold",), fg='white', bg='steelblue', width=17, height=0,command=lambda:debloq())
            OK.grid(row=5, column=3,columnspan=3)

            ttprocs=Label(fenetre, text="Nombre de \nprocessus", font=("Courier", 15, "italic"), fg='black', bg='lightskyblue1')#titre pour le nombre de processus
            ttprocs.grid(row=3, column=5,columnspan=6,)


            if man==2:
                
                nbprocs=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le nombre de processus   

            else:
                nbprocs=Label(fenetre, text="", font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)
               

            nbprocs.grid(row=4, column=5,columnspan=6,ipady=15,ipadx=30)


            ttQuantum=Label(fenetre, text="Quantum", font=("Courier", 15, "italic"), fg='black', bg='lightskyblue1')#titre pour le quantum
            ttQuantum.grid(row=3, column=7,columnspan=8,)

            if man==2:
                
                Quantum=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le quantum

            else:
                
                Quantum=Label(fenetre, text="", font=("courier", 12, "italic"),fg='black', bg='white',width=10, height=1)


            Quantum.grid(row=4, column=7,columnspan=8,ipady=15,ipadx=30)

        
        
                
            GO=Button(fenetre, text="GO", font=("calibri", 18, "bold", 'underline'), fg='white', bg='steelblue',state='disabled', width=5, height=0,command=lambda:buttonGo(Type))
            GO.grid(row=4, column=10,columnspan=12)
         


            affcase=Button(fenetre, text="Afficher les cases",state='disabled', font=("calibri", 15, "bold"), fg='white', bg='steelblue', width=17, height=0,command=lambda:CreaCase())
            affcase.grid(row=8,column=3,columnspan=3)


            titre=Label(fenetre, text="Ordonnancement", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  
            soustitre=Label(fenetre, text="Quelques Indications: Nombres de processus compris entre 4-10\n                             Durée d’un processus entre 1-10, Quantum max 4", font=("courier", 15), fg='darkblue', bg='lightskyblue1')

            titre.grid(row=1, column=4,columnspan=7)
            soustitre.grid(row=2, column=3,columnspan=11,sticky='w',ipady=20,ipadx=50)

            B1=Button(fenetre, text="Rappel", font=("courier", 18, "bold", 'underline'), fg='white', bg='#103985',state='disabled', width=15, height=2,command=lambda:create())

            B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
             
            B3=Button(fenetre, text="Valider", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Valider())
             
            B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2,command=lambda:back2())
             
            B5=Button(fenetre, text="Quitter", font=("courier", 18), fg='white', bg='#103985', width=15, height=2,command=lambda:back())

            B1.grid(row=18, column=3,pady=10)
            B2.grid(row=18, column=5,pady=10)
            B3.grid(row=18, column=7,pady=10)
            B5.grid(row=18, column=9,pady=10)
            B4.grid(row=18, column=11,pady=10)

            ##############################################################Fenetre rappel####################################################################
            def create():
                      
                    types=fenetre.menu.get()
                        
                    rappel = Toplevel(fenetre)
                    rappel.config(background="lightskyblue1")
                 
                        
                    Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1').grid(row=1, column=1, columnspan=3)
                    
                    if types=='Tourniquet':
               
                        i="Tourniquet :\n"
                        a="Le processus sélectionné est celui en top de liste \net chaque nouveau processus est ajouté en fin de liste\n"
                        j="Un processus en cours s'exécute pendant un temps (q)\n et se met en fin de file s’il n’a pas fini \n"
                        c="L’arrivée d’un processus avec une plus grande priorité \nentraîne l’arrêt du processus en cours et s'exécute.\n"                      
                        
                    elif types=='FIFO':
                        
                        i="FIFO :\n"
                        a="FIFO = First-In, First-Out , le premier processus\n arrivé est le premier à s'exécuter\n"
                        j="Temps de réponse pour un processus = \nDate de fin - Date d'arrivée \n"
                        c="Temps moyen de réponse = somme des temps de réponse \nde chaque processus divisé par nombre de processus\n"                      
                        


                    elif types=='PCTER':
                        
                        i="PCTER :\n"
                        a="Le processus sélectionné est celui qui a le\n plus court temps d'exécution restant\n"
                        j="\n"
                        c="\n"                      
                        

                    elif types=='Priorite fixes':

                        i="Priorités fixes :\n"
                        a="Comparaison des processus pour trouver celui avec la plus grande priorité\n"
                        j="Respecter l’ordre de priorité : si une nouvelle tâche à une plus \n grande priorité le processus est interrompu\n"
                        c="Lorsque deux processus ont la même priorités, la règle du FIFO s’applique\n"                      


                    else :

                        i="Algorithmes multifiles :\n"
                        a="Quand une file est ordonnancée par un quantum n elle applique \n son algorithme d'ordonnancement pendant n unités de temps\n\n\n sauf si elle se retrouve vide avant l'expiration du quantum \ndans ce cas la file suivante prend le relai \n\n\n Quand une file est interrompue, elle reprend là où elle en était \n donc si un processus navait pas fini son quantum, il le termine.\n"
                        j="FIFO = First-In, First-Out , le premier processus\n arrivé est le premier à s'exécuter\n"
                        e="Migration"
                        c="Une fois qu'un processus c'est éxcuter 1 fois il passe à la file suivante"
                        
                        Label(rappel, text=e, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16,'bold')).grid(row=7, column=1, columnspan=3)
                      
                        
                   
                   
                    
                    Label(rappel, text=i, bg='lightskyblue1', fg='darkslateblue', font=('Courier',20,'bold')).grid(row=4, column=1, columnspan=3)                   
                    Label(rappel, text=a, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=5, column=1, columnspan=3)
                                
                          
                    Label(rappel, text=j, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=6, column=1, columnspan=3)

                    Label(rappel, text=c, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=8, column=1, columnspan=3)
                    
                    
                   

                    rappel.rowconfigure(1, weight=1)
                    rappel.rowconfigure(2, weight=1)
                    rappel.rowconfigure(3, weight=1)
                    rappel.rowconfigure(4, weight=1)
                    rappel.rowconfigure(5, weight=1)
                    rappel.rowconfigure(6, weight=1)
                    rappel.rowconfigure(7, weight=1)
                    rappel.rowconfigure(8, weight=1)
                    rappel.rowconfigure(9, weight=1)
                    rappel.rowconfigure(10, weight=1)
                    rappel.rowconfigure(11, weight=1)
                    rappel.rowconfigure(12, weight=1)

                    rappel.columnconfigure(1, weight=0)
                    rappel.columnconfigure(2, weight=1)
                    rappel.columnconfigure(3, weight=0)    

                    def exit_btn():

                        rappel.destroy()
                        rappel.update()

                    btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
                    btn.grid(row=12, column=1,columnspan=3,sticky='n')


        


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
    tMenu=Label(fenetre, text= "  Bienvenue sur l'application d'entrainement", font=("Courier", 35, "italic"), fg='blue4', bg='lightskyblue1')
    tMenu.grid(row=1, column=2, columnspan=3,ipady=40)
    stMenu=Label(fenetre, text= "     Séléctionner le module que vous souhaitez travailler", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    stMenu.grid(row=2, column=2, columnspan=3,ipady=40)
    
    Bchap1=Button(fenetre, text="   Codage de l'information", font=("courier", 18, "italic"), fg='white', bg='#103985', command = Chap1)
    Bchap1.grid(row=4, column=3,sticky='e',ipady=10,ipadx=231)

    Bchap2=Button(fenetre, text="Ordonnancement", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap2)#command= Chap2
    Bchap2.grid(row=6, column=3,sticky='e',ipady=10,ipadx=315)

    Bchap3=Button(fenetre, text="Gestion de la mémoire", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap3)#command= Chap3
    Bchap3.grid(row=8, column=3, sticky='e',ipady=10,ipadx=266)

    Bchap4=Button(fenetre, text="Gestion de fichier", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap4) #command= Chap4
    Bchap4.grid(row=10, column=3,sticky='e',ipady=10,ipadx=287)
    
    Quitter=Button(fenetre, text= "Quitter", font=("courier", 18, "italic"), fg='white', bg='#103985', command= fenetre.destroy)
    Quitter.grid(row=17, column=3,columnspan=4,ipadx=20)




Menu()

fenetre.mainloop()

