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
def dec_bin(decimal,Apres = 5):
    entier, dec = str(decimal).split('.')
    entier = int(entier)
    dec = '0.' + dec
    dec = float(dec)
    resultat = str(bin(entier).lstrip("0b")+'.')
	# Nombre après la virgule
    for i in range(Apres):
        dec *= 2
        if dec < 1 :
            resultat += '0'
        elif dec > 1 :
            resultat += '1'
            dec -= 1
    return resultat


#=========================================================================#
#Fonction qui permet de convertir les binaires décimaux en entier décimaux      
def bin_dec(binaire,Apres = 5):
    #on sépare l'entier et le décimal en deux variables distinctes
    entier, dec = str(binaire).split('.')
    entier = int(entier,2)
    resultat = entier
    val = 0.0
    puis = 0.5
    for i in dec: 
        if i =='1':
            val += puis
        puis /= 2
    resultat += (val)
    resultat = '%.*f' % (Apres, resultat)
    return str(resultat)
    

#=========================================================================#
lischoix = [ '10','2']

def  AleaEx6_Ordre(lischoix):
        #aléatoire de l'ordre
        choix = choice(lischoix)
        return(choix)


def AleaEx6():
    ordre=AleaEx6_Ordre(lischoix)
    if ordre=='2':
            valeur=NumVirgule(10)
    else:     
            valeur=NumVirgule(2)
    return(valeur,ordre)


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

man = 2
ordre = ""
if man == 1 :
    alea=AleaEx6()
    ordre=alea[1]
    valeur=alea[0]
    
def get(ordre):
    if man == 2:
        entier = saisieVal.get()
        apresvirgule = saisieVirg.get()
        util = Resultats.get()
        ordre = fenetre.option_var.get()
    else:
        entier = valeur
        util = Resultats.get()

    if apresvirgule > '5' :
        messagebox.showerror("showerror", "Mauvaise saisie")
        return(1)

    if ordre == "10":
        ok = CtrlSyntaxe(str(entier),2,1,32)
        ok2 = CtrlSyntaxe(util,10,1,20,0,10000)
        if ok == False or ok2 == False:
            messagebox.showerror("showerror", "Mauvaise saisie")
            return(1)
    else:
        ok = CtrlSyntaxe(entier,10,1,20,0,10000)
        ok2 = CtrlSyntaxe(util,2,1,32)
        if ok == False or ok2 == False:
            messagebox.showerror("showerror", "Mauvaise saisie")
            return(1)
    
    if ordre == "10":
        rep = bin_dec(entier,apresvirgule)
    else:
        rep = dec_bin(entier,apresvirgule)
    
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
#----------------------------------------------------------------------------------------------

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

##val.set(OptionsExo6[0]) # default value
##w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo6[0], *OptionsExo6)
if man==2:
    fenetre.option_var= tk.StringVar(fenetre)
    w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo6[0], *OptionsExo6)
else:
    w1=Label(fenetre, text=ordre, font=("courier", 15, "italic"), fg='black', bg='white',width=4, height=1)


txt3=Label(fenetre, text="Nombres après la virgule", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
if man == 2 :
    saisieVirg=Entry(fenetre) #ERREUR - faut que ça le lise en tant que integer
    val = IntVar(fenetre)
else:
    saisieVirg = Label(fenetre, text=valeur, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)


txt4=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats


#========================================================================#




B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

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
