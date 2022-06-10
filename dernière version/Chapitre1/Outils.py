#================== Version 1.0 =================================


from random import *
def CtrlSyntaxe(ch,syn,min,max,min10=0,max10=0):
    comptep=0
    "controle la syntaxe de ch en fonction de syn (ch peux être un nombre en base 2, 8, 10, 16, piussance syn prendra respectivement les valeurs2, 8 ,10, 16, puissance pour indiquer la syntaxe que ch doit avoir."
    mot2='01.'
    mot8='01234567'
    mot10='-.0123456789'
    mot16='0123456789ABCDEF'
    dico={}
    dico[2]=mot2
    dico[8]=mot8
    dico[10]=mot10
    dico[16]=mot16
    ok=True
    if min<=len(ch)<=max:
        mot=dico[syn]
        for i in ch:
            if not i in mot:
                ok=False
                break
        if ok and syn==10:            
            for f in range(len(ch)):
                if ch[f]=='-' and f>=1:
                    ok=False
                if ch[0]=='-':
                    if ch[f]=='.':
                        comptep+=1
                        if f<2:
                            ok=False
                else:
                    if ch[f]=='.':
                        comptep+=1
                        if f<1:
                            ok=False
            if comptep>1:
                ok=False
            if ok==True:
                if not int(float(ch)) in range(min10,max10+1):
                    ok=False
    else:
        ok=False
    return(ok)

def AleaExAll(syn,min,max):
    "crer une chaine aléatoire en base 2, 8, 10 ou 16 en fonction de la valeur de syn et permet d'en gérer la taille"
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
        ch=randint(min,max)
    elif syn == 16:
        for i in range(alea):
            a=randint(0,15)
            ch=ch+mot16[a]
    elif syn == 'puissance': #il affiche directement la valeur de la puissance sous formed'un chiffre
        ch=2**alea
    elif syn == 'puissanceExp': # il affiche la puissance sous forme de 2**(chiffre)
        ch=alea
        #####alea=AleaExAll('puissanceExp',1, 20)
        #####ch='2**'+str(alea)
    return(ch)
a=0
cpt=0
def VerifRep(rep,util):
    a=0
    global cpt
    "Compare la réponse à l’exercice (rep) avec la réponse de l’utilisateur (util)"
    if rep == util:
        a=1 #bloquer le bouton valider ==> Gagner
        cpt = 0
    else:
        cpt = cpt + 1
        if cpt>2:
            a=-1 #bloquer le bouton valider ==> Perdu
            cpt=0
        else:
            a=0 #reesayer ==> nouvelle chance
    return(a)

def Conv(basedep,basearr,entier):
    "Convertie de la base basedep à la base basearr un entier coder en basedep"
    dico={}
    dico[2]='b'
    dico[8]='o'
    dico[16]='x'
    if basedep == 10:
        rep=format(int(entier),dico[basearr])
    elif basearr == 10:
        rep=int(str(entier),basedep)
    else:
        rep=int(str(entier),basedep)
        rep=format(rep,dico[basearr])
    return(rep)

def Raccourcir(ch):
    "Enleve les espaces d'une chaine ch"
    ch=ch.replace(" ","")
    return(ch)

