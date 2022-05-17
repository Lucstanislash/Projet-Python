
def AleaExA5():
    
#Ici on détemrine si on travaille en SVA ou C2
#Si 1 --> SVA
#Si 0 -->C2
    
    for i in range(1):
        s=randint(0,1)        
    
    if s==1:
        formats="SVA"
    else:
        formats="C2"  
    
    return(formats)

def ent():
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

        formats=AleaExA5()
        entier=ent()
        rep=RepExA5(entier)
        
        print("Format",formats)
        print(" ")
        print("Valeur",entier)
        print(" ")

        util=input("positif ou négatif \n")

        VerifRep(rep,util)
