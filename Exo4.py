from random import*
import math
from Outils import*
#-------------------ALEATOIRE#----------------------------#

def Alea4 ():
    a=AleaExAll(2,1,16)
    alea=randint(1,8)
    ch=""
    ch1='0'
    print("Votre nombre en base de 10 => ", a)
    print("Votre puissance de 2 => ", alea)
    c=False
    while c==False:
        if (len(a)<alea):
            c=False
        nb=randint(0,1)
        if (nb==1):
            oper="*"    
        else:
            oper="/"
        print("Vous devez =>",oper)
        return (a,alea,oper)
    return (a,alea,oper)
    
##################################
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

def Sais_Ex4():
    c=False
    while c==False:
        ch1=input("saisir votre nombre en base de 2 =>")
        ch2=input("Saisir votre puissance de 2 => ")
        #depend de l'interface
        if (len(ch1)<int(ch2)):
            c=False
        else:
            c=CtrlSyntaxe(ch1,2,1,16)
            c=CtrlSyntaxe(ch1,2,1,16)
        oper=input(" Saisir '*' si vous voulez mulitiplier '/' si vous voulez divisez")        
        oper1=['*','/']
        if oper not in oper1:
            c=False
    return(ch1,ch2,oper)
           
def repEx4(a,alea,oper):
    ch=''
    ch1='0'
    while (len(a))>=int(alea):
        if oper=='*':
            ch+=(a+(ch1*int(alea)))
        elif oper=='/':
            ch+=(a[:-int(alea)])
        else:
            break
        return (ch)
                  
def Exo4 ():
    verif=2
    base=[2,10]
    man=str(input("Saisie manuel ou aléatoire => "))
    if man=='manuel':
        a=Sais_Ex4 ()
    else:
        a=Alea4()
    rep=repEx4(a[0],a[1],a[2])
    while verif!=1:
        util=input("Sisir la reponse du calcul : ")
        verif=VerifRep(rep,util)
        if verif==0:
            print("Reesseyer")
        elif verif==-1:
            print("Voici la reponse => ", rep)
            break
        else:
            print("gagné")
    
