from random import*
import math
from Outils import*

type=2

def Nbproc () :
    n=randrange(4,14)
    print("Nombre de processus : ",n)
    cpt=0
    listarv=[]
    listdur=[]
    listp=[]
    alea=[]
    for i in range (n):
        cpt=(cpt+1)
        duree=randrange(1,10)
        listdur.append(duree)
        listp.append(cpt)
        arv=randrange(1,20)
        listarv.append(arv)
        listarv.sort()

    print("Processus : ",listp)
    print("DateA : ",listarv)
    print("Quantum : ",listq)
    print("Duree : ",listdur)
    print(duree)
    Somme=0
    
    for i in range(len(listarv)):
        Somme+=listdur[i] #calcul somme des duree
        if listarv[i]>Somme: #comparaison somme duree et date arrivee
            Nbproc()

    alea.append(listdur)
    alea.append(listarv)
    alea.append(listp)
    print(alea)
        


    
Nbproc ()


