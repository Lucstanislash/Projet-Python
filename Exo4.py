
from random import*
import math
import Outils
#########################################################

def Alea4 ():
    a=AleaExAll(2,1,16)
    alea=randint(1,8)
    ch=""
    ch1='0'
    print("Votre nombre en base de 10 => ", a)
    print("Votre puissance de 2 => ", alea)
    while (len(a)>=alea):
        nb=randint(0,1)
        if (nb==1):
                oper="*"    
        else:
                oper="/"
        print("Vous devez =>",oper)
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
    ch1=input("saisir votre nombre en base de 2 =>")
    CtrlSyntaxe(ch1,2,1,16)
    ch2=input("Saisir votre puissance de 2 => ")
    CtrlSyntaxe(ch2,10,1,8)
    #depend de l'interface
    oper=input(" Saisir '*' si vous voulez mulitiplier '/' si vous voulez divisez")
    return(ch1,ch2,oper)
            
def repEx4(a,alea,oper):
    ch=''
    ch1='0'
    while (len(a))>=int(alea):
        if oper=='*':
            ch+=(a+(str(ch1)*alea))
        elif oper=='/':
            ch+=(a[:-alea])
        else:
            break
        return (ch)
                  
def Exo4 ():
    verif=2
    base=[2,10]
    man=str(input("Saisie manuel ou aléatoire"))
    if man=='manuel':
        a=Sais_Ex4 ()
    else:
        a=Alea4()
    rep=repEx4(a[0],a[1],a[2])
    while verif!=1:
        util=input("Sisir la reponse du calcul :")
        verif=VerifRep(rep,util)
        if verif==0:
            print("Reesseyer")
        elif verif==-1:
            print("Voici la reponse", rep)
            break
        else:
            print("gagné")
    

