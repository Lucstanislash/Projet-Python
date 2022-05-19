from random import *
def CtrlSyntaxe(ch,syn,min,max,min10=0,max10=0):
    ##controle la syntaxe de ch en fonction de syn (ch peux être un nombre en base 2, 8, 10, 16, piussance syn prendra respectivement les valeurs2, 8 ,10, 16, puissance pour indiquer la syntaxe que ch doit avoir.
    mot2='01'
    mot8='01234567'
    mot10='0123456789'
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
            if not int(ch) in range(min10,max10+1):
                ok=False
    else:
        ok=False
    return(ok)

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
        ch=randint(min,max)
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

def Conv(basedep,basearr,entier):
    dico={}
    dico[2]='b'
    dico[8]='o'
    dico[16]='x'
    if basedep == 10:
        rep=format(int(entier),dico[basearr])
    elif basearr == 10:
        rep=int(entier,basedep)
    else:
        rep=int(entier,basedep)
        rep=format(rep,dico[basearr])
    return(rep)
        
