# _*_ coding:Utf-8 _*_

from random import *
from outils import*


lis=["SVA","C2"]

def  AleaFormat5(Li):
        """Sort aléatoirement une valeur entre 1 et 2 pour choisir la base dans la liste li"""
        i=randrange(0,2)
        formats=Li[i]
        return(formats)

def AleaEnt5():
        """Génère aléatoirement un entier en base 2, entre 8 et 16 bits"""
        ent=AleaExAll(2,8,16)
        return(ent)

def RepExA5(entier):
        """permet de généré la réponse , signe positif ou négatif"""
        signe=list(entier)

        if signe[0]=='0' :
                
                rep="positif"# positif

        else:
                rep="negatif"# négatif
        
        return(rep)

        
def ExoA5():
        """génère l'entier, puis l'utilisateur saisie la réponse puis verif avec la rep"""
        formats=AleaFormat5()
        entier=AleaEnt5()
        rep=RepExA5(entier)
        
        print("Format",formats)
        print(" ")
        print("Valeur",entier)
        print(" ")

        util=input("positif ou négatif \n")

        VerifRep(rep,util)



Li=["10","SVA","C2"]

def  AleaFormatBi5(Li):
        """Sort aléatoirement une valeur entre 0 et 3 pour choisir la base dans la liste li"""
        i=randrange(0,3)
        basedep=Li[i]
        return(basedep)
        
def AleaFormatBis5(basedep):
        """on a retiré la base choisi aléatoirement puis on retire aléatoirement la base d'arrivé"""
        Libis=Li.copy()
        Libis.remove(basedep)
        i=randrange(0,2)
        basearriv=Libis[i]
        return (basearriv)

def AleaExB5(basedep):
        """cree un entier aleatoire dans la bse basedep"""
        
        bits=randint(4,16)    
                
        min= 1-2**(bits-1)
        max= 2**(bits-1)-1

        
        if basedep=="SVA" :
                ent=AleaExAll(2,8,16)
        elif basedep=="C2":
                ent=AleaExAll(2,8,16)
                
        else:
                ent=AleaExAll(10,min,max)               
                 
        return(ent)



def C2_ent(C):
        
    """Conversion  C2 vers entier"""

    if C[0]=="0":       
        return int(C,2)
    else:
        return int(C,2)-(1<<len(C))



def EntierC2(entier):
    """Conversion entier vers C2"""    
    switch=''
    binaire=format(int(entier),'b')
    
    for i in binaire:
        if i == '1':
            switch+='0'
        else:
            switch+='1'
    
    rep=(bin(int(str(switch), 2) + int(str(1), 2)).replace("0b",""))
    if int(entier)>0:
        rep='0'+rep
    return(rep)

def C2_SVA(basedep,entier):
        
        """Conversion C2 vers SVA"""  
        if basedep=="C2":
                
                entier=C2_ent(entier)
                rep=Ent_SVA(entier)
                                
        else:
                rep=SVA_Ent(entier)
                rep=EntierC2(rep)
                
        return(rep)


                
def Ent_SVA(entier):
     """Conversion entier vers SVA"""     
     rep=format(int(entier),'b')
        
     if int(entier)<0:
        rep=rep.replace("-","1")

     else:
        rep='0'+rep
        
     return(rep)

def SVA_Ent(entier):
      """Conversion SVA vers entier"""                
      rep=int(entier[1:],2)
      
      if entier[0]=="1":
        rep='-'+str(rep)

      return(rep) 


                
def RepExB5(basedep,entier,basearriv):
        """exercice global avec choix aléatoire de la base + valeur de la réponse"""
        
        print("Voici l'entier",entier)
        print("Voici la base de départ",basedep)
        print("Voci la base d'arrivée",basearriv)

        if basedep=="10":
                if basearriv=="C2":
                     rep=EntierC2(entier)
                else:
                     rep=Ent_SVA(entier)
                        
                                               
                
        elif basedep=="C2":
                if basearriv=="10":
                      rep=C2_ent(entier)
                      
                else:
                      rep=C2_SVA(basedep,entier)
                      
                      
        else:
                if basearriv=="10":                     
                      rep=SVA_Ent(entier)
                                             
                else:
                      rep=C2_SVA(basedep,entier)
               
        
        return(rep)

def SaisieAll():
        """Saisie aléatoire des bases"""        
        basedep=AleaFormatBi5(Li)
        entier=AleaExB5(basedep)
        basearriv=AleaFormatBis5(basedep)

        return(basedep,entier,basearriv)

def SaisieExB5():       

#Une fois dans l'interface remplacer la saisie manuel des bases
#par un menu déroulant, actuellment impossible car pas interface

        """Saisie manuel des bases et verif"""
        
        BaseD=input("Saisir la base de départ")
        BaseA=input("Saisir la base d'arivée")
        Bits=int(input("Saisir les bits"))
        
        min= 1-2**(Bits-1)
        max= 2**(Bits-1)-1

        
        if BaseD=="SVA" or BaseD=="C2":
                entier=input("Saisir la valeur à convertir")
                ctrl=CtrlSyntaxe(ch,2,0,16)

        elif BaseD=="10":
                entier=input("Saisir la valeur à convertir")
                ctrl=CtrlSyntaxe(entier,10,0,4,min,max)
        else:
                ctrl= "Mauvaise base de départ"

        if ctrl== True :

                return(entier,BaseD,BaseA)
