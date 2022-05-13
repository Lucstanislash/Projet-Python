def Binaire_aleaEx2()

#========================Saisie Manuelle==============================

def Binaire_saisEx2(a, b, oper)
    oper = input("Saisissez un opérateurs entre * , - ou + : ")
    a = input("Saisissez le premier entier binaire de moins de 16 bits : ")
    CtrlSyntaxe(a,16)
    b = input("Saisissez le second entier binaire de moins de 16 bits : ")
    CtrlSyntaxe(b,16)

def RepExo2 ( a, b, oper)
    if oper == '*'
      rep = ((bin(int(a, 2) * int(b, 2)))
    elif oper == '+'
      rep = ((bin(int(a, 2) + int(b, 2)))
    elif oper == '-'
      rep = ((bin(int(a, 2) - int(b, 2)))
    return(rep)
 
# (rep => réponse calculé) qui est comparé à (util => réponse de l'utilisateur)
 VerifRep(rep,util)
