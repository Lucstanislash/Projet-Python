from tkinter import *
from Outils import *
import random
from functools import partial
from tkinter import messagebox


fenetre=Tk()
fenetre.config(background='lightskyblue1')
fenetre.rowconfigure(1, weight=0)
fenetre.rowconfigure(2, weight=0)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=1)

fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=1)
#===================================================================================================================
#=======================================FONCTIONS D'EXERCICE 3
#====================================================================================================================
def AleaEx3(choix,n,mini,maxi):
    
    #Donne des nombres binaires aléatoires
    ch = '1'        
    if choix == 'quelconque':
        taille = randint(mini,maxi)
        for i in range(taille):
            a=randint(0,1)
            ch+=str(a)
    elif choix == 'correct':
        taille = randint(min(mini, n+1), maxi)
        for i in range(taille-n):
            a=randint(0,1)
            ch+=str(a)
        ch+='0'*n # += erreur 
    return(ch)

#=======================================================================================================================
def List(n):
    liste=[]
    #Crée une liste avec des nombres binaires aléatoires 
    for i in range(7): #génère des nombres binaires aléatoires 
        liste.append(AleaEx3('quelconque',n,1,30))
    for i in range(3):#pour avoir au moins 3 réponses correctes
        liste.append(AleaEx3('correct',n,1,30))
    shuffle(liste) #permet de bien mélanger les suggestions
    return(liste)
#========================================================================================================================
def Valid():
    #============================Liste des réponses correctes
    def ReponseEx3(lprop, n):
        RepEx3=[]                   #Récupère les bonnes réponses
        seq='0'*n
        for i in lprop:
            if i[-n:]==seq:         #Remplace le calcul(if int(i,2)% (2**n) == 0:)
                RepEx3.append(i)
            #print(" Mauvaise réponse, vous avez perdu !\n Le résultat est:" + [RepEx3])
        return(RepEx3)

    #============================Liste des réponses d'utilisateur
    def Recup():                    #Récupère les réponses d'utilisateurs
        UtilEx3=[]
        selected_item = StringVar() # on crée une variable StringVar() pour stocker la valeur de l'item sélectionné
        item= my_listbox.curselection() #tous les reponses selectionnées
        for i in item:
            selected_item = my_listbox.get(i) #pour les récuperer
            UtilEx3.append(selected_item)     #pour les ajouter à la liste des reponses d'utilisateurs
        return(UtilEx3)
        #selected_item.set(UtilEx3)
        #on affecte la valeur de l'item à la variable
        #cela affiche les valeur selectionné sur l'unterface

    #===============================Vérification de la Réponse d'utilisateur

    vérif = VerifRep(ReponseEx3(lprop, alea),Recup())
    
    #================================Validation Rep
    global resu
            
    #a=" Mauvaise réponse, vous avez perdu !\n Le résultat est: \n"      
    if vérif == 1:
        B3.destroy() #bloquer le bouton valider ==> Gagner
        messagebox.showinfo(title="Information",
                            message="Bonne Réponse, Bravo !! ")
        #resu=Label(cadre1, text="Bonne Réponse, Bravo !! ", font=("courier", 25, "italic"), fg='green', bg='lightskyblue1')
        #resu.pack(pady= 5, side=TOP)
    elif vérif == -1:
        B3.destroy() #bloquer le bouton valider ==> Perdu
        messagebox.showinfo(title="Information",
                            message=" Mauvaise réponse, vous avez perdu !\n Le résultat est: \n" +("\n".join(ReponseEx3(lprop, alea)))) 
    elif vérif == 0:
        messagebox.showinfo(title="Information",
                            message="Mauvaise réponse, réessayer en cliquant sur NOUVEAU !")#resu=Label(cadre1, text="Mauvaise réponse, réessayer ! ", font=("courier", 25, "italic"), fg='red', bg='lightskyblue1') #width=largeur, height=hauteur ,command= partial(PageChoix,"Entiers non signées")) #, command= PageChoix("Entiers non signées")
        #resu.pack(pady= 5, side=TOP)

