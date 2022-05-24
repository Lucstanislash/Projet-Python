from random import*
import math
from Outils import*
#-------------------ALEATOIRE#----------------------------#

def Alea4 ():
    nb=randint(0,1)     #choix de l'opération
    if (nb==1):
        oper="*"    
    else:
        oper="/"
    print("L'operation effectuer ==>",oper)
    p=randint(1,8) #choix de la puissance
    print(p)
    taille =randrange(1,17-p)
    ch='1'
    if oper=='/':
        for i in range (taille-1):
            c=randrange(0,2)
            if c==1:
                ch+='1'
            else:
                ch+='0'
        ch+='0'*p
    else:
        taille =randrange(1,17)
        for g in range (taille):
            c=randrange(0,2)
            if c==1:
                ch+='1'
            else:
                ch+='0'
    print("nombre binaire",ch)
    return ([ch, p, oper])
    
##################################


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
           
def repEx4(ch,puis,oper):

   
    if oper=='*':
        rep=ch+'0'*puis
    elif oper=='/':
        rep=ch[:-puis]
    return (rep)

for i in range(5):
    donnees=Alea4()
    print("les données : ", donnees)
    print("reponse ", repEx4(donnees[0], donnees[1], donnees[2]))
                  
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
    
