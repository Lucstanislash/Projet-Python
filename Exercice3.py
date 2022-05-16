import random

def AleaPuissance2():
    ch = ''
    for i in range(random.randrange(1,32)):
        j = random.randint(0,1)
        if j == 0:
            ch += '0'
        else :
            ch += '1'
    return(ch)

l = []
def List(l):
    for i in range(10):
        l.append(AleaPuissance2())


#Quizz : le reste à voir //code interface
#Manipuler les listes pour les avoir sous forme de quizz


        
            


                
            
        
        
            


            
        
