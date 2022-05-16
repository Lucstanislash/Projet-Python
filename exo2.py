
#========================Données Aléatoires==============================
def Binaire_aleaEx2()
    a = AleaExAll(2,1,16)
    b = AleaExAll(2,1,16)
    signe = randint(1,3) # pour les 3 opérateurs différents, le +, - et *
    if signe == 1
        oper = '+'
    elif signe == 2
        oper = '-'
    elif signe == 3
        oper = '*'
    return(a,b,oper)

#========================Saisie Manuelle==============================

def Binaire_saisEx2(a, b, oper)
    oper = input("Saisissez un opérateurs entre * , - ou + : ")
    a = input("Saisissez le premier entier binaire de moins de 16 bits : ")
    CtrlSyntaxe(a,16)
    b = input("Saisissez le second entier binaire de moins de 16 bits : ")
    CtrlSyntaxe(b,16)

#========================Calcul de la réponse selon les données==============================
def RepExo2 ( a, b, oper)
    if oper == '*'
      rep = ((bin(int(a, 2) * int(b, 2)))
    elif oper == '+'
      rep = ((bin(int(a, 2) + int(b, 2)))
    elif oper == '-'
      rep = ((bin(int(a, 2) - int(b, 2)))
    return(rep)

util = input("Saisissez la réponse au calcul")
#========================Vérification==============================
# (rep => réponse calculé) qui est comparé à (util => réponse de l'utilisateur)
 VerifRep(rep,util)
