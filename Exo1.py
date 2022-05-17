from random import *
def CtrlSyntaxe(ch,syn,min,max):
    ##controle la syntaxe de ch en fonction de syn (ch peux être un nombre en base 2, 8, 10, 16, piussance syn prendra respectivement les valeurs2, 8 ,10, 16, puissance pour indiquer la syntaxe que ch doit avoir.
    mot2='01'
    mot8='01234567'
    mot10='0123456789'
    mot16='0123456789ABCDEF'
    a=False
    if len(ch)>min and len(ch)<max:
        a=True
        if syn == 2:
            for i in ch:
                if i in mot2:
                    a=True
                else:
                    a=False
                    break
        elif syn == 8:
            for i in ch:
                if i in mot8:
                    a=True
                else:
                    a=False
                    break
        elif syn == 10:
            for i in ch:
                if i in mot10:
                    a=True
                else:
                    a=False
                    break
        elif syn == 16:
            for i in ch:
                if i in mot16:
                    a=True
                else:
                    a=False
                    break
    return(a)

def AleaExAll(syn,min,max):
    mot16='0123456789ABCDEF'
    ch=""
    alea=randint(min,max)
    if syn == 2:
        for i in range(alea):
            a=randint(0,1)
            ch+=str(a)
    elif syn == 8:
        for i in range(alea):
            a=randint(0,7)
            ch+=str(a)
    elif syn == 10:
        for i in range(alea):
            a=randint(0,9)
            ch+=str(a)
    elif syn == 16:
        for i in range(alea):
            a=randint(0,15)
            ch=ch+mot16[a]
    elif syn == 'puissance':
        ch=2**alea
    return(ch)

a=0
cpt = 0
def VerifRep(rep,util):
    #Compare la réponse à l’exercice (rep) avec la réponse de l’utilisateur (util)
    if rep == util:
        a=1 #bloquer le bouton valider
    else:
        global cpt
        cpt = cpt + 1
        if cpt>2:
            a=-1 #bloquer le bouton valider
        else:
            a=0 #reesayer
    return(a)
    

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
    return(basedep,basearr,entier)


def RepEx1(a):

    if a[0] == 2:
        if a[1] == 8:
            b=int(a[2],2)
            b=format(b,'o')
        elif a[1] == 10:
            b=int(a[2],2)
        elif a[1] == 16:
            b=int(a[2],2)
            b=format(b,'x')
    elif a[0] == 8:
        if a[1] == 2:
            b=int(a[2],8)
            b=format(b,'b')
        elif a[1] == 10:
            b=int(a[2],8)
        elif a[1] == 16:
            b=int(a[2],8)
            b=format(b,'x')
    elif a[0] == 10:
        if a[1] == 2:
            b=format(a[2],'b')
        elif a[1] == 8:
            b=format(a[2],'o')
        elif a[1] == 16:
            b=format(a[2],'x')
    elif a[0] == 16:
        if a[1] == 2:
            b=int(a[2],16)
            b=format(b,'b')
        elif a[1] == 8:
            b=int(a[2],16)
            b=format(b,'o')
        elif a[1] == 10:
            b=int(a[2],16)
    return(b)
            
def Exo1():
    verif=2
    base=[2,8,10,16]
    man=str(input("Saisie manuel ou aléatoire?"))
    if man == 'manuel':
        a=SaisiEx1()
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
        a=[basedep,basearr,entier]
    rep=RepEx1(a)
    while verif!=1:
        util=str(input("Saisir la réponse: "))
        verif=VerifRep(str(rep),util)
        if verif==0:
            print("réessaye")
        elif verif==-1:
            print("perdu, ","Voici la réponse: ",rep)
            break
    else:
        print("Gagné")

        
            
        
    
    
