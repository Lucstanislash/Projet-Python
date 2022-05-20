from random import *
from Outils import *

l = []
def List(l):
    #Crée une liste avec des nombres binaires aléatoires
    for i in range(10):
        l.append(AleaExAll(2, 1, 32))

Rep = []
def RepEx3(l):
    #Donne les bonnes réponses#======>>> *** à corriger
    for i in l:
        if int(i) % 2 == 0:
            print(i)
            Rep.append(i)
  
#Juste pour le tester mais le code va probablement être différent vu qu'on va faire un *qcm*#
Util = []            
def RepUtil(l,Util):
    #Retient les réponses de l'utilisateur 
    # # # # loop pour faire le plus d'inputs # # # #
    repUtil = input('>>> ').lower()
    if repUtil in l:
        print('Votre réponse est : ', repUtil,'.')#Pour tester
        Util.append(repUtil)
            
#Manipuler les listes pour les avoir sous forme de quizz / vérification des réponses

#Quizz : le reste à voir //code interface



        
            


                
            
        
        
            


            
        
