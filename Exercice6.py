from random import *
from Outils import *

###=================================== Saisies ===========================================#
##def SaisieOrdreChaine():
##    basedep = input("Saisissez la base de départ => ")
##    if basedep == '10' :
##        NbDec = input("Saisissez le nombre que vous voulez convertir en base 2 => ")
##        if CtrlSyntaxe(NbDec, 10, 1,10000) == True:
##            return(NbDec)
##        else :
##            print("/!\ Erreur : Ce n'est pas la bonne synthaxe.")
##    elif basedep == '2' :
##        NbBin = input("Saisissez le nombre que vous voulez convertir en base 10 => ")
##        if CtrlSyntaxe(NbBin, 2, 1, 32) == True:
##            return(NbBin)
##        else :
##            print("/!\ Erreur : Ce n'est pas la bonne synthaxe.")

def ApresVirgule():
    NbBinVirgule = int(input("Saisissez combien de bits après la virgule => "))
    if NbBinVirgule<= 5 :
        return(NbBinVirgule)
    else :
        print("/!\ Erreur : 5 est le max de bits après la virgule. ")
    
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

#==============================================================================================  

##def AleaOrdreEx6():
##    lischoix = [ '10','2']
##    choix = choice(lischoix)
##    if choix == '10' :
##        Dec = 
##        RepEx6Alea.append(a)
##        return(a)
##    else :
##        b = 
##        RepEx6Alea.append(b)
##        return(b)

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
    

#=============================================================================
lischoix = [ '10','2']

def  AleaEx6_Ordre(lischoix):
        #aléatoire de l'ordre
        choix = choice(lischoix)
        return(choix)

def AleaEx6():
    ordre=AleaEx6_Ordre(lischoix)
    if ordre=='10':
            valeur=NumVirgule(10)
    else:     
            valeur=NumVirgule(2)
            
    return(valeur,ordre)


def SaisieEx6():
    ok = False
    while ok == False:
        Ordre = str(input("Saisissez le format de conversion ( '10' ou '2' ) => "))
        if Ordre == '10':
            nb=str(input("Saisissez le nombre que vous voulez convertir en base 10 => "))
##            ok = CtrlSyntaxe(nb,2,1,10000)
        elif Ordre == '2':
            nb = str(input("Saisissez le nombre que vous voulez convertir en base 2 => "))
##            ok = CtrlSyntaxe(nb,10,1,32) 
        else:
            ok=False
    return(nb,Ordre)

##def PrincipalEx6():
##
##    man=input("manuel ou aléatoire \n")
##   
##    if man=="manuel":
##        saisie=SaisieEx6()
##
##        
##    elif man=="aleatoire":
##        saisie=AleaEx6()   
##    else:
##        print("erreur de syntaxe")
##        
##    Ordre=saisie[1]
##    Val=saisie[0]    
##    print("Formats de conversion :",Ordre)
##    print("voici la valeur à convertir :",Val)
##    
##    if Ordre == '10' :       
##        rep = bin_dec(Val)
##        print("voici la réponse ",rep)
##        
##    else:
##        rep=dec_bin(Val)
##        print("voici la réponse ",rep)
##        
##    util=input("Saisir la réponse")
##    verif=VerifRep(rep,util)
##    
##    return(verif)


