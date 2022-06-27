from random import*
import math
from Outils import*

type1=['FIFO','PCTER','Tourniquet','Prio']
type1='Prio' 

def Nbproc () :
    n=randrange(4,14)
    print("Nombre de processus : ",n)
    mini=0
    maxi=0
    cpt=0
    listarv=[]
    listdur=[]
    listprio=[]
    listp=[]
    alea={}
    LP=[]
    q=randrange(1,5)
    for i in range (n):
        duree=randrange(1,10)
        cpt=cpt+1
        listdur.append(duree)
        listp.append(i+1)
        arv=randint(mini,maxi)
        listarv.append(arv)
        mini=arv
        prio=randrange(1,5)
        listprio.append(prio)
        maxi=maxi+duree
        
       
    for i in range(len(listp)):
        if type1=='Prio': #Prioeité fixe
            LP.append({"n°":listp[i],"Arv":listarv[i],"duree":listdur[i],'prio':listprio[i]})
        else :
            LP.append({"n°":listp[i],"Arv":listarv[i],"duree":listdur[i]})
    
    print("Processus : ",listp)
    print("DateA : ",listarv)
    print("Duree : ",listdur)
    print(LP)

    return(LP)

    



    
Nbproc ()


