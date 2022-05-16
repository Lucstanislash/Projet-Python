def outils:
    from random import *
    def CtrlSyntaxe(ch,syn,min,max):
        ##controle la syntaxe de ch en fonction de syn (ch peux être un nombre en base 2, 8, 10, 16, en SVA, C2, IEEE 32 bits, syn prendra respectivement les valeurs2, 8 ,10, 16, SVA, C2 ou IEEE pour indiquer la syntaxe que ch doit avoir.
        mot2='01'
        mot8='01234567'
        mot10='0123456789'
        mot16='0123456789ABCDEF'
        a=True
        print(len(ch))
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

    a=0
    cpt = 0
    def VerifRep(rep,util):
        #Compare la réponse à l’exercice (rep) avec la réponse de l’utilisateur (util)
        if rep == util:
            a=1 #bloquer le bouton valider
        else:
            global cpt
            cpt = cpt + 1
            if cpt>2:
                a=-1 #bloquer le bouton valider
            else:
                a=0 #reesayer
        print(a)
        return(a)

    
        















































