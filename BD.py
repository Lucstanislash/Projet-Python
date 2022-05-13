from tkinter import*
from pickle import *
from os import mkdir,chdir,getcwd,listdir
import os

#--------------------------------------Analyse----------------------------------------


def Analyse_enseignant():
    
    global UE 
    cadre=Frame(fen)
# Pour avoir une liste avec ascenseur - Utilisation du widget Scrollbar
    ascenseur=Scrollbar(cadre) 
# positionnement d'un déroulement vertical, barre de défilement à droite
    ascenseur.pack(side='right', fill=Y) 
    message=Label(cadre, text="Enseignant présent dans la faculté ")
    message.pack()
# définition de la zone d'affichage de la liste, et liaison avec l'ascenseur
    lesNoms=Listbox(cadre, yscrollcommand=ascenseur.set) 

    for u in UE:
        seq=str(u)
        seq+=" "+UE[u]['nom_enseignant']
        lesNoms.insert(END, seq)
    lesNoms.pack(side='left')
    ascenseur.config(command=lesNoms.yview) # configuration de l'ascenseur
    bfin=Button(cadre, text="OK",command= cadre.destroy)
    bfin.pack()
    cadre.pack()     

def Analyse_etudiant():

    global etu # dictionnaire des noms
    cadre=Frame(fen)
# Pour avoir une liste avec ascenseur - Utilisation du widget Scrollbar
    ascenseur=Scrollbar(cadre) 
# positionnement d'un déroulement vertical, barre de défilement à droite
    ascenseur.pack(side='right', fill=Y) 
    message=Label(cadre, text="profil de l'etudiant ")
    message.pack()
# définition de la zone d'affichage de la liste, et liaison avec l'ascenseur
    lesNoms=Listbox(cadre, yscrollcommand=ascenseur.set) 

    for e in etu:
        seq=str(e)
        seq+=" "+etu[e]["nom"]+" " +etu[e]["prenom"]
        lesNoms.insert(END, seq)
    lesNoms.pack(side='left')
    ascenseur.config(command=lesNoms.yview) # configuration de l'ascenseur
    bfin=Button(cadre, text="OK",command= cadre.destroy)
    bfin.pack()
    cadre.pack()

def Analyse_intitule():
    monEtu=()
    seq=[]
    def saisie_etu():
        nom=SaisieNom.get()
               
        ok = True
            
        if ok:
            monEtu=str(nom)
            
        for u in Suit:
            if monEtu==Suit[u]['nom']:
                cadre=Frame(fen)
                ascenseur=Scrollbar(cadre) 
                ascenseur.pack(side='right', fill=Y) 
                message=Label(cadre, text="intitulés des UE dans lequel l'étudiant est inscrit")
                message.pack()
                lesNoms=Listbox(cadre, yscrollcommand=ascenseur.set) 
                seq=" "+Suit[u]['intitule']
                lesNoms.insert(END, seq)
                lesNoms.pack(side='left')
                ascenseur.config(command=lesNoms.yview)
                bfin=Button(cadre, text="Quitter",command= cadre.destroy)
                bfin.pack()
                cadre.pack()
            
        SaisieNom.delete(0,END) 
        
    cadre=Frame(fen) 
    message=Label(cadre, text="Nom de l'étudiant") 
    message.pack()
    SaisieNom=Entry(cadre) 
    SaisieNom.pack()
    
    bval=Button(cadre, text="Valider", command=saisie_etu)
    bval.pack()
    bfin=Button(cadre, text="Quitter", command=cadre.destroy) 
    bfin.pack()
    cadre.pack()

def Analyse_vogue():
    
    global UE
    maxi=0        
    l={}

    cadre=Frame(fen)
    ascenseur=Scrollbar(cadre) 
    ascenseur.pack(side='right', fill=Y) 
    message=Label(cadre, text="intitulé de l'UE la plus suivie")
    message.pack()
    lesNoms=Listbox(cadre, yscrollcommand=ascenseur.set)
    for e in UE:
        l[UE[e]['nombre']]=UE[e]['intitule']
        print(l)
    for i in l:
        maxi=max(l)
    lesNoms.insert(END,l[maxi])
           
    lesNoms.pack(side='left')
    ascenseur.config(command=lesNoms.yview)
    bfin=Button(cadre, text="Quitter",command= cadre.destroy)
    bfin.pack()
    cadre.pack() 
    

#----------------------Inscription\Relation-------------------------
    
