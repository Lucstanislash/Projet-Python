from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
from random import*
from tkinter import messagebox


###===================================== L'aléatoire =====================================#
def NumVirgule(base):
    liste = []
    if base == 2:
        entier = AleaExAll(2, 1, 27)#32 - 5 = 27 max (Nombre avant la virgule)
        liste.append(entier)
        while 1:
            dec = AleaExAll(2, 1, 5)
            if '1' in dec :
                liste.append(dec)
                break
        ch = '.'.join(liste)
        return(ch) #ajoute une virgule
    elif base == 10:
        entier = uniform(1,10000)
        entier = round(entier,randrange(1,5))
        return str(entier)	
 
#==========================================================================#
#Fonction qui permet de convertir les entiers décimaux en binaire décimaux
def dec_bin(decimal,ApresVirg):
    entier, dec = str(decimal).split('.')
    entier = int(entier)
    dec = '0.' + dec
    dec = float(dec)
    resultat = str(bin(entier).lstrip("0b")+'.')
    ApresVirg = int(ApresVirg)
	# Nombre après la virgule
    for i in range(ApresVirg):
        dec *= 2
        if dec < 1 :
            resultat += '0'
        else :
            resultat += '1'
            dec -= 1
    return resultat


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

def AleaApresVirg():
    ApresVirg = randint(1,6)
    return str(ApresVirg)

def AleaEx6():
    ordre=AleaEx6_Ordre(lischoix)
    if ordre=='2':
            valeur=NumVirgule(10)
    else:     
            valeur=NumVirgule(2)
            
    return(valeur,ordre)


def count_decimaux(nombre, choix):
    n = nombre[::-1].find('.')
    if choix == 'resultat':
        return(n)
    elif choix == 'ctrlsynth':
        if n > 5 :
            return(True)
    
#==========================================================================================#
fenetre=Tk()
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

man = 1
ordre = ""
if man == 1 :
    alea=AleaEx6()
    aleavirg = AleaApresVirg()
    ordre = alea[1]
    valeur = alea[0]
    
def get(ordre):
    if man == 2:
        entier = saisieVal.get()
        apresvirgule = saisieVirg.get()
        util = Resultats.get()
        ordre = fenetre.option_var.get()
    else:
        entier = valeur
        apresvirgule = aleavirg
        nb_apres = count_decimaux(entier, 'resultat')
        util = Resultats.get()

    if apresvirgule > '5' :
        messagebox.showerror("showerror", "Il ne faut pas excéder 5 nombres après la virgule")
        return(1)

    if ordre == "10":
        ok = CtrlSyntaxe(str(entier),2,1,32)
        ok2 = CtrlSyntaxe(util,10,1,20,0,10000)
        ok3 = count_decimaux(entier, 'ctrlsynth')
        if ok == False or ok2 == False:
            messagebox.showerror("showerror", "Mauvaise saisie")
            return(1)
        elif ok3 == True:
            messagebox.showerror("showerror", "Maximum de bits après la virgule est : 5")
            return(1)
    else:
        ok = CtrlSyntaxe(entier,10,1,20,0,10000)
        ok2 = CtrlSyntaxe(util,2,1,32)
        ok3 = count_decimaux(entier, 'ctrlsynth')
        if ok == False or ok2 == False:
            messagebox.showerror("showerror", "Mauvaise saisie")
            return(1)
        elif ok3 == True:
            messagebox.showerror("showerror", "Maximum de nombres après la virgule est : 5")
            return(1)
        
    if man == 2:
        if ordre == "10":
            rep = bin_dec(entier,apresvirgule)
        else:
            rep = dec_bin(entier,apresvirgule)
    else :
        if ordre == "10":
            rep = bin_dec(entier,aleavirg)
        else:
            rep = dec_bin(entier,aleavirg)
    
    Verif = VerifRep(rep,util)
    
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
       
#------------------------------------------------------------------------------------------------------------#

OptionsExo6 = ("Base 2","Base 10")


