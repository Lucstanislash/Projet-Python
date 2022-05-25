    NomExo = Label(fenetre, text= NomExercice, font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    NomExo.grid(row=1, column=2)
    txt3=Label(fenetre, text= "Souhaitez vous une saisie Manuelle ou Aléatoire", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    txt3.grid(row=1, column=2)
            
    bManuelle=Button(fenetre, text="Manuel", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(CommandExo,'Manuel'))
    bManuelle.grid(row=2, column=1)

    bAléa=Button(fenetre, text="Aléatoire", font=("courier", 18, "italic"), fg='white', bg='#103985',command=partial(CommandExo,'Aléa'))
    bAléa.grid(row=2, column=2)

    bRetour=Button(fenetre, text="Retour", font=("courier", 18, "italic"), fg='white', bg='#103985', command=partial(back,2))
    bRetour.grid(row=3, column=2)
