from random import *
def CtrlSyntaxe(ch,syn,min,max):
        ##controle la syntaxe de ch en fonction de syn (ch peux être un nombre en base 2, 8, 10, 16, piussance syn prendra respectivement les valeurs2, 8 ,10, 16, puissance pour indiquer la syntaxe que ch doit avoir.
        mot2='01'
        mot8='01234567'
        mot10='0123456789'
        mot16='0123456789ABCDEF'
        a=True
        
        if len(ch)<min or len(ch)>max:
            a=False
        else:
            if syn == 2:
                for i in ch:
                    if i not in mot2:
                        a=False
            elif syn == 8:
                for i in ch:
                    if i not in mot8:
                        a=False
            elif syn == 10:
                for i in ch:
                    if i not in mot10:
                        a=False
            elif syn == 16:
                for i in ch:
                    if i not in mot16:
                        a=False
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

def VerifRep(rep,util):
        #Compare la réponse à l’exercice (rep) avec la réponse de l’utilisateur (util)
        if rep == util:
            print("Bravo")
        else:
            print("Perdu")



#========================Données Aléatoires==============================
def Binaire_aleaEx2():
    a = AleaExAll(2,1,16)
    b = AleaExAll(2,1,16)
    signe = randint(1,3) # pour les 3 opérateurs différents, le +, - et *
    if signe == 1:
        oper = '+'
    elif signe == 2:
        oper = '-'
    elif signe == 3:
        oper = '*'
    return(a,b,oper)

#========================Saisie Manuelle==============================

def Binaire_saisEx2():
    oper = input("Saisissez un opérateurs entre * , - ou + : ")
    Entier1 = input("Saisissez le premier entier binaire de moins de 16 bits : ")
    ent1=CtrlSyntaxe(Entier1,16,1,16)
    if ent1 == True:
        a = Entier1
    else:
        print("erreur de saisie")
    print(Entier1)
    print(a)
    Entier2 = input("Saisissez le second entier binaire de moins de 16 bits : ")
    ent2=CtrlSyntaxe(Entier2,16,1,16)
    if ent2 == True:
        b = Entier2
    else:
        print("erreur de saisie")
    print(Entier2)
    print(b)
    return(a,b,oper)

#========================Calcul de la réponse selon les données==============================
def RepExo2 (ch1,ch2,signe):
    if signe == '*':
      rep = (bin(int(ch1, 2) * int(ch2, 2)).replace('0b',''))
    elif signe == '+':
      rep = (bin(int(ch1, 2) + int(ch2, 2)).replace('0b',''))
    elif signe == '-':
      rep = (bin(int(ch1, 2) - int(ch2, 2)).replace('0b',''))
    return(rep)
#bin permet de faire des calcul entre chiffre binaire mais il rajoute toujours un 0b devant, donc il faut mettre ".replace('0b','')" derrière pour enlever le 0b




def Exo2():
    #Saisie=Binaire_saisEx2()
    Saisie=Binaire_aleaEx2()
    rep = RepExo2(Saisie[0],Saisie[1],Saisie[2])

    print("Les valeurs", Saisie)
    print(" ")
    print(rep)
    util = input("Saisissez la réponse au calcul :")

    #========================Vérification==============================
    # (rep => réponse calculé) qui est comparé à (util => réponse de l'utilisateur)
    VerifRep(rep,util)

Exo2()
