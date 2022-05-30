    NomExo = Label(fenetre, text= NomExercice, font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    NomExo.grid(row=1, column=1, columnspan=5)
    txt3=Label(fenetre, text= "Souhaitez vous une saisie Manuelle ou Aléatoire", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt3.grid(row=3, column=1, columnspan=5)
            
    bManuelle=Button(fenetre, text="Manuel", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(CommandExo,'Manuel'))
    bManuelle.grid(row=5, column=2, ipady=20, ipadx=100)

    bAléa=Button(fenetre, text="Aléatoire", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Aléa'))
    bAléa.grid(row=5, column=4, ipady=20,ipadx=100)

    bRetour=Button(fenetre, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(back,2))
    bRetour.grid(row=7, column=3)
