
from tkinter import*
fenetre=Tk()
fenetre.title("Application Python")
fenetre.geometry("700x500")
fenetre.minsize(500,600 )
fenetre.iconbitmap("logo.ico")
fenetre.config(background='lightskyblue1')

cadre1=Frame(fenetre, bg='lightskyblue1')
cadre2=Frame(fenetre, bg='lightskyblue1')
cadre3=Frame(fenetre, bg='lightskyblue1')
cadre4=Frame(fenetre, bg='lightskyblue1')

########## Menu est la fenetre principale contenant les 4 chapitres
def Menu():
    def Chap1(): ######### Chap1 est la 2eme fenetre contenant les 8 exercices
        tMenu.destroy() # pour détruire les buttons du fenetre1
        stMenu.destroy()
        Bchap1.destroy()
        Bchap2.destroy()
        Bchap3.destroy()
        Bchap4.destroy()
        Quitter.destroy()
        # Command est la fonction produite en cliquant sur chaque exercice
        def command1(): #Exercice1
            tExo.destroy() # pour détruire les buttons du fenetre2
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
                label3.destroy()
                txt3.destroy()
                button31.destroy()
                button32.destroy()
                button33.destroy()
                Chap1() #Retour à la page précédente: fenetre des exercices(2eme)
            # Création des buttons de la 3eme fenetre répondant à la QUESTION (saisie manuel ou aléatoire)
            label3 = Label(cadre1, text= "NOM EXO", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
            label3.pack(expand=YES)
            txt3=Label(cadre2, text= "Souhaitez vous une saisie \n Manuel ou Aléatoire", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
            txt3.pack(pady=20)
            
            button31=Button(cadre3, text="Manuel", font=("courier", 18, "italic"), fg='white', bg='#103985')
            button31.pack(fill=X, padx=10, ipadx= 25, ipady= 25, side='left')

            button32=Button(cadre3, text="Aléatoire", font=("courier", 18, "italic"), fg='white', bg='#103985')
            button32.pack(fill=X, padx=16, ipadx= 25, ipady= 25, side='right')

            button33=Button(cadre4, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=back)
            button33.pack(pady=10, fill=X)


        #la fonction command est à répéter 6 fois pour les exercise:
            #les entiés non signées (deja fais)
            #operation en binaire
            #operation sans calcul
            #décimaux
            #les rééls
            #les tableaux


        def back(): # Retour
            tExo.destroy()
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
            
        # Création des exercices de la 2eme fenetre        
        tExo = Label(cadre1, text= "Codage de l'information", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        tExo.pack(expand=YES)
                    
        Bexo1=Button(cadre2, text="Entiers non signées", font=("courier", 18, "italic"), fg='white', bg='#103985', command= command1)
        Bexo1.pack(pady=10, fill=X, padx=10)

        Bexo2=Button(cadre2, text="Opération en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
        Bexo2.pack(pady=10, fill=X, padx=10)

        Bexo3=Button(cadre2, text="Multiplication en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985')
        Bexo3.pack(pady=10, fill=X, padx=10)

        Bexo4=Button(cadre2, text="Opérations sans calcul", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
        Bexo4.pack(pady=10, fill=X, padx=10)

        Bexo5=Button(cadre2, text="Entiers signées", font=("courier", 18, "italic"), fg='white', bg='#103985')
        Bexo5.pack(pady=10, fill=X, padx=10)

        Bexo6=Button(cadre2, text="Les Réels", font=("courier", 18, "italic"), fg='white', bg='#103985')
        Bexo6.pack(pady=10, fill=X, padx=10)

        Bexo7=Button(cadre2, text="Les Décimaux", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
        Bexo7.pack(pady=10, fill=X, padx=10)

        Bexo8=Button(cadre2, text="Les Tableaux", font=("courier", 18, "italic"), fg='white', bg='#103985')
        Bexo8.pack(pady=10, fill=X, padx=10)

        Retour=Button(cadre4, text= "Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command= back)
        Retour.pack(fill=X, pady=10)


        
    # Création des chapitres de la 1ere fenetre    
    tMenu=Label(cadre1, text= "Bienvenue sur l'application d'entrainement", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    tMenu.pack(pady=25)
    stMenu=Label(cadre1, text= "Séléctionner le module que vous souhaitez travailler", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    stMenu.pack(pady=20)
    
    Bchap1=Button(cadre2, text="Codage de l'information", font=("courier", 18, "italic"), fg='white', bg='#103985', command = Chap1)
    Bchap1.pack(pady=25, fill=X, padx=100)

    Bchap2=Button(cadre2, text="Ordonnancement", font=("courier", 18, "italic"), fg='white', bg='#103985')
    Bchap2.pack(pady=25, fill=X, padx=100)

    Bchap3=Button(cadre2, text="Gestion de la mémoire", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
    Bchap3.pack(pady=25, fill=X, padx=100)

    Bchap4=Button(cadre2, text="Gestion de fichier", font=("courier", 18, "italic"), fg='white', bg='#103985') #command=affich4)
    Bchap4.pack(pady=25, fill=X, padx=100)
    
    Quitter=Button(cadre4, text= "Quitter", font=("courier", 18, "italic"), fg='white', bg='#103985', command= fenetre.destroy)
    Quitter.pack(fill=X, pady=10)

Menu()

cadre1.pack(expand=YES)
cadre2.pack(expand=YES)
cadre3.pack(expand=YES)
cadre4.pack(expand=YES)

fenetre.mainloop()

