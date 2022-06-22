from tkinter import*

fenetre=Tk()
fenetre.rowconfigure(1, weight=1)
fenetre.rowconfigure(2, weight=1)
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
fenetre.columnconfigure(13, weight=1)
fenetre.columnconfigure(14, weight=1)
fenetre.columnconfigure(15, weight=1)


Duree=10
def CreaCase(Duree):
    colmin=5
    colmax=12
    lignemin=5
    lignemax=14
    col=0
    ligne=0
    ListNom=[]
    for i in range(Duree):
        Nom=str("a"+str(i))
        ListNom.append(Nom)
    print(ListNom)
    print(ListNom[1])
    for i in range(Duree):
        ListNom[i]=Entry(fenetre,width=10)
        ListNom[i].grid(row=lignemin+ligne, column=colmin+col, pady=20, columnspan=colmin+col )
        ValTemps=(str(i)+"-"+str(i+1))
        Temps=Label(fenetre, text=ValTemps ,font=("courier", 8), fg='black', bg='white')
        Temps.grid(row=lignemin+ligne, column=colmin+col,sticky='s', columnspan=colmin+col)
        
        if colmin+col>=colmax:
            col=0
            ligne+=1
        else:
            col+=1
    ListNom[3].configure(state="disabled")

B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='red',command=lambda:CreaCase(Duree))
B.grid(row=4, column=4)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='blue',command=lambda:CreaCase(Duree))
B.grid(row=5, column=4)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='green',command=lambda:CreaCase(Duree))
B.grid(row=6, column=4)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='yellow',command=lambda:CreaCase(Duree))
B.grid(row=7, column=4)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='purple',command=lambda:CreaCase(Duree))
B.grid(row=8, column=4)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='orange',command=lambda:CreaCase(Duree))
B.grid(row=9, column=4)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='brown',command=lambda:CreaCase(Duree))
B.grid(row=10, column=4)


B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='red',command=lambda:CreaCase(Duree))
B.grid(row=4, column=5)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='blue',command=lambda:CreaCase(Duree))
B.grid(row=5, column=5)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='green',command=lambda:CreaCase(Duree))
B.grid(row=6, column=5)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='yellow',command=lambda:CreaCase(Duree))
B.grid(row=7, column=5)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='purple',command=lambda:CreaCase(Duree))
B.grid(row=8, column=5)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='orange',command=lambda:CreaCase(Duree))
B.grid(row=9, column=5)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='brown',command=lambda:CreaCase(Duree))
B.grid(row=10, column=5)



B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='red',command=lambda:CreaCase(Duree))
B.grid(row=4, column=3)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='blue',command=lambda:CreaCase(Duree))
B.grid(row=5, column=3)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='green',command=lambda:CreaCase(Duree))
B.grid(row=6, column=3)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='yellow',command=lambda:CreaCase(Duree))
B.grid(row=7, column=3)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='purple',command=lambda:CreaCase(Duree))
B.grid(row=8, column=3)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='orange',command=lambda:CreaCase(Duree))
B.grid(row=9, column=3)
B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='brown',command=lambda:CreaCase(Duree))
B.grid(row=10, column=3)
        
fenetre.mainloop