def CadreSaisieSuit():
    def ajout():
        
        global Suit,etu,UE 
        nom=SaisieNom.get()
        intitule=SaisieUE.get()     

        ok = True
        for s in Suit:           
            if Suit[s]["nom"]==nom and Suit[s]["intitule"]==intitule:
                ok=False
                break
        
        else:
            for e in etu :
                if etu[e]["nom"]==nom:
                    for u in UE:
                        if UE[u]['intitule']==intitule:
                           UE[u]['nombre']+=1
                           indice=len(Suit) + 1
                           Suit[indice]={"nom":nom, "intitule":intitule}
                           break
                    break

                   
        SaisieNom.delete(0,END) 
        SaisieUE.delete(0,END)

    cadre=Frame(fen) 
    message=Label(cadre, text="Nom") 
    message.pack()
    SaisieNom=Entry(cadre) 
    SaisieNom.pack()
    
    message_prenom=Label(cadre, text="UE") 
    message_prenom.pack()
    SaisieUE=Entry(cadre)
    SaisieUE.pack()

    
    bval=Button(cadre, text="Valider", command=ajout) 
    bval.pack()
    bfin=Button(cadre, text="OK", command=cadre.destroy) 
    bfin.pack()
    cadre.pack()

    
def visu_Suit():
   
    global Suit
    cadre=Frame(fen)
# Pour avoir une liste avec ascenseur - Utilisation du widget Scrollbar
    ascenseur=Scrollbar(cadre) 
# positionnement d'un déroulement vertical, barre de défilement à droite
    ascenseur.pack(side='right', fill=Y) 
    message=Label(cadre, text=" UE suivi par l'etudiant ")
    message.pack()
# définition de la zone d'affichage de la liste, et liaison avec l'ascenseur
    lesNoms=Listbox(cadre, yscrollcommand=ascenseur.set) 

    for e in Suit:
        seq=str(e)
        seq+=" "+Suit[e]["nom"]+" " +Suit[e]["intitule"]
        lesNoms.insert(END, seq)
    lesNoms.pack(side='left')
    ascenseur.config(command=lesNoms.yview) # configuration de l'ascenseur
    bfin=Button(cadre, text="OK",command= cadre.destroy)
    bfin.pack()
    cadre.pack()
    
def Enregistrer_Suit():
    global Suit
    chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")
    e = open("relation",'wb')
    dump(Suit,e)
    os.chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")
def Restaurer_Suit():
    global Suit
    chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")
    e = open("relation",'rb')
    Suit = load(e)
    os.chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers") 

#------------------------Etudiant--------------------
def CadreSaisie():
    def ajout():    
        global etu 
        nom=SaisieNom.get()
        prenom=SaisiePrenom.get()
        naissance=SaisieNaissance.get()
               
        ok = True
        for e in etu:
            if etu[e]["nom"]==nom and etu[e]["prenom"]==prenom:
                ok = False
                break
            
        if ok:
            id=len(etu) + 1
            etu[id]={"nom":nom, "prenom":prenom, "naissance": naissance}    
           
            
        SaisieNom.delete(0,END) 
        SaisiePrenom.delete(0,END)
        SaisieNaissance.delete(0,END)

    cadre=Frame(fen) 
    message=Label(cadre, text="Nom") 
    message.pack()
    SaisieNom=Entry(cadre) 
    SaisieNom.pack()
    message_prenom=Label(cadre, text="Prénom") 
    message_prenom.pack()
    SaisiePrenom=Entry(cadre)
    SaisiePrenom.pack()
    message_annee=Label(cadre, text="Année de naissance") 
    message_annee.pack()
    SaisieNaissance=Entry(cadre)
    SaisieNaissance.pack()
    
    bval=Button(cadre, text="Valider", command=ajout) 
    bval.pack()
    bfin=Button(cadre, text="OK", command=cadre.destroy) 
    bfin.pack()
    cadre.pack()


def visu_etu():
   
    global etu # dictionnaire des noms
    cadre=Frame(fen)
# Pour avoir une liste avec ascenseur - Utilisation du widget Scrollbar
    ascenseur=Scrollbar(cadre) 
# positionnement d'un déroulement vertical, barre de défilement à droite
    ascenseur.pack(side='right', fill=Y) 
    message=Label(cadre, text="profil de l'etudiant ")
    message.pack()
# définition de la zone d'affichage de la liste, et liaison avec l'ascenseur
    lesNoms=Listbox(cadre, yscrollcommand=ascenseur.set) 

    for e in etu:
        seq=str(e)
        seq+=" "+etu[e]["nom"]+" " +etu[e]["prenom"]+" "+etu[e]['naissance']
        lesNoms.insert(END, seq)
    lesNoms.pack(side='left')
    ascenseur.config(command=lesNoms.yview) # configuration de l'ascenseur
    bfin=Button(cadre, text="OK",command= cadre.destroy)
    bfin.pack()
    cadre.pack()
    
def Enregistrer_Etu():
    global etu
    chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")
    e = open("profil_etudiant",'wb')
    dump(etu,e)
    os.chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")
def Restaurer_Etu():
    global etu
    chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")
    e = open("profil_etudiant",'rb')
    etu = load(e)
    os.chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")    

