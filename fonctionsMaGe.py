from math import sqrt               #Dans le module maths importe la fonction racine carré

#Fonctions décimales
def addition(a12,b12):               #Prend deux variables (a12 et b12) et definit la fonction addition
    a,b = eval(a12), eval(b12)       #Transforme les variables en type nombre précédement chaine de caractères
    c=a+b                            #Donne a une valeur c le résultat de a+b 
    return c                         #Retourne la valeur c
    
def soustraction(a12,b12):           #Prend deux variables (a12 et b12) et définit la fonction soustraction
    a,b=eval(a12),eval(b12)          #Transforme les variables en type nombre précédement chaine de caractère
    c=a-b                            #Donne a une valeur c le résultat de a-b
    return c                         #Retourne la valeur c
        
def multiplication(a12,b12):         #Définit la fonction multiplication (a12 et b12) et définit la fonction multiplication
    a,b=eval(a12),eval(b12)          #Transforme les variables en type nombre
    c=a*b                            #Donne a une valeur c le résultat de a*b 
    return c                         #Affiche la valeur c
    
def division(a12,b12):               #Définit la fonction multiplication (a12 et b12) et définit la fonction division
    a,b=eval(a12),eval(b12)          #Transforme les variables en type nombre
    if b==0:                         #Dans le cas du dénominateur qui vaut 0"
        return 'Erreur : Division par 0'  #Afficher 'Erreur : Division par 0'
    else:                            #Si b!=0
        c,d=a//b,a%b                 #c prend la valeur de la division euclidienne de a par b et d prend la valeur du reste de la division euclidienne de a par b
        return c,'reste de ',d       #Retourne c puis le reste de la division de a par b : d

def racine(a12):                     #Definit la fonction racine carré
    a=eval(a12)                      #a prend la valeur numérique de la variable a12
    if a<0:                          #Dans le cas ou a<0
        return "Erreur : Racine carrée d'un nombre négatif"   #Afficher 'Erreur' puisque impossibilité de calculer une racine négative
    else:                            #Sinon
        c=sqrt(a)                    #c prend la valeur de la racine de la variable a
        c=float(c)                   #c change de type et deviens un nombre à virgule
        return c                     #Retourne c

def carre(a12):                      #Définit la fonction carré
    a=eval(a12)                      #a prend la valeur numérique de la variable a12 précédement chaine de caractères
    return a**2                      #Retourne le nombre a puissance 2                      

def puissance(a,n):                  #Définit la fonction puissance et prend deux variables en entrée le nombre a et sa future puissance n
    if checkpuissance(a,n) == False: #Utilise une des fonctions check pour verrifier la taille du nombre
        y="Erreur : L'une des deux valeurs est trop grande" #y prend comme chaine de caractère "Erreur : L'une des deux valeurs est trop grande"
        return y                     #Retourne y
    a,n=eval(a),eval(n)              #a et n prennent respectivement les valeurs de type nombre des valeurs entrées au départ                  
    return a**n                      #Retourne la valeur numérique a**n

#Fin des fonctions décimales
#Fonctions de calcul binaires

def additionbin(a,b):                #Définit la fonction addition en binaire
    if checkneg2(a) == False or checkneg2(b) == False:    #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend la valeur de type chaine de caractère "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Affiche y
    if checkbin(a) == False or checkbin(b) == False:      #Si la fonction de check pour les nombres binaire détecte un nombre qui n'est pas binaire
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend la valeur de type chaine de caractère "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    a,b=bin2dec(a),bin2dec(b)                             #a et b prennent la valeur de la fonction qui convertit un nombre binaire en un nombre décimale (pourtant de type string)
    a,b=eval(a),eval(b)                                   #Change le type des variables de a et de b en type nombre
    c=dec2bin(str(a+b))                                   #La variable c prend la valeur de la fonction convertissant un nombre décimal en binaire de la variable du type string de a+b
    return c                                              #Retourne c

