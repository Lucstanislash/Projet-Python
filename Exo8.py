from Outils import *

def SaisieEx8():
    min10=1
    max10=500
    a=False
    while a==False:
        TailleTab=int(input("Taille du tableau: "))
        TailleCase=int(input("Taille des cases: "))
        Ad1mot=int(input("Adresse du premier mot: "))
        if TailleTab*TailleCase<950:
            a=CtrlSyntaxe(str(TailleTab),10,1,10,30,300)
    return(TailleTab,TailleCase,Ad1mot)

def RepEx8(donne):
    nbmot=donne[0]*donne[1]
    numdermot=(nbmot+donne[2])-1
    numpremot=donne[2]
    return([str(nbmot),str(numpremot),str(numdermot)])

def Exo8():
    util=[]
    verif=2
    verif2=2
    man=str(input("Saisie manuel ou aléatoire?"))
    if man == 'manuel':
        donne=SaisieEx8()
    else:
        TailleTab=AleaExAll(10,30,300)
        TailleCase=AleaExAll(10,1,30)
        Ad1mot=AleaExAll(10,1,1000)
        donne=(TailleTab,TailleCase,Ad1mot)
    rep=RepEx8(donne)
    while verif!=1:
        util.append(str(input("Saisir taille du tableau en mot")))
        util.append(str(input("Saisir adresse du premier mot")))
        util.append(str(input("Saisir Adresse du dernier mot")))
        verif=VerifRep(rep,util)
        if verif==0:
            print("réessaye")
        elif verif==-1:
            print("perdu, ","Voici la réponse: ",rep)
            break
    else:
        print("Gagné")
        
    donne2=AleaExAll(10,1,donne[0])
    print('Donner le contenu de la case',donne2)
    rep2=donne[2]+(donne2-1)*donne[1]
    while verif2!=1:
        util=str(input("Saisir la réponse: "))
        verif2=VerifRep(str(rep2),util)
        if verif2==0:
            print("réessaye")
        elif verif2==-1:
            print("perdu, ","Voici la réponse: ",rep2)
            break
    else:
        print("Gagné")
    
    
    
    





    

