from random import *

def SaisieOrdreChaine():
    a = input("Saisissez l'ordre de conversion")
    if a == '10' :
        ch1 = input("Saisissez le nombre que vous voulez convertir en base 2 => ")
        CtrlSyntaxe(ch1, 10, 0, 10000)
    elif a == '2' :
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