def soustractionbin(a,b):                                #Définit la fonction soustraction en binaire
    if checkbin(a) == False or checkbin(b) == False:     #Si la fonction de check pour les nombres binaire détecte un nombre qui n'est pas binaire
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    if checkneg(a,b) == True:                            #Si la fonction de check pour les négatifs de a ou de b detecte un nombre négatif affiche vrai
        y="Erreur : Le résultat de l'opération est négatif" #y prend comme variable un texte de type string "Erreur : Le résultat de l'opération est négatif"
        return y                                          #Retourne y
    if checkneg2(a) == False or checkneg2(b) == False:   #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"   #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    a,b=bin2dec(str(a)),bin2dec(str(b))                  #Transforme a et b en nombre binaires
    a,b=eval(a),eval(b)                                  #a et b se transforment en type nombre
    c=dec2bin(str(a-b))                                  # c prend la valeur de a-b puis on le transforme en string pour pouvoir passer de c en décimal a c en binaire
    return c                                             #Retourne c

def multiplicationbin(a,b):          #Définit la fonction multiplication en binaire
    if checkneg2(a) == False or checkneg2(b) == False:   #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    if checkbin(a) == False or checkbin(b) == False:     #Si la fonction de check pour les nombres binaire détecte un nombre qui n'est pas binaire
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    a,b=bin2dec(a),bin2dec(b)                            #a et b se transforment en nombre décimaux
    a,b=eval(a),eval(b)                                  #a et b passent du type string au type nombre
    c=dec2bin(str(a*b))                                  #c prend la valeur de a*b puis passe en type string pour etre convertit de décimal à binaire
    return c                                             #affiche c (en binaire)