#---------------------------UE-----------------------
def CadreSaisieUE ():
    def ajout():
   
        global UE
        intitule=SaisieNomue.get()
        volume_hor=SaisieVol.get()
        nom_enseignant=SaisieEns.get()
               
        ok = True
        for e in UE:
            if UE[e]["intitule"]==intitule:
                ok = False
                break
            
        if ok:
            code=len(UE) + 1
            UE[code]={"intitule":intitule, "volume_hor":volume_hor, "nom_enseignant": nom_enseignant, "nombre":0}
        SaisieNomue.delete(0,END) 
        SaisieVol.delete(0,END)
        SaisieEns.delete(0,END)
        
    cadreUe=Frame(fen) 
    message=Label(cadreUe, text="Nom de l'UE") 
    message.pack()
    SaisieNomue=Entry(cadreUe) 
    SaisieNomue.pack()
    vol=Label(cadreUe, text="Volume horaire de cette UE") 
    vol.pack()
    SaisieVol=Entry(cadreUe)
    SaisieVol.pack()
    Nom_ens=Label(cadreUe, text="Nom de l'enseignant") 
    Nom_ens.pack()
    SaisieEns=Entry(cadreUe)
    SaisieEns.pack()
    bval=Button(cadreUe, text="Valider", command=ajout) # bouton de validation de la saisie qui lance l'enregistrement du nom dans la liste
    bval.pack()
    bfin=Button(cadreUe, text="OK", command=cadreUe.destroy) 
    bfin.pack()
    cadreUe.pack()
    
def visu_UE():
    #Visualisation des noms de la liste
    global UE # la liste des noms
    cadre=Frame(fen)
# Pour avoir une liste avec ascenseur - Utilisation du widget Scrollbar
    ascenseur=Scrollbar(cadre) 
# positionnement d'un déroulement vertical, barre de défilement à droite
    ascenseur.pack(side='right', fill=Y) 
    message=Label(cadre, text="Nom de l'UE, volume horaire, nom de l'enseignant et id ")
    message.pack()
# définition de la zone d'affichage de la liste, et liaison avec l'ascenseur
    lesNoms=Listbox(cadre, yscrollcommand=ascenseur.set) 

    for u in UE:
        seq=str(u)
        seq+=" "+UE[u]["intitule"]+" " +UE[u]["volume_hor"]+" "+UE[u]['nom_enseignant']
        lesNoms.insert(END, seq)
    lesNoms.pack(side='left')
    ascenseur.config(command=lesNoms.yview) # configuration de l'ascenseur
    bfin=Button(cadre, text="OK",command= cadre.destroy)
    bfin.pack()
    cadre.pack()
    
def Enregistrer_UE ():
    global UE
    chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")
    e = open("fiche_UE",'wb')
    dump(UE,e)
    os.chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")


def Restaurer_UE():
    global UE
    chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")
    e = open("fiche_UE",'rb')
    UE = load(e)
    os.chdir("D:\Programme\python\Scripts\Mes_Prog_Python\les_fichiers")


etu={}
UE={}
Suit={}  

fen=Tk()
monMenu=Menu(fen)
menuEtu=Menu(monMenu)
menuEtu.add_command(label="Ajout", command=CadreSaisie)

menuEtu.add_command(label="Visualisation", command=visu_etu)
menuEtu.add_command(label="Enregistrer",command=Enregistrer_Etu)
menuEtu.add_command(label="Restauration", command=Restaurer_Etu)

menuUE = Menu(monMenu)
menuUE.add_command(label="Ajout", command=CadreSaisieUE)
menuUE.add_command(label="Visualisation", command=visu_UE)
menuUE.add_command(label= "Enregistrer", command=Enregistrer_UE)
menuUE.add_command(label="Restaurer", command=Restaurer_UE)

menuSuit = Menu(monMenu)
menuSuit.add_command(label="Ajout", command=CadreSaisieSuit)
menuSuit.add_command(label="Visualisation", command=visu_Suit)
menuSuit.add_command(label="Enregistrer", command=Enregistrer_Suit)
menuSuit.add_command(label="Restaurer", command=Restaurer_Suit)

menuAnalyse = Menu(monMenu)
menuAnalyse.add_command(label="Liste des enseignants", command=Analyse_enseignant)
menuAnalyse.add_command(label="Liste des etudiants", command=Analyse_etudiant)
menuAnalyse.add_command(label="UE suivi par l'etudiant", command=Analyse_intitule)
menuAnalyse.add_command(label="UE en vogue", command=Analyse_vogue)
menuAnalyse.add_command(label="Enregistrer", command=Enregistrer_Suit)
menuAnalyse.add_command(label="Restaurer", command=Restaurer_Suit)
menuAppli=Menu(monMenu)
menuAppli.add_command(label="Quitter", command=fen.destroy)

monMenu.add_cascade(label="Étudiants", menu=menuEtu)
monMenu.add_cascade(label="UE", menu=menuUE)
monMenu.add_cascade(label="Inscription", menu=menuSuit)
monMenu.add_cascade(label="Analyse", menu=menuAnalyse)
monMenu.add_cascade(label="Gestion", menu=menuAppli)

fen.config(menu=monMenu)
fen.mainloop()
