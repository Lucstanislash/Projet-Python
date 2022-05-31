from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox


def Ent_IEEE(floatt):
    """fonction qui transforme un entier en IEEE"""
##conversion float vers entier##
    entier=int(float(floatt))
## conversion entier vers binaire##
    
    binaire= format(entier,'b')
    if int(entier)<0:
        binaire=binaire.replace("-","")    

## on sépare la chaine en 2 le bit implicite dans la première le reste dans l'autre
    ch_imp=binaire[0]
    ch_rest=binaire[1:]

## calcul de exposant puis conv vers binaire
    Exp=127+(len(ch_rest))
 
    ExpB= format(Exp,'b')
     
## calcul de la taille de la mantisse pour les décimaux
    FMantisse= 32-(len(ExpB)+len(binaire))

#transforme la partie décimal d'un float en binaire avec pour longueur FMantisse
    ch_dec=""
    dec=str(float(floatt)).replace(str(int(float(floatt))),'0')

    for i in range(FMantisse):
        dec=float(dec)*2
        if int(dec) >= 1:
            dec-=1
            ch_dec+='1'
        else:
            ch_dec+='0'
##concaténation des diff chaines 
    IEEE=ch_imp+ExpB+ch_rest+ch_dec
    Hexa=Conv(2,16,IEEE)
    Hexa= Hexa.upper()
    return(Hexa)

###IEEE=Ent_IEEE(floatt)


def IEE_Ent(Hexa):
    """fonction qui transforme un IEEE en entier"""
    IEEE=Conv(16,2,Hexa)
    
## récupère  l'exposant en binaire et le bim implicite
    ExpB=IEEE[1:9]
    ch_imp=IEEE[0]
    
## conversion en entier puis - 127 pour déterminer l'exposant
    Exp=int(ExpB,2)

    Exp=Exp-127

##récupère les bits de la valeur de l'entier
    n=Exp+9
    ch_rest=IEEE[9:n]
    finIEEE=IEEE[n:]

## reconstitue la chaine en binaire de l'entier puis conversion de entier
    
    binaire=ch_imp+ch_rest
    entier=int(binaire,2)
    
    if ch_imp[0]=="1":
        entier='-'+str(entier)

    cpt=0
    dec=0
    for i in finIEEE:
        cpt-=1
        if i=='1':
            dec+=2**cpt
    dec=round(dec,2)
    
    rep=str(dec).replace("0",entier)  
    return(rep)

lis=["IEEE","entier"]

def  AleaFormat5(lis):
        """Sort aléatoirement une valeur entre 1 et 2 pour choisir la base dans la liste li"""
        i=randrange(0,2)
        formats=lis[i]
        return(formats)
    
def AleaEx7Ent():
    entier=random.uniform(-1000,10000)
    entier=round(entier,2)
    return(entier)
   
def AleaEx7IEEE():   

    Hexa=AleaExAll(16,8,8)
    return(Hexa)

def SaisieAllEx7():
    formats=AleaFormat5(lis)
    if formats=="entier":
            valeur=AleaEx7IEEE()
            
    else:     
            valeur=AleaEx7Ent()
            
    return(valeur,formats)

fenetre=tk.Tk()
fenetre.config(background="lightskyblue1")


fenetre.rowconfigure(1, weight=0)
fenetre.rowconfigure(2, weight=0)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=1)

fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=1)
man=2
formats=""
if man ==1 :
    alea=SaisieAllEx7()
    formats=alea[1]
    valeur=alea[0]
    
def get(formats):
    if man==2:
        entier = saisieVal.get()
        util = Resultats.get()
        formats = fenetre.option_var.get()
    else:
        entier=valeur
        util = Resultats.get()

    if formats=="IEEE":
        ok=CtrlSyntaxe(entier,10,1,20,-10000,10000)
        ok2=CtrlSyntaxe(util,16,1,8)
        if ok==False or ok2==False:
            messagebox.showerror("showerror", "Mauvaise saisie")
            return(1)
    else:
        ok=CtrlSyntaxe(entier,16,1,8)
        ok2=CtrlSyntaxe(entier,10,1,20,-10000,10000)
        if ok==False or ok2==False:
            messagebox.showerror("showerror", "Mauvaise saisie")
            return(1)
    
    if formats=="IEEE":
        rep=Ent_IEEE(entier)

    else:
        rep=IEE_Ent(entier)
    
    Verif=VerifRep(rep,util)
    
    if Verif == 1:
        B3['state']='disabled' #bloquer le bouton valider ==> Gagner
        B2['state']='normal'
        resu=Label(fenetre, text="Bonne Réponse, Bravo !! ", font=("courier", 25, "italic"), fg='green', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    elif Verif == -1:
        B3['state']='disabled' #bloquer le bouton valider ==> Perdu
        B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
        resu=Label(fenetre, text="Vous avez perdu ! Le résultat est :", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1')
    elif Verif == 0:
        resu=Label(fenetre, text="Mauvaise réponse, réessayer ! ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
    resu.grid(row=5,column=1,columnspan=4,sticky='s')


OptionsExo1 = ("IEEE","entier")


titre=Label(fenetre, text="Les réels", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')  # Placement de l'invite

soustitre=Label(fenetre, text="Quelques Indications: ", font=("courier", 25), fg='darkblue', bg='lightskyblue1') 



txt1=Label(fenetre, text="Réel à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
if man==2:
    
    saisieVal=Entry(fenetre) 
    val=StringVar(fenetre) # variable qui récupérera la valeur de la case à cocher

else:
    saisieVal=Label(fenetre, text=valeur, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)



txt2=Label(fenetre, text="Convertir au format", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
if man==2:
   
    fenetre.option_var= tk.StringVar(fenetre)
    w1 = ttk.OptionMenu(fenetre,fenetre.option_var,OptionsExo1[0], *OptionsExo1)
else:
    w1=Label(fenetre, text=formats, font=("courier", 15, "italic"), fg='black', bg='white',width=4, height=1)



txt3=Label(fenetre, text="Résultat", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')

Resultats=Entry(fenetre) #width= largeur, height= hauteur) # Création de la zone de résultats


        

def create():
    rappel = Toplevel(fenetre)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')

    txt1=Label(rappel, text="1 bit de signe", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="8 bits d’exposant biaisé (biaisé de 127)", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt3=Label(rappel, text="23 bits de mantisse", font=("courier", 25, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
    txt4=Label(rappel, text="Ne pas oublier le bit implicite", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

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
    B3['state']='normal'
    B2['state']='disabled'
    if man ==1 :
        alea=SaisieAllEx7()
        formats=alea[1]
        valeur=alea[0]
        saisieVal.config(text=valeur)
        w1.config(text=formats)
        
B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:get(formats))
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2)

titre.grid(row=1, column=2,columnspan=3)
soustitre.grid(row=2, column=1,columnspan=3,sticky='w',ipady=40)
txt1.grid(row=3, column=1,columnspan=2,sticky='w',ipady=40)
saisieVal.grid(row=3, column=2,ipadx=200,columnspan=4,ipady=10)

txt2.grid(row=4, column=1,columnspan=2,sticky='w')
txt3.grid(row=5, column=1,columnspan=2,sticky='w',ipady=40)
w1.grid(row=4, column=2,ipadx=235,columnspan=4,ipady=10)
Resultats.grid(row=5, column=2,ipadx=200,columnspan=4,ipady=10)



#bouton#
B1.grid(row=6, column=1)
B2.grid(row=6, column=2)
B3.grid(row=6, column=3)
B4.grid(row=6, column=4)
B5.grid(row=6, column=5)

fenetre.mainloop()
