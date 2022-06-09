from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
from random import*
from tkinter import messagebox

def Exercice6(f, select):
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

    fenetre.columnconfigure(0, weight=1)
    fenetre.columnconfigure(1, weight=1)
    fenetre.columnconfigure(2, weight=1)
    fenetre.columnconfigure(3, weight=1)
    fenetre.columnconfigure(4, weight=1)
    fenetre.columnconfigure(5, weight=1)
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
            ApresVirg = saisieVirg.get()          
            util = Resultats.get()
            formats = fenetre.option_var.get()
            
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
                        print(entier)
                        okEnt= count_decimaux(entier, 'resultat','5')
                        print(okEnt)
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
                            messagebox.showerror("showerror", "Erreur de saisie du résultat")
                            return(1)
            
            
        elif man==1:
            
            entier = valeur
            print("voici l'entier beach",entier)
            util = Resultats.get()
            formats=w1.cget("text")
            print("voici l'entier beach",formats)
            ApresVirg=saisieVirg.cget("text")
            print("voici l'entier beach",ApresVirg)

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
                        print(ok2)
                        print("miaou")
                    elif formats=='10':

                        ok2 = CtrlSyntaxe(util,10,1,20,1,10000)
                        print(ok2)
                        print("miamiaou")

                    else:
                        print("miaou bitch")
                
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
            
        
        elif man==1:

           alea=AleaEx6()
           ordre = alea[1]
           valeur = alea[0]
           virgule=AleaVirgule(ordre)
           
           Resultats.delete(0,END)

           saisieVal.config(text=valeur)
           saisieVirg.config(text=valeur)
           w1.config(text=valeur)
          
            
    #------------------------------------------------------------------------------------------------------------#

    OptionsExo6 = ("2","10")


    titre=Label(fenetre, text="Les Décimaux", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')  # Placement de l'invite

    soustitre=Label(fenetre, text="Quelques Indications: Base de départ 10 valeur --> 0 et 10 000, entre 1 et 6 bits après la virgule \n              Base de départ 2 --> max 5 bits après la virgule , valeur max 32 bits", font=("courier", 15), fg='darkblue', bg='lightskyblue1') 

    if man==1:
        if ordre=='10':    
            txt1=Label(fenetre, text="Binaire à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        else:
            txt1=Label(fenetre, text="Décimal à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        
    else:
            txt1=Label(fenetre, text="Valeur à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
           
       
    if man==2:
        saisieVal=Entry(fenetre) 
        val=StringVar(fenetre) # variable qui récupérera la valeur de la case à cocher
    else:
        saisieVal=Label(fenetre, text=valeur, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)


    txt2=Label(fenetre, text="Convertir au format", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')

    ##val.set(OptionsExo6[0]) # default value
    ##w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo6[0], *OptionsExo6)

    if man==2:
        fenetre.option_var= tk.StringVar(fenetre)
        w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo6[0], *OptionsExo6)
    else:
        w1=Label(fenetre, text=ordre, font=("courier", 15, "italic"), fg='black', bg='white',width=4, height=1)

    if man==1:
        if ordre=='10':
            txt3=Label(fenetre, text="Nombres après la virgule", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
        else:
            txt3=Label(fenetre, text="Bits après la virgule", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    else:
            txt3=Label(fenetre, text="Nombres après la virgule", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')

        
    if man == 2 :
        val = IntVar(fenetre)
        saisieVirg=Entry(fenetre) #ERREUR - faut que ça le lise en tant que integer
    else:
        saisieVirg = Label(fenetre, text=virgule, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)


    txt4=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
    Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats

    #======================================================================================================================#
    def create():
        rappel = Toplevel(fenetre)
        rappel.config(background="lightskyblue1")
        titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        titre.grid(row=1, column=2,columnspan=3,sticky='s')

        txt1=Label(rappel, text="Pour obtenir la partie décimale\non utilise la méthode de la multiplication.", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
      
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

    B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

    B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
     
    B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get())
     
    B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2)
     
    B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2,command=fenetre.destroy)

    titre.grid(row=1, column=2,columnspan=3)
    soustitre.grid(row=2, column=1,columnspan=4,ipady=10)
    txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=10)
    saisieVal.grid(row=3, column=2,ipadx=200,columnspan=4,ipady=10)

    txt2.grid(row=4, column=1,columnspan=2,sticky='w')
    w1.grid(row=4, column=2,ipadx=235,columnspan=4,ipady=10)

    txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=10)
    saisieVirg.grid(row=5, column=2,ipadx=200,columnspan=4,ipady=10)

    txt4.grid(row=6, column=1,columnspan=2,sticky='w',ipady=10)
    Resultats.grid(row=6, column=2,ipadx=200,columnspan=4,ipady=10)



    #bouton#
    B1.grid(row=7, column=1)
    B2.grid(row=7, column=2)
    B3.grid(row=7, column=3)
    B4.grid(row=7, column=5)
    B5.grid(row=7, column=4)