#========= Rappel fenetre ==================================
#===========================================================
def create():
    rappel = Toplevel(fenetre)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')

    txt1=Label(rappel, text="Multiplication :", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="Ajouter des 0 à la fin \n du nombre en base 2 donné", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt3=Label(rappel, text="Division : ", font=("courier", 25, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
    txt4=Label(rappel, text="Supprimer des 0 à la fin \n du nombre en base 2  donné", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

    txt1.grid(row=2, column=3)
    txt2.grid(row=3, column=3)
    txt3.grid(row=4, column=3)
    txt4.grid(row=5, column=3)

    rappel.rowconfigure(1, weight=1)
    rappel.rowconfigure(2, weight=1)
    rappel.rowconfigure(3, weight=1)
    rappel.rowconfigure(4, weight=1)
    rappel.rowconfigure(5, weight=1)
    rappel.rowconfigure(6, weight=1)

    rappel.columnconfigure(1, weight=0)
    rappel.columnconfigure(2, weight=1)
    rappel.columnconfigure(3, weight=1)
    rappel.columnconfigure(4, weight=1)
    rappel.columnconfigure(5, weight=0)    

    def exit_btn():

        rappel.destroy()
        rappel.update()

    btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
    btn.grid(row=6, column=2,columnspan=3,sticky='n')

#=============================================================================================================================================#
                                                #INTERFACE GRAFIQUE#
#=============================================================================================================================================#        
#====================================cadre1
titre=Label(fenetre, text="Multiplicité en binaire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.grid(row=1, column=2,columnspan=3) # Placement de l'invite


#===================================cadre2
txt1=Label(fenetre, text="QUESTION: Cochez la bonne réponse...", font=("courier", 20, "bold"), fg='black', bg='lightskyblue1')
txt1.grid(row=2, column=3,columnspan=4,sticky='w',ipady=10)
#choix aleatoire de la puissance de 2
txt2=Label(fenetre, text="Puissance de 2", font=("courier", 20), fg='black', bg='lightskyblue1')
txt2.grid(row=3,column=1,columnspan=2,sticky='w',ipady=10) # Placement de la zone de saisie
t2 = Text(fenetre,  font=("courier", 15), height = 1, width = 25)
t2.grid(row=3, column=3,ipadx=100,columnspan=4,ipady=10)
ch=""
syn='puissanceExp'
alea=AleaExAll('puissanceExp',1, 20)
ch = '2**'+str(alea)
t2.insert(END, ch)

#choix aleatoire d'entiers binaire
txt3=Label(fenetre, text="Entiers en binaire", font=("courier", 20), fg='black', bg='lightskyblue1')
txt3.grid(row=4, column=1,columnspan=2,sticky='w')

my_listbox=Listbox(fenetre,font=("courier", 15), width=25, selectmode = MULTIPLE) #(yscrollcommand = my_scrollbar.set, )
#my_scrollbar.config(command = my_listbox.yview) 
#my_scrollbar.pack(side = RIGHT, fill=Y)         
my_listbox.grid(row=4, column=3,ipadx=100,columnspan=4,ipady=10)                

lprop=List( alea) 
my_list = lprop

for i in my_list:
    my_listbox.insert(END, i)


def select():
    for i in range (10):
        my_listbox.select_set(i)

select= Button(fenetre, text="selectionner tous", width=5, height=1, command = select)
select.grid(row=5, column=2,ipadx=100,columnspan=4,ipady=10)

def delet():
    for i in range (10):
        my_listbox.select_clear(i)

delet= Button(fenetre, text="supprimer", width=5, height=1, command =
delet)
delet.grid(row=5, column=4,ipadx=100,columnspan=4,ipady=10)

def Nouveau ():
    global ch
    B3['state']='normal'
    B2['state']='disabled'
    titre.destroy()
    
    

#======================Cadre 3
B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())
B2=Button(fenetre, text="Nouveau",font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Nouveau())
B3=Button(fenetre, text="Valider",command=Valid, font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, relief="solid")
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=15, height=2)
 

B1.grid(row=7, column=1)
B2.grid(row=7, column=2)
B3.grid(row=7, column=3)
B4.grid(row=7, column=4)
B5.grid(row=7, column=5)
fenetre.mainloop