def divisionbin(a,b):                #Définit la fonction division en binaire
    if checkneg2(a) == False or checkneg2(b) == False:    #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    if checkbin(a) == False or checkbin(b) == False:      #Si la fonction de check pour les nombres binaire détecte un nombre qui n'est pas binaire
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    a,b=bin2dec(a),bin2dec(b)                             #a et b se transforment de décimaux à binaires
    a,b=eval(a),eval(b)                                   #a et b passent du type string au type nombre
    if b==0:                                              #Dans le cas ou b serait égal à 0
        return 'Erreur : Division par 0'                  #Retourner 'Erreur : Division par 0'  
    else:                                                 #Sinon
        c,d=dec2bin(str(a//b)),dec2bin(str(a%b))          #c prend la valeur de la division euclidienne de a par b le tout transformé en binaire et d prend la valeur du reste de la division euclidienne , transformé en binaire
    return c,'Reste de ',d                                #Affiche c puis d

def racinebin(a):                   #Définit la fonction racine en binaire
    if checkneg2(a) == False:                             #Si la fonction de check2 pour le négatif a detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    if checkbin(a) == False:                              #Si la fonction de check pour le nombre binaire détecte un nombre qui n'est pas binaire                              
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    b=bin2dec(a)                                          #b prend la valeur de a et passe de binaire à décimal
    b=int(b)                                              #Transforme b en entier
    c=int(sqrt(int(b)))                                   #C prend la valeur de la racine de l'entier b
    if c**2==b:                                           #Si c au carré vaut b
        c=dec2bin(str(c))                                 #c prend la valeur du type string de c puis se transforme en nombre binaire
        return str(c)                                     #Retourne c qui est en type string
    else:                                                 #Sinon
        return "Erreur : La racine n'est pas un nombre entier" #Retourner "Erreur : La racine n'est pas un nombre entier"

def carrebin(a):                   #Définit la fonction carré en binaire
    if checkneg2(a) == False:                              #Si la fonction de check2 pour le négatif a detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                           #Retourne y
    if checkbin(a) == False:                               #Si la fonction de check pour le nombre binaire détecte un nombre qui n'est pas binaire     
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                            #Retourne y
    a=bin2dec(a)                                           #a prend la valeur de a mais en decimal
    c=int(a)                                               #c prend la valeur de a en entier
    c=dec2bin(str(c**2))                                   #c prend la valeur de c puissance deux transformé en type string dans le but de pouvoir le transformer de decimal à binaire
    return c                                               #Retourne la valeur c

def puissancebin(a,n):             #Définit la fonction puissance en binaire
    if checkneg2(a) == False or checkneg2(n) == False:     #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                           #Retourne y
    if checkbin(a) == False:                               #Si la fonction de check pour le nombre binaire a détecte un nombre qui n'est pas binaire     
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                           #Retourne y
    a,n=int(bin2dec(a)),int(bin2dec(n))                    #a prend la valeur décimale de a (type entier) et n prend la valeur de l'entier décimal de n
    if checkpuissancebin(a,n) == False:                    #Utilise la puissance de check de a et n pour voir si ils ne sont pas trop grands
        y="Erreur : L'une des deux valeurs est trop grande" #y prend la valeur "Erreur : L'une des deux valeurs est trop grande"
        return y                                           #Retourne y
    c=dec2bin(str(a**n))                                   #c prend la valeur de a puissance n transformé en decimal
    return c                                               #Affiche c

#Fin du binaire


#Debut calcul hexa

def additionhex(a12,b12):          #Définit la fonction addition en héxadécimal
    if checkneg2(a12) == False or checkneg2(b12) == False: #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                           #Retourne y
    a,b=eval(hex2dec(a12)),eval(hex2dec(b12))              # a prend la valeur de a12 transformé en décimal puis transformé en type nombre et b également pour b12
    c=dec2hex(str(a+b))                                    #c prend la valeur de a+b transformé en héxadécimal
    return c                                               #Retourne c

def soustractionhex(a12,b12):      #Définit la fonction soustraction en hexadécimal
    if checkneg2(a12) == False or checkneg2(b12) == False: #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                           #Retourne y
    if checkneg(a12,b12)==True:                            #Si la fonction de check pour les négatifs de a ou de b detecte un nombre négatif affiche vrai
        y="Erreur : Le résultat de l'opération est négatif" #y prend comme variable le texte "Erreur : Le résultat de l'opération est négatif"
        return y                                           #Retourne y
    a,b=eval(hex2dec(a12)),eval(hex2dec(b12))              # a prend la valeur de a12 transformé en décimal puis transformé en type nombre et b également pour b12
    a=int(a); b=int(b)                                     #a et b se transforment en type nombre
    c=dec2hex(str(a-b))                                    #c prend la valeur de a-b transformé en héxadécimal                           
    return c                                               #Retourne c

def multiplicationhex(a12,b12):    #Définit la fonction multiplication en héxadécimal
    if checkneg2(a12) == False or checkneg2(b12) == False: #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    a,b=eval(hex2dec(a12)),eval(hex2dec(b12))
    a=int(a); b=int(b)
    c=dec2hex(str(a*b))
    return c

def divisionhex(a12,b12):
    if checkneg2(a12) == False or checkneg2(b12) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    a,b=eval(hex2dec(a12)),eval(hex2dec(b12))
    a=int(a); b=int(b)
    if b==0:
        return 'Erreur : Division par 0'
    else:
        c,d=dec2hex(str(a//b)),dec2hex(str(a%b))
        return c,'et comme reste',d
    
def racinehex(a12):
    if checkneg2(a12) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
    b=hex2dec(a12)
    b=int(b)
    if b<0:
        return "Erreur : Racine carrée d'un nombre négatif"
    else:
        c=int(sqrt(b))
        if c**2==b:
            c=dec2hex(str(c))
            return c
        else:        
            return "Erreur : La racine n'est pas un nombre entier"

def carrehex(a12):
    a=int(hex2dec(a12))
    c=dec2hex(str(a**2))
    return c

def puissancehex(a12,b12):
    if checkneg2(a12) == False or checkneg2(b12) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    a,b=int(hex2dec(a12)),int(hex2dec(b12))
    if checkpuissancehex(a,b) == False:
        y="Erreur : L'une des deux valeurs est trop grande"
        return y
    c=dec2hex(str(a**b))
    return c
#début des fonctions de calcul octales

def additionoct(a,b):
    if checkneg2(a) == False or checkneg2(b) == False:   #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend la valeur de type chaine de caractère "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Affiche y
    if checkoct(a) == False or checkoct(b) == False:      #Si la fonction de check pour les nombres binaire détecte un nombre qui n'est pas binaire
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend la valeur de type chaine de caractère "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    a,b=oct2dec(a),oct2dec(b)                             #a et b prennent la valeur de la fonction qui convertit un nombre binaire en un nombre décimale (pourtant de type string)
    a,b=eval(a),eval(b)                                   #Change le type des variables de a et de b en type nombre
    c=dec2oct(str(a+b))                                   #La variable c prend la valeur de la fonction convertissant un nombre décimal en binaire de la variable du type string de a+b
    return c                                              #Retourne c
def soustractionoct(a,b):                                 #Définit la fonction soustraction en binaire
    if checkneg(a,b) == True:                            #Si la fonction de check pour les négatifs de a ou de b detecte un nombre négatif affiche vrai
        y="Erreur : Le résultat de l'opération est négatif" #y prend comme variable un texte de type string "Erreur : Le résultat de l'opération est négatif"
        return y                                          #Retourne y
    if checkneg2(a) == False or checkneg2(b) == False:     #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"   #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    if checkoct(a) == False or checkoct(b) == False:     #Si la fonction de check pour les nombres binaire détecte un nombre qui n'est pas binaire
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y                        
    a,b=oct2dec(str(a)),oct2dec(str(b))                  #Transforme a et b en nombre binaires
    a,b=eval(a),eval(b)                                  #a et b se transforment en type nombre
    c=dec2oct(str(a-b))                                  # c prend la valeur de a-b puis on le transforme en string pour pouvoir passer de c en décimal a c en binaire
    return c                                             #Retourne c

def multiplicationoct(a,b):          #Définit la fonction multiplication en binaire
    if checkneg2(a) == False or checkneg2(b) == False:   #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    if checkoct(a) == False or checkoct(b) == False:     #Si la fonction de check pour les nombres binaire détecte un nombre qui n'est pas binaire
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    a,b=oct2dec(a),oct2dec(b)                            #a et b se transforment en nombre décimaux
    a,b=eval(a),eval(b)                                  #a et b passent du type string au type nombre
    c=dec2oct(str(a*b))                                  #c prend la valeur de a*b puis passe en type string pour etre convertit de décimal à binaire
    return c                                             #affiche c (en binaire)

def divisionoct(a,b):                #Définit la fonction division en binaire
    if checkneg2(a) == False or checkneg2(b) == False:    #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    if checkoct(a) == False or checkoct(b) == False:      #Si la fonction de check pour les nombres binaire détecte un nombre qui n'est pas binaire
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    a,b=oct2dec(a),oct2dec(b)                             #a et b se transforment de décimaux à binaires
    a,b=eval(a),eval(b)                                   #a et b passent du type string au type nombre
    if b==0:                                              #Dans le cas ou b serait égal à 0
        return 'Erreur : Division par 0'                  #Retourner 'Erreur : Division par 0'  
    else:                                                 #Sinon 
        c,d=dec2oct(str(a//b)),dec2oct(str(a%b))          #c prend la valeur de la division euclidienne de a par b le tout transformé en binaire et d prend la valeur du reste de la division euclidienne , transformé en binaire
    return c,'Reste de ',d                                #Affiche c puis d

def racineoct(a):                   #Définit la fonction racine en binaire
    if checkneg2(a) == False:                             #Si la fonction de check2 pour le négatif a detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    if checkoct(a) == False:                              #Si la fonction de check pour le nombre binaire détecte un nombre qui n'est pas binaire                              
        y="Erreur : Vous avez fait une erreur de syntaxe" #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                          #Retourne y
    b=oct2dec(a)                                          #b prend la valeur de a et passe de binaire à décimal
    b=int(b)                                              #Transforme b en entier
    c=int(sqrt(int(b)))                                   #C prend la valeur de la racine de l'entier b
    if c**2==b:                                           #Si c au carré vaut b
        c=dec2oct(str(c))                                 #c prend la valeur du type string de c puis se transforme en nombre binaire
        return str(c)                                     #Retourne c qui est en type string
    else:                                                 #Sinon
        return "Erreur : La racine n'est pas un nombre entier" #Retourner "Erreur : La racine n'est pas un nombre entier"

def carreoct(a):                   #Définit la fonction carré en binaire
    if checkneg2(a) == False:                              #Si la fonction de check2 pour le négatif a detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                           #Retourne y
    if checkoct(a) == False:                               #Si la fonction de check pour le nombre binaire détecte un nombre qui n'est pas binaire     
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                            #Retourne y
    a=oct2dec(a)                                           #a prend la valeur de a mais en decimal
    c=int(a)                                               #c prend la valeur de a en entier
    c=dec2oct(str(c**2))                                   #c prend la valeur de c puissance deux transformé en type string dans le but de pouvoir le transformer de decimal à binaire
    return c                                               #Retourne la valeur c

def puissanceoct(a,n):             #Définit la fonction puissance en binaire
    if checkneg2(a) == False or checkneg2(n) == False:     #Si la fonction de check2 pour les négatifs de a ou de b detecte un nombre négatif
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                           #Retourne y
    if checkoct(a) == False:                               #Si la fonction de check pour le nombre binaire a détecte un nombre qui n'est pas binaire     
        y="Erreur : Vous avez fait une erreur de syntaxe"  #y prend comme variable un texte de type string "Erreur : Vous avez fait une erreur de syntaxe"
        return y                                           #Retourne y
    a,n=int(oct2dec(a)),int(oct2dec(n))                    #a prend la valeur décimale de a (type entier) et n prend la valeur de l'entier décimal de n
    if checkpuissanceoct(a,n) == False:                    #Utilise la puissance de check de a et n pour voir si ils ne sont pas trop grands
        y="Erreur : L'une des deux valeurs est trop grande" #y prend la valeur "Erreur : L'une des deux valeurs est trop grande"
        return y                                           #Retourne y
    c=dec2oct(str(a**n))                                   #c prend la valeur de a puissance n transformé en decimal
    return c                                               #Affiche c

#Début des fonctions binaires

def bin2dec(x):                     
    if checkbin(x) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    else:            
        x=str(int(x))
        s=0
        for i in x:                    
            s=s*2+int(i)
        return str(s)
        
def bin2hex(x):
    if checkbin(x) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    else:
        y=dec2hex(bin2dec(x))
        return str(y)

def dec2bin(x):
    z = eval(x)
    y = ""
    if z == 0:
        y = '0'
    try:
        if z/int(z)==1:
            while z != 0:
                z, r = z//2, z%2
                y = str(r)+y
        else:
            y="Erreur : Vous avez entré un nombre à virgule"
        return y
    except ZeroDivisionError:
        y='0'
        return y

#Debut de l'hexadecimal

def hex2dec(x):
    y = int(x, 16)
    return str(y)

def hex2bin(x):
    y=dec2bin(hex2dec(x))
    return str(y)

def dec2hex(x):
    z = eval(x)
    chiffre_hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    y = ""
    if z == 0:
        y = '0'
    while z != 0:
        z, r = z//16, z%16
        y = chiffre_hexa[r]+y
    return str(y)
#Fin des conversion hexa

#Début fonctions octal

def oct2dec(x):
    if checkoct(x) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    else:            
        x=str(int(x))
        s=0
        for i in x:                    
            s=s*8+int(i)
        return str(s)

def dec2oct(x):
    z = int(str(x))
    y = ""
    if z == 0:
        y = '0'
    try:
        if z/int(z)==1:
            while z != 0:
                z, r = z//8, z%8
                y = str(r)+y
        else:
            y="Erreur : Vous avez entré un nombre à virgule"
        return y
    except ZeroDivisionError:
        y='0'
        return y

def bin2oct(x):
    if checkbin(x) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    else:
        y=dec2oct(bin2dec(x))
        return str(y)

def oct2bin(x):
    if checkoct(x) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    else:
        y=dec2bin(oct2dec(x))
        return str(y)

def oct2hex(x):
    if checkoct(x) == False:
        y="Erreur : Vous avez fait une erreur de syntaxe"
        return y
    else:
        y=dec2hex(oct2dec(x))
        return str(y)

def hex2oct(x):
    y=dec2oct(hex2dec(x))
    return str(y)

#Fonctions de check

def checkoct(x):
    for i in str(x):
        if i == "8" or i == "9":
            return False
    return True

def checkneg(a,b):
    a,b=eval(a),eval(b)
    if b>a:
        return True
    return False

def checkneg2(x):
    try:
        if x[0] == '-':
            return False
    except IndexError:
        return False
    return True

def checkbin(x):
    for i in x:
        if i != "0" and i != "1":
            return False
    return True

def checkresult(x):
    if len(str(x)) > 20:
        return False
    return True

def checkpuissance(x,y):
    if len(str(x)) > 4 or len(str(y)) > 3:
        return False
    return True

def checkpuissancehex(x,y):
    if len(str(x)) > 3 or len(str(y)) > 2:
        return False
    return True

def checkpuissancebin(x,y):
    if len(str(x)) > 13 or len(str(y)) > 10:
        return False
    return True

def checkpuissanceoct(x,y):
    if len(str(x)) > 5 or len(str(y)) > 4:
        return False
    return True

#Fin des fonctions de check
            
if __name__=="__main__":
    print(oct2dec(10))
    


