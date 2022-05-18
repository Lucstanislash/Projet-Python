from random import *
from Outils import *

#============================= Saisie / Menu déroulant ================================#
#Utilisateur choisit l’ordre de conversion // code d'interaction avec l'interface à voir ... 
#après que l'interface exo 6 soit complète // un scroll pour les choix de base dep/arriv 
#au lieu de les saisir manuellement sera mieux 
#def SaisieOrdreChaine():
#    basedep = input("Saisissez la base de départ => ")
#    if basedep == '10' :
#        ch1 = input("Saisissez le nombre que vous voulez convertir en base 2 => ")
#        CtrlSyntaxe(ch1, 10, 1, 5)#####################ne doit pas dépasser 10000 à voir*
#        ch3 = input("Saisissez combien de bit après la virgule => ")
#    elif basedep == '2' :
#        ch2 = input("Saisissez le nombre que vous voulez convertir en base 10 => ")
#        CtrlSyntaxe(ch2, 2, 1, 32)


############## Cahier de charge ... confusing à reconsulter... demain #################         
#==================================== L'aléatoire ====================================#
def testEx6(): #pour la taille max du nombre aléatoire en base 10 (base 10 => base 2)
	a = AleaExAll(10, 1, 5)
	if int(a) <= 10000:
		print(a)
	else :
		return(testEx6())

## Fusionner deux listes vec des randomizers
## => Ce qui Permet de créer un nombre binaire décimal (base 2 => base 10)
def NumDecimal():
    l=[]
    b = AleaExAll(2, 1, 27) 
	#32 - 5 = 27 max (Nombre avant la virgule car si je mets 32 ... j'aurai plus de 32 bits en faisant le join)
    l.append(b)
    a = AleaExAll(2, 1, 5)
    if '1' in a :
        l.append(a)
    else:
        NumDecimal()
    ch = ','.join(l) #ajoute une virgule 
    print(ch)

    
def AleaOrdreEx6():
    l = [ 'choix1','choix2']
    c = choice(l)
    if c == 'choix1' :
        basedep = 10
        basearriv = 2
        print(basedep, basearriv)
        testEx6()
    else :
        basedep = 2
        basearriv = 10
        print(basedep, basearriv)
        NumDecimal()
