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


#=========================== Puissance de 2 ===========================#

power = AleaExAll('puissance', 1, 32)


#================== Liste des valeurs binaires aléatoires ===============#

#liste qui contient les bonnes réponses
l = []

def List(l):
    
    #Crée une liste avec des nombres binaires aléatoires 

    for i in range(7): #génère des nombres binaires aléatoires 
        
        l.append(AleaEx3(1,32))

    for i in range(3): #pour avoir au moins 3 réponses correctes

        correct = (int(AleaEx3(1,15),2) * power)

        a = bin(correct)[2:]

        correp = a.zfill(8) 

        l.append(str(correp))

    shuffle(l) #permet de bien mélanger les suggestions


#====================== Liste des Réponses correctes ====================#

#Liste des réponses correctes
Rep = []

def RepEx3(l,Rep):
    
    #Donne les bonnes réponses

    for i in l:

        if int(i,2)% power == 0: 

            Rep.append(i)



#====================== Liste des Réponses correctes ====================#
            
#Liste des réponses de l'utilisateur        
Util = []         

def RepUtil(l,Util):

    #Retient les réponses de l'utilisateur

    repUtil = input('>>> ').lower()

    if repUtil in l:

        print('Votre réponse est : ', repUtil,'.')#Pour tester

        Util.append(repUtil)
        

#====================== Vérification des réponses ========================#


   


            
        
