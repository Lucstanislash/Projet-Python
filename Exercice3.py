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


exposant = AleaExAll('puissanceExp',1,16)

print("l'exposant est",exposant)

    
#liste qui contient les bonnes réponses
l = []

def List(liste, n):
    #Crée une liste avec des nombres binaires aléatoires 
    for i in range(7): #génère des nombres binaires aléatoires 
        liste.append(AleaEx3('quelconque',n,1,30))
    for i in range(3):#pour avoir au moins 3 réponses correctes
        liste.append(AleaEx3('correct',n,1,30))
    shuffle(liste) #permet de bien mélanger les suggestions

#====================== Liste des Réponses correctes ====================#

#Liste des réponses correctes
RepEx3 = []

def ReponseEx3(l,RepEx3,n):
    #Donne les bonnes réponses
    for i in l:
        if int(i,2)% (2**n) == 0: 
            RepEx3.append(i)

#====================== Liste des Réponses correctes ====================#
            
#Liste des réponses de l'utilisateur
UtilEx3 = []

#Pour tester
def RepUtil(l,UtilEx3):

    #Retient les réponses de l'utilisateur
    repUtil = input('>>> ').lower()
    if repUtil in l:
        print('Votre réponse est : ', repUtil,'.')#Pour tester voir laquelle des valeurs j'ai ajouté
        UtilEx3.append(repUtil)
        

#====================== Vérification des réponses ========================#

VerifRep(RepEx3, UtilEx3)

#ça marche
   
   
