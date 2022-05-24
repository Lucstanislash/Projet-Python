from random import *
from Outils import *


def AleaEx3(min,max):
    
    #Donne des nombres binaires aléatoires
    #J'utilise cette aléatoire parce que j'ai besoin d'avoir des nombres binaires
    #qui commencent par 1, sinon une partie du code ne marchera pas
    
    mot2='01'
    
    ch = '1'
    
    alea = randint(min,max)
    
    for i in range(alea):
        
            a=randint(0,1)
            
            ch+=str(a)

    return(ch)



#*Erreurs de proba 
#def TestTest(n):  
#    a = AleaEx3(1,32)
#        if a [-n:] == '0'*n :       
#        return(a)   
#    else :
#        return(TestTest(n))



puissance = AleaExAll('puissanceExp',1,20)
#================== Liste des valeurs binaires aléatoires ===============#
#liste qui contient les bonnes réponses
l = []

def List(liste, n):
    
    #Crée une liste avec des nombres binaires aléatoires 

    for i in range(7): #génère des nombres binaires aléatoires 
        
        liste.append(AleaEx3(1,32))

    for i in range(3):#pour avoir au moins 3 réponses correctes

        a = TestTest(n)
       
        liste.append(a)
        
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
   
