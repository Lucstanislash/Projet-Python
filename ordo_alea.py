from random import*
import math
from Outils import*

type=2

def Nbproc () :
    n=randrange(4,14)
    print("Nombre de processus : ",n)
    mini=0
    maxi=0
    cpt=0
    listarv=[]
    listdur=[]
    listp=[]
    alea={}
    LP=[]
    for i in range (n):
        duree=randrange(1,10)
        cpt=cpt+1
        listdur.append(duree)
        listp.append(i+1)
        arv=randint(mini,maxi)
        listarv.append(arv)
        mini=arv
        maxi=maxi+duree
        
       
    for i in range(len(listp)):
        LP.append({"n°":listp[i],"Arv":listarv[i],"duree":listdur[i]})
         

    print("Processus : ",listp)
    print("DateA : ",listarv)
    print("Duree : ",listdur)
    print(LP)
    

    
    Somme=0
    
##    for i in range(len(listarv)):
##        Somme+=listdur[i] #calcul somme des duree
##        if listarv[i]>Somme: #comparaison somme duree et date arrivee
##            Nbproc()

    print(alea)
        


    
Nbproc ()


