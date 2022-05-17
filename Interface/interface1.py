
from tkinter import*
fenetre=Tk()
fenetre.title("Application Python")
#fenetre.geometry("")
#fenetre.minisize( , )
fenetre.iconbitmap("logo.ico")
fenetre.config(background='lightskyblue1')

cadre1=Frame(fenetre, bg='lightskyblue1')
cadre2=Frame(fenetre, bg='lightskyblue1')
#cadre3=Frame(fenetre, bg='lightskyblue1')
cadre4=Frame(fenetre, bg='lightskyblue1')


def tab1():
    def tab2():
        txt1.destroy()
        txt2.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        
        label2 = Label(cadre1, text= "Codage de l'information", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        label2.pack(expand=YES)
        def back():
            label2.destroy()
            button1.destroy()
            button2.destroy()
            button3.destroy()
            button4.destroy()
            button5.destroy()
            button6.destroy()
            button7.destroy()
            button8.destroy()
            button9.destroy()
            tab1()

        button1=Button(cadre2, text="Entiers non signées", font=("courier", 18, "italic"), fg='white', bg='#103985')
        button1.pack(pady=10, fill=X, padx=10)

        button2=Button(cadre2, text="Opération en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
        button2.pack(pady=10, fill=X, padx=10)

        button3=Button(cadre2, text="Multiplication en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985')
        button3.pack(pady=10, fill=X, padx=10)

        button4=Button(cadre2, text="Opérations sans calcul", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
        button4.pack(pady=10, fill=X, padx=10)

        button5=Button(cadre2, text="Entiers signées", font=("courier", 18, "italic"), fg='white', bg='#103985')
        button5.pack(pady=10, fill=X, padx=10)

        button6=Button(cadre2, text="Les Réels", font=("courier", 18, "italic"), fg='white', bg='#103985')
        button6.pack(pady=10, fill=X, padx=10)

        button7=Button(cadre2, text="Les Décimaux", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
        button7.pack(pady=10, fill=X, padx=10)

        button8=Button(cadre2, text="Les Tableaux", font=("courier", 18, "italic"), fg='white', bg='#103985')
        button8.pack(pady=10, fill=X, padx=10)

        button9=Button(cadre4, text= "Menu principale", font=("courier", 18, "italic"), fg='white', bg='#103985', command= back)
        button9.pack(fill=X, pady=10)
        
## pour mettre les buttons sous forme de lignes et colomnes, faut utiliser 'grid' au lieu de 'pack'
##utiliser row et comumn à l'interieur, pady padx ipadx ipady ...
        ### http://tkinter.fdex.eu/doc/gp.html ###
        
##        button1=Button(cadre2, text="Entiers non signées", font=("courier", 18, "italic"), fg='white', bg='#103985')
##        button1.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=0, column=0)
##
##        button2=Button(cadre2, text="Opération en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
##        button2.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=1, column=0, width=200)
##
##        button3=Button(cadre2, text="Multiplication en binaire", font=("courier", 18, "italic"), fg='white', bg='#103985')
##        button3.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=2, column=0)
##
##        button4=Button(cadre2, text="Opérations sans calcul", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
##        button4.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=3, column=0)
##
##        button5=Button(cadre2, text="Entiers signées", font=("courier", 18, "italic"), fg='white', bg='#103985')
##        button5.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=0, column=1)
##
##        button6=Button(cadre2, text="Les Réels", font=("courier", 18, "italic"), fg='white', bg='#103985')
##        button6.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=1, column=1, )
##
##        button7=Button(cadre2, text="Les Décimaux", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
##        button7.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=2, column=1)
##
##        button8=Button(cadre2, text="Les Tableaux", font=("courier", 18, "italic"), fg='white', bg='#103985')
##        button8.grid(ipady=25, ipadx=25, pady=10,padx= 25, row=3, column=1)
##
        
    txt1=Label(cadre1, text= "Bienvenue sur l'application d'entrainement", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    txt1.pack(pady=25)
    txt2=Label(cadre1, text= "Séléctionner le module que vous souhaitez travailler", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt2.pack(pady=20)
    b1=Button(cadre2, text="Codage de l'information", font=("courier", 18, "italic"), fg='white', bg='#103985', command = tab2)
    b1.pack(pady=25, fill=X, padx=100)

    b2=Button(cadre2, text="Ordonnancement", font=("courier", 18, "italic"), fg='white', bg='#103985')
    b2.pack(pady=25, fill=X, padx=100)

    b3=Button(cadre2, text="Gestion de la mémoire", font=("courier", 18, "italic"), fg='white', bg='#103985')#command=affich3)
    b3.pack(pady=25, fill=X, padx=100)

    b4=Button(cadre2, text="Gestion de fichier", font=("courier", 18, "italic"), fg='white', bg='#103985') #command=affich4)
    b4.pack(pady=25, fill=X, padx=100)
    
    b5=Button(cadre4, text= "Quitter", font=("courier", 18, "italic"), fg='white', bg='#103985', command= fenetre.destroy)
    b5.pack(fill=X, pady=10)

tab1()

cadre1.pack(expand=YES)
cadre2.pack(expand=YES)
#cadre3.pack(expand=YES)
cadre4.pack(expand=YES)

fenetre.mainloop()

