from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox

def Exercice8(f,select):
    fenetre=f
    fenetre.config(background="lightskyblue1")
    #fenetre.attributes('-fullscreen', True)

    fenetre.rowconfigure(1, weight=0)
    fenetre.rowconfigure(2, weight=2)
    fenetre.rowconfigure(3, weight=1)
    fenetre.rowconfigure(4, weight=1)
    fenetre.rowconfigure(5, weight=1)
    fenetre.rowconfigure(6, weight=1)
    fenetre.rowconfigure(7, weight=1)
    fenetre.rowconfigure(8, weight=1)
    fenetre.rowconfigure(9, weight=1)

    fenetre.columnconfigure(0, weight=1)
    fenetre.columnconfigure(1, weight=1)
    fenetre.columnconfigure(2, weight=1)
    fenetre.columnconfigure(3, weight=1)
    fenetre.columnconfigure(4, weight=1)
    fenetre.columnconfigure(5, weight=1)

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
            ok=CtrlSyntaxe(str(taille),10,1,10,30,300)
            ok2=CtrlSyntaxe(str(TailleC),10,1,10,1,300)
            ok3=CtrlSyntaxe(str(Adresse),10,1,100,1,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
            if ok==False or ok2==False or ok3==False:
                B6['state']='normal'
                messagebox.showerror(title="Information",
                            message="Mauvaise saisie")
                return(1)
            elif int(taille)*int(TailleC)>950:
                B6['state']='normal'
                messagebox.showerror(title="Information",
                            message="Mauvaise saisie")
                return(1)
                
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
        if donne==1:
            messagebox.showerror(title="Information",
                            message="Mauvaise saisie")
            B6['state']='normal'
            return(1)
        else:
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
                print("Miaou")
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
                if man==1:
                    ok=False
            else:
                ok=CtrlSyntaxe(i,10,0,200,0,100000000000000000000000000)
            if ok==False:
                messagebox.showerror(title="Information",
                                message="Mauvaise saisie")
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
                                message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n"
                                +"Nombres de mots:"
                                + ("".join(rep[0]))
                                + "\n"
                                +"Numéro du premier mot: "
                                + ("".join(rep[1]))
                                + "\n"
                                +"Numéro du dernier mot: "
                                + ("".join(rep[2]))
                                + "\n"
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

    soustitre=Label(fenetre, text="Quelques Indications: La taille du tableau est comprise entre 30 et 300 cases \n                     Taille mot * taille case ne doit pas dépasser 950 mots ",font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

    txt1=Label(fenetre, text="Taille du tableau", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
    txt1a=Label(fenetre, text="(en nombre de case)", font=("courier", 12, "italic"), fg='black', bg='lightskyblue1')

    txt2=Label(fenetre, text="Taille d'une case", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
    txt2a=Label(fenetre, text="(en nombre de mot)", font=("courier", 12, "italic"), fg='black', bg='lightskyblue1')

    txt3=Label(fenetre, text="Adresse 1 mot ", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')
    txt4=Label(fenetre, text="Numéro de case", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1')

    txtQ10=Label(fenetre, text="Nombre de mots", font=("courier", 20), fg='black', bg='lightskyblue1')
    txtQu1=Label(fenetre, text="Question 1 :", font=("courier", 20, "bold"), fg='black', bg='lightskyblue1')
    txtQ11=Label(fenetre, text="Numéro du premier mot", font=("courier", 20), fg='black', bg='lightskyblue1')
    txtQ12=Label(fenetre, text="Numéro du dernier mot", font=("courier", 20), fg='black', bg='lightskyblue1')

    txtQ2=Label(fenetre, text="Mot contenus dans la case", font=("courier", 20), fg='black', bg='lightskyblue1')
    txtQu2=Label(fenetre, text="Question 2 :", font=("courier", 20, "bold"), fg='black', bg='lightskyblue1')

    if man ==2:
        
        TailleTab=Entry(fenetre,justify='center',borderwidth=3)

        TailleCase=Entry(fenetre,justify='center',borderwidth=3)

        AdPMTab=Entry(fenetre,justify='center',borderwidth=3)

    else:
        TailleTab=Label(fenetre, text=taille , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
        TailleCase=Label(fenetre, text=TailleC , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
        AdPMTab=Label(fenetre, text=Adresse , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)

        
    NumCase=Label(fenetre, text=donne2 , font=("courier", 15, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken")


    NbCTab=Entry(fenetre,justify='center')

    NumPTab=Entry(fenetre,justify='center') 
    NumDTab=Entry(fenetre,justify='center')

    MotCase=Entry(fenetre,justify='center') 



    def create():
        rappel = Toplevel(fenetre)
        rappel.config(background="lightskyblue1")
        titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='darkblue', bg='lightskyblue1')
        titre.grid(row=1, column=2,columnspan=3,sticky='s')

        txt1=Label(rappel, text="Si a est le premier mot du tableau,", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
        txt2=Label(rappel, text=" et si une case contient n mots,", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
        txt3=Label(rappel, text=" le premier mot de la case n°k", font=("courier", 20, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
        txt4=Label(rappel, text=" est le mot a+(k-1)*n", font=("courier", 20, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

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
            
           TailleTab.delete(0,END)
           TailleCase.delete(0,END)
           AdPMTab.delete(0,END)

           
           NbCTab.delete(0,END)
           NumPTab.delete(0,END) 
           NumDTab.delete(0,END)
           MotCase.delete(0,END)
            
    B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

    B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
     
    B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(donne))
     
    B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,state='disabled')
     
    B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fenetre.destroy)

    B6=Button(fenetre, text="Go!", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=16, height=0,command=lambda:control(donne,ko,taille,TailleC,Adresse))

    titre.grid(row=1, column=2,columnspan=3)
    soustitre.grid(row=2, column=1,columnspan=5,sticky='w')

    txt1.grid(row=3, column=1,columnspan=2,sticky='w')
    TailleTab.grid(row=3, column=2,ipady=10)

    txt1a.grid(row=3, column=1,sticky='s')

    txt2.grid(row=3, column=3,columnspan=4,sticky='w')
    TailleCase.grid(row=3,column=4,ipady=10)

    txt2a.grid(row=3, column=3,sticky='s')

    B6.grid(row=4, column=5,sticky='nw')

    txt3.grid(row=4, column=1,columnspan=2,sticky='w',ipady=30)
    AdPMTab.grid(row=4, column=2,ipady=10)

    txt4.grid(row=4,column=3,columnspan=4,sticky='w',ipady=30)
    NumCase.grid(row=4, column=4,ipady=10)

    txtQ10.grid(row=5, column=2,columnspan=3,sticky='w')
    NbCTab.grid(row=5, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

    txtQu1.grid(row=5, column=1,sticky='w')

    txtQ11.grid(row=6, column=2,columnspan=3,sticky='w')
    NumPTab.grid(row=6, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

    txtQ12.grid(row=7, column=2,columnspan=3,sticky='w')
    NumDTab.grid(row=7, column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')


    txtQ2.grid(row=8, column=2,columnspan=3,sticky='w')
    MotCase.grid(row=8,column=4,columnspan=5,ipadx=100,ipady=10,sticky='w')

    txtQu2.grid(row=8, column=1,sticky='w')



    #bouton#
    B1.grid(row=9, column=1)
    B2.grid(row=9, column=2)
    B3.grid(row=9, column=3)
    B4.grid(row=9, column=4)
    B5.grid(row=9, column=5)
