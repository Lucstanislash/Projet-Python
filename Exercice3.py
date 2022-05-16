import random

def AleaPuissance2():
    #Donne des nombres binaires aléatoires
    ch = '1'
    for i in range(random.randrange(1,32)):
        j = random.randint(0,1)
        if j == 0:
            ch += '0'
        else :
            ch += '1'
    return(ch)

l = []
def List(l):
    #Crée une liste avec des nombres binaires aléatoires
    for i in range(10):
        l.append(AleaPuissance2())

def RepEx3(l):
    #Donne les bonnes réponses
    for i in l:
        if int(i) % 2 == 0:
            print(i)
            
            
#Manipuler les listes pour les avoir sous forme de quizz / vérification des réponses

#Quizz : le reste à voir //code interface



        
            


                
            
        
        
            


            
        
