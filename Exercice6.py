from random import *

#Utilisateur choisit l’ordre de conversion
def SaisieOrdreChaine():
    basedep = input("Saisissez la base de départ => ")
    if basedep == '10' :
        ch1 = input("Saisissez le nombre que vous voulez convertir en base 2 => ")
        CtrlSyntaxe(ch1, 10, 0, 10000)
        ch3 = input("Saisissez combien de bit après la virgule => ")
    elif basedep == '2' :
        ch2 = input("Saisissez le nombre que vous voulez convertir en base 10 => ")
        CtrlSyntaxe(ch2, 2, 1, 32)
    else :
        print('/!\ Erreur : Impossible de convertir sous \nun autre format que 10 ou 2 ')

        
def AleaOrdre():
    l = [ 'choix1','choix2']
    c = choice(l)
    if c == 'choix1' :
        basedep = 10
        basearriv = 2
        return(basedep, basearriv)
    else :
        basedep = 2
        basearriv = 10
        return(basedep, basearriv)