titre=Label(fenetre, text="Les Décimaux", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')  # Placement de l'invite

soustitre=Label(fenetre, text="Quelques Indications: ", font=("courier", 25), fg='darkblue', bg='lightskyblue1') 



txt1=Label(fenetre, text="Décimal à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
if man==2:
    saisieVal=Entry(fenetre) 
    val=StringVar(fenetre) # variable qui récupérera la valeur de la case à cocher
else:
    saisieVal=Label(fenetre, text=valeur, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)


txt2=Label(fenetre, text="Convertir au format", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')

if man==2:
    fenetre.option_var= tk.StringVar(fenetre)
    w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo6[0], *OptionsExo6)
else:
    w1=Label(fenetre, text=ordre, font=("courier", 15, "italic"), fg='black', bg='white',width=4, height=1)


txt3=Label(fenetre, text="Nombres après la virgule", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
if man == 2 :
    val = IntVar(fenetre)
    saisieVirg=Entry(fenetre)
else:
    saisieVirg = Label(fenetre, text=aleavirg, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)


txt4=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats


imgEx6 = PhotoImage(file="img_ex6.gif")
    
#======================================================================================================================#
def create(imgEx6):
    rappel = Toplevel(fenetre)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')
    

    txt1=Label(rappel, text="Binaire en Base 10 :", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="Les bits avant la virgule correspondent à des puissance positifs de la base,\n alors que les bits après la virgule correspondent à des puissances négatives de la base  :", font=("courier", 17, "italic"), fg='black', bg='lightskyblue1', height=2)
    txt3=Label(rappel, text="10.101(2) = 2**1 + 2**(-1) + 2**(-3) \n= 2 + 0.5 + 0.125 = 2.625", font=("courier", 15, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
    txt4=Label(rappel, text="Base 10 en Binaire :", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt5=Label(rappel, text="Pour convertir en binaire on utilise la méthode de la multiplication de manière\nà ce que l'on multiplie par 2 le nombre après la virgule tel que:", font=("courier", 15, "italic"), fg='black', bg= 'lightskyblue1', height=2)
    bt= Label(rappel, image = imgEx6)

    txt1.grid(row=2, column=3)
    txt2.grid(row=3, column=3)
    txt3.grid(row=4, column=3)
    txt4.grid(row=5, column=3)
    txt5.grid(row=6, column=3)
    bt.grid(row=7, column=3)
    


    rappel.rowconfigure(1, weight=1)
    rappel.rowconfigure(2, weight=1)
    rappel.rowconfigure(3, weight=1)
    rappel.rowconfigure(4, weight=1)
    rappel.rowconfigure(5, weight=1)
    rappel.rowconfigure(6, weight=1)
    rappel.rowconfigure(7, weight=1)
    rappel.rowconfigure(8, weight=1)

    rappel.columnconfigure(1, weight=0)
    rappel.columnconfigure(2, weight=1)
    rappel.columnconfigure(3, weight=1)
    rappel.columnconfigure(4, weight=1)
    rappel.columnconfigure(5, weight=1)
    rappel.columnconfigure(6, weight=1)
    rappel.columnconfigure(7, weight=1)
    rappel.columnconfigure(8, weight=0)

    def exit_btn():

        rappel.destroy()
        rappel.update()

    btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
    btn.grid(row=8, column=3,columnspan=3,sticky='n')

def nouveau():
    B3['state']='normal'
    B2['state']='disabled'
    if man ==1 :
        alea=AleaEx6()
        ordre=alea[1]
        aleavirg = AleaApresVirg()
        valeur=alea[0]
        saisieVal.config(text=valeur)
        w1.config(text=ordre)
        Resultats.delete(0,END)
    else:
        
       saisieVal.delete(0,END)
       Resultats.delete(0,END)

B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create(imgEx6))

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(ordre))
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,state='disabled')
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fenetre.destroy)

titre.grid(row=1, column=2,columnspan=3)
soustitre.grid(row=2, column=1,columnspan=3,sticky='w',ipady=10)
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
B4.grid(row=7, column=4)
B5.grid(row=7, column=5)

fenetre.mainloop()
