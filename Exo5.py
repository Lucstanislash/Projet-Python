# _*_ coding:Utf-8 _*_

from random import *
from outils import*


lis=["SVA","C2"]

def  AleaFormat5(Li):
        i=randrange(0,2)
        formats=Li[i]
        return(formats)

def AleaEnt5():
        ent=AleaExAll(2,8,16)
        return(ent)

def RepExA5(entier):
        
        signe=list(entier)

        if signe[0]=='0' :
                
                rep="positif"# positif

        else:
                rep="negatif"# négatif
        
        return(rep)

        
def ExoA5():

        formats=AleaFormat5()
        entier=AleaEnt5()
        rep=RepExA5(entier)
        
        print("Format",formats)
        print(" ")
        print("Valeur",entier)
        print(" ")

        util=input("positif ou négatif \n")

        VerifRep(rep,util)


def SaisieExB5():       

#Une fois dans l'interface remplacer la saisie manuel des bases
#par un menu déroulant, actuellment impossible car pas interface

        
        BaseD=input("Saisir la base de départ")
        BaseA=input("Saisir la base d'arivée")
        Bits=int(input("Saisir les bits"))
        
        min= 1-2**(Bits-1)
        max= 2**(Bits-1)-1
        
        print (min)
        print(max)

        
        if BaseD=="SVA" or BaseD=="C2":
                ch=input("Saisir la valeur à convertir")
                ctrl=CtrlSyntaxe(ch,2,0,16)

        elif BaseD=="10":
                ch=input("Saisir la valeur à convertir")
                ctrl=CtrlSyntaxe(ch,10,0,4,min,max)
        else:
                ctrl= "Mauvaise base de départ"

        if ctrl== True :

                return(ch,BaseD,BaseA)


Li=["10","SVA","C2"]

def  AleaFormatB25(Li):
        i=randrange(0,3)
        basedep=Li[i]
        return(basedep)
        
def AleaFormatBis5(basedep):

        Libis=Li.copy()
        Libis.remove(basedep)
        i=randrange(0,2)
        basearriv=Libis[i]
        return (basearriv)

def AleaExB5():

        basedep=AleaFormatB25(Li)
        bits=randint(1,16)
         
                
        min= 1-2**(bits-1)
        max= 2**(bits-1)-1

        basearriv=AleaFormatBis5(basedep)
        
        if basedep=="SVA" :
                ent=AleaExAll(2,8,16)
                
        elif basedep=="C2":
                ent=AleaExAll(2,8,16)                
        else:
                 ent=AleaExAll(10,min,max)
                 
        return(ent,basedep,basearriv)
                







