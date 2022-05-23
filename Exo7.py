from Outils import*

floatt=-14.21

def Ent_IEEE(floatt):
    """fonction qui transforme un entier en IEEE"""
##conversion float vers entier##
    entier=int(float(floatt))
## conversion entier vers binaire##
    
    binaire= format(entier,'b')
    if int(entier)<0:
        binaire=binaire.replace("-","")    

## on sépare la chaine en 2 le bit implicite dans la première le reste dans l'autre
    ch_imp=binaire[0]
    ch_rest=binaire[1:]

## calcul de exposant puis conv vers binaire
    Exp=127+(len(ch_rest))
 
    ExpB= format(Exp,'b')
     
## calcul de la taille de la mantisse pour les décimaux
    FMantisse= 32-(len(ExpB)+len(binaire))

#transforme la partie décimal d'un float en binaire avec pour longueur FMantisse
    ch_dec=""
    dec=str(float(floatt)).replace(str(int(float(floatt))),'0')

    for i in range(FMantisse):
        dec=float(dec)*2
        if int(dec) >= 1:
            dec-=1
            ch_dec+='1'
        else:
            ch_dec+='0'
##concaténation des diff chaines 
    IEEE=ch_imp+ExpB+ch_rest+ch_dec
    Hexa=Conv(2,16,IEEE)
    Hexa= Hexa.upper()
    return(Hexa)

###IEEE=Ent_IEEE(floatt)


def IEE_Ent(Hexa):
    """fonction qui transforme un IEEE en entier"""
    IEEE=Conv(16,2,Hexa)
    
## récupère  l'exposant en binaire et le bim implicite
    ExpB=IEEE[1:9]
    ch_imp=IEEE[0]
    
## conversion en entier puis - 127 pour déterminer l'exposant
    Exp=int(ExpB,2)

    Exp=Exp-127

##récupère les bits de la valeur de l'entier
    n=Exp+9
    ch_rest=IEEE[9:n]
    finIEEE=IEEE[n:]

## reconstitue la chaine en binaire de l'entier puis conversion de entier
    
    binaire=ch_imp+ch_rest
    entier=int(binaire,2)
    
    if ch_imp[0]=="1":
        entier='-'+str(entier)

    cpt=0
    dec=0
    for i in finIEEE:
        cpt-=1
        if i=='1':
            dec+=2**cpt
    dec=round(dec,2)
    
    rep=str(dec).replace("0",entier)  
    return(rep)

lis=["IEEE","entier"]

def  AleaFormat5(lis):
        """Sort aléatoirement une valeur entre 1 et 2 pour choisir la base dans la liste li"""
        i=randrange(0,2)
        formats=lis[i]
        return(formats)
    
def AleaEx7Ent():

    entier=AleaExAll(10,-10000,10000)
    return(entier)
   
def AleaEx7IEEE():   

    Hexa=AleaExAll(16,8,8)
    return(Hexa)

def SaisieAllEx7():
    formats=AleaFormat5(lis)
    if formats=="entier":
            valeur=AleaEx7IEEE()
            
    else:     
            valeur=AleaEx7Ent()
            
    return(valeur,formats)

def SaisieEx7():
    ok=False
    while ok==False:
        formats=str(input("Saisir le format de conversion ( IEEE ou entier)"))
        if formats=="entier":
            nb=str(input("Saisir un Hexa de 8 symbole"))
            ok=CtrlSyntaxe(nb,16,8,8)
        elif formats=="IEEE":
            nb=str(input("Saisir un float de -10000 à 10000"))
            ok=CtrlSyntaxe(nb,10,0,20,-10000,10000)
        else:
            ok=False
    return(nb,formats)

def PrincipalEx7():

    man=input("manuel ou aléatoire \n")
   
    if man=="manuel":
        saisie=SaisieEx7()
        
    elif man=="aleatoire":
        saisie=SaisieAllEx7()
        
    else:
        print("erreur de syntaxe")
        
    formats=saisie[1]
    valeur=saisie[0]    
    print("Formats de conversion",formats)
    print("voici la valeur à convertir",valeur)
    
    if formats=="IEEE":       
        rep=Ent_IEEE(valeur)
        print("voici la réponse ",rep)
        
    else:
        rep=IEE_Ent(valeur)
        print("voici la réponse ",rep)
        
    util=input("Saisir la réponse")
    verif=VerifRep(rep,util)
    
    return(verif)

    
