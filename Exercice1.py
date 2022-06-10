from Outils import *
    
def SaisiEx1():
    a=False
    while a==False:
        basedep=int(input("Base de départ"))
        basearr=int(input("Base d'arrivé"))
        entier=str(input("entier à convertir:"))
        if basedep!=basearr:
            if basedep==8:
                a=CtrlSyntaxe(entier,8,1,10)
            elif basedep==16:
                a=CtrlSyntaxe(entier,16,1,8)
            elif basedep==2:
                a=CtrlSyntaxe(entier,2,1,32)
            elif basedep==10:
                a=CtrlSyntaxe(entier,10,1,10,1,10000)
    return(basedep,basearr,entier)


def RepEx1(donne):
    dico={}
    dico[2]='b'
    dico[8]='o'
    dico[16]='x'
    if donne[0] == 10:
        print(dico[donne[1]])
        rep=format(int(donne[2]),dico[donne[1]])
    elif donne[1] == 10:
        rep=int(donne[2],donne[0])
    else:
        rep=int(donne[2],donne[0])
        rep=format(rep,dico[donne[1]])
    return(rep)
            
def Exo1():
    verif=2
    base=[2,8,10,16]
    man=str(input("Saisie manuel ou aléatoire?"))
    if man == 'manuel':
        donnee=SaisiEx1()
    else:
        a=randint(0,3)
        b=randint(0,3)
        while a==b:
            a=randint(0,3)
            b=randint(0,3)

        basedep=base[a]
        basearr=base[b]
        if basedep==2:
            entier=AleaExAll(2,1,32)
        if basedep==8:
            entier=AleaExAll(8,1,10)
        if basedep==10:
            entier=AleaExAll(10,1,5)
        if basedep==16:
            entier=AleaExAll(16,1,8)
        print("basedep: ", basedep,"basearr: ", basearr,"entier: ",entier)
        donnee=[basedep,basearr,entier]
    rep=RepEx1(donnee)
    while verif!=1:
        print(cpt)
        util=str(input("Saisir la réponse: "))
        verif=VerifRep(str(rep),util)
        if verif==0:
            print("réessaye")
        elif verif==-1:
            print("perdu, ","Voici la réponse: ",rep)
            break
    else:
        print("Gagné")
   
        
    
    
