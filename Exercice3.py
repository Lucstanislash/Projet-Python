from random import *
from Outils import *


def AleaEx3(choix,n,mini,maxi):
    
    #Donne des nombres binaires aléatoires
    ch = '1'        
    if choix == 'quelconque':
        taille = randint(mini,maxi)
        for i in range(taille):
            a=randint(0,1)
            ch+=str(a)
    elif choix == 'correct':
        taille = randint(min(mini, n+1), maxi)
        for i in range(taille-n):
            a=randint(0,1)
            ch+=str(a)
        ch+='0'*n # += erreur 
    return(ch)

#Liste des réponses affichées
def List(liste, n):
    #Crée une liste avec des nombres binaires aléatoires 
    for i in range(7): #génère des nombres binaires aléatoires 
        liste.append(AleaEx3('quelconque',n,1,30))
    for i in range(3):#pour avoir au moins 3 réponses correctes
        liste.append(AleaEx3('correct',n,1,30))
    shuffle(liste) #permet de bien mélanger les suggestions

#====================== Liste des Réponses correctes ====================#

#Retient les réponses correctes
def ReponseEx3(l,RepEx3,n):
    #Donne les bonnes réponses
    for i in l:
        if int(i,2)% (2**n) == 0: 
            RepEx3.append(i)


   
   
