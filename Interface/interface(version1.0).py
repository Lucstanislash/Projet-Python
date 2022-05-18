from tkinter import*
from functools import partial
fenetre=Tk()
fenetre.title("Application Python")
fenetre.geometry("700x500")
fenetre.minsize(500,600 )
#fenetre.iconbitmap("logo.ico")
fenetre.config(background='lightskyblue1')

cadre1=Frame(fenetre, bg='lightskyblue1')
cadre2=Frame(fenetre, bg='lightskyblue1')
cadre3=Frame(fenetre, bg='lightskyblue1')
cadre4=Frame(fenetre, bg='lightskyblue1')

#============== Fonctions globales =====================================

#la fonction PageChoix est à répéter 6 fois pour les exercise:
            #les entiés non signées (deja fais)
            #operation en binaire
            #operation sans calcul
            #décimaux
            #les rééls
            #les tableaux

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

    def back(): #Retour
        NomExo.destroy()
        txt3.destroy()
        button31.destroy()
        button32.destroy()
        button33.destroy()
        Chap1() #Retour à la page précédente: fenetre des exercices(2eme)
            # Création des buttons de la 3eme fenetre répondant à la QUESTION (saisie manuel ou aléatoire)
    NomExo = Label(cadre1, text= NomExercice, font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    NomExo.pack(expand=YES)
    txt3=Label(cadre2, text= "Souhaitez vous une saisie \n Manuel ou Aléatoire", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt3.pack(pady=20)
            
    button31=Button(cadre3, text="Manuel", font=("courier", 18, "italic"), fg='white', bg='#103985')
    button31.pack(fill=X, padx=10, ipadx= 25, ipady= 25, side='left')

    button32=Button(cadre3, text="Aléatoire", font=("courier", 18, "italic"), fg='white', bg='#103985')
    button32.pack(fill=X, padx=16, ipadx= 25, ipady= 25, side='right')

    button33=Button(cadre4, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=back)
    button33.pack(pady=10, fill=X)

#==================================================================================
#==============Menu c'est la fenetre principale contenant les 4 chapitres==========
#==================================================================================
    
def Menu():
    global Chap1
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
        
        tExoChap1 = Label(cadre1, text= "Codage de l'information", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap1.pack(expand=YES)
                    
        Bexo1=Button(cadre2, text="Entiers non signées", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        Bexo1.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=0, column=0)

        Bexo2=Button(cadre2, text="Opérations en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Opérations en binaire"))#command=affich3)
        Bexo2.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=1, column=0)

        Bexo3=Button(cadre2, text="Multiplications en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Multiplications en binaire"))
        Bexo3.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=2, column=0)

        Bexo4=Button(cadre2, text="Opérations sans calcul", font=("courier", 18, "italic"), fg='white', bg='#103985',width=largeur, height=hauteur , command= partial(PageChoix,"Opérations sans calcul"))#command=affich3)
        Bexo4.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=3, column=0)

        Bexo5=Button(cadre2, text="Entiers signées", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers signées"))
        Bexo5.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=0, column=1)

        Bexo6=Button(cadre2, text="Les Réels", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Réels"))
        Bexo6.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=1, column=1)

        Bexo7=Button(cadre2, text="Les Décimaux", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Décimaux"))#command=affich3)
        Bexo7.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=2, column=1)

        Bexo8=Button(cadre2, text="Les Tableaux", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= partial(PageChoix,"Les Tableaux"))
        Bexo8.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=3, column=1)

        Retour=Button(cadre4, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', width=largeur, height=hauteur ,command= back)
        Retour.pack(fill=X, pady=10)

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
        tExoChap2 = Label(cadre1, text= "Ordonnancement", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap2.pack(expand=YES)

        st = Label(cadre2, text= "Partie en cours de création", font=("Courier", 28, "italic"), fg='blue4', bg='lightskyblue1')
        st.pack(expand=YES)

        Retour=Button(cadre4, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command= back)
        Retour.pack(fill=X, pady=10)

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
        tExoChap3 = Label(cadre1, text= "Gestion de la mémoire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap3.pack(expand=YES)

        st = Label(cadre2, text= "Partie en cours de création", font=("Courier", 28, "italic"), fg='blue4', bg='lightskyblue1')
        st.pack(expand=YES)

        Retour=Button(cadre4, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command= back)
        Retour.pack(fill=X, pady=10)

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
        tExoChap4 = Label(cadre1, text= "Gestion de fichier", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExoChap4.pack(expand=YES)

        st = Label(cadre2, text= "Partie en cours de création", font=("Courier", 28, "italic"), fg='blue4', bg='lightskyblue1')
        st.pack(expand=YES)

        Retour=Button(cadre4, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command= back)
        Retour.pack(fill=X, pady=10)

        
    #============Création des chapitres de la 1ere fenetre    
    tMenu=Label(cadre1, text= "Bienvenue sur l'application d'entrainement", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    tMenu.pack(pady=25)
    stMenu=Label(cadre1, text= "Séléctionner le module que vous souhaitez travailler", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    stMenu.pack(pady=20)
    
    Bchap1=Button(cadre2, text="Codage de l'information", font=("courier", 18, "italic"), fg='white', bg='#103985', command = Chap1)
    Bchap1.pack(pady=25, fill=X, padx=100)

    Bchap2=Button(cadre2, text="Ordonnancement", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap2)#command= Chap2
    Bchap2.pack(pady=25, fill=X, padx=100)

    Bchap3=Button(cadre2, text="Gestion de la mémoire", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap3)#command= Chap3
    Bchap3.pack(pady=25, fill=X, padx=100)

    Bchap4=Button(cadre2, text="Gestion de fichier", font=("courier", 18, "italic"), fg='white', bg='#103985', command= Chap4) #command= Chap4
    Bchap4.pack(pady=25, fill=X, padx=100)
    
    Quitter=Button(cadre4, text= "Quitter", font=("courier", 18, "italic"), fg='white', bg='#103985', command= fenetre.destroy)
    Quitter.pack(fill=X, pady=10)




Menu()

cadre1.pack(expand=YES)
cadre2.pack(expand=YES)
cadre3.pack(expand=YES)
cadre4.pack(expand=YES)

fenetre.mainloop()
