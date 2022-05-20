from tkinter import *
from Exercice3 import *

fenetre=Tk()
fenetre.config(background='lightskyblue1')

cadre1=Frame(fenetre, bg='lightskyblue1') # création d'un premier cadre
cadre2=Frame(fenetre, bg='lightskyblue1')
cadre3=Frame(fenetre, bg='lightskyblue1')

my_scrollbar = Scrollbar(cadre2, orient= VERTICAL) #pour pouvoir se déplacer verticallement
#====================================cadre1
titre=Label(cadre1, text="Multiplication en binaire", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.pack(pady= 10, expand=YES) # Placement de l'invite
#soustitre=Label(cadre1, text="Quelques Indications: ", font=("courier", 18), fg='red', bg='lightskyblue1') 
#soustitre.pack(pady= 10, side=LEFT) 

#===================================cadre2
#puissance
txt1=Label(cadre2, text="Puissance de 2", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt1.place(x=100, y=100)
saisieVal=Entry(cadre2) 
saisieVal.place(x=700, y=100, width=500, height=48) # Placement de la zone de saisie

#choix aleatoire
txt2=Label(cadre2, text="Entiers en binaire", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
txt2.place(x= 75, y= 200)

my_listbox=Listbox(cadre2,width=80,yscrollcommand = my_scrollbar.set, selectmode = MULTIPLE)
my_scrollbar.config(command = my_listbox.yview) #####
my_scrollbar.pack(side = RIGHT, fill=Y)         #####
my_listbox.place(x= 700, y= 200)                      #####

l = []
List(l) 
my_list = l

for i in my_list:
    my_listbox.insert(END, i)

select= Button(cadre2, text="Aucunue de ces réponses", width=20, height=1)
select.place(x= 710, y= 370)

def select():
    my_label.config(text = my_listbox.get(ANCHOR))

select= Button(cadre2, text="selectionner", width=20, height=1, command = select)
select.place(x= 870, y= 370)

def delet():
    my_label.delete(ANCHOR)
    my_label.config(text ='')

select= Button(cadre2, text="supprimer", width=20, height=1, command = delet)
select.place(x= 1030, y= 370)




#======================Cadre 3
B1=Button(cadre3, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='red', bg='#103985', width=20, height=2)
B1.grid(row=0, column=0, pady=10, padx=10)
B2=Button(cadre3, text="Nouveau", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2)
B2.grid(row=0, column=1, pady=10, padx=10)
B3=Button(cadre3, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2)
B3.grid(row=0, column=2, pady=10, padx=10)
B4=Button(cadre3, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=20, height=2, relief="solid")
B4.grid(row=0, column=3, pady=10, padx=10)
B5=Button(cadre3, text="Quitter", font=("calibri", 18, "bold"), fg='red', bg='grey', width=20, height=2)
B5.grid(row=0, column=4, pady=10, padx=10)  

cadre1.pack(fill=BOTH)
cadre2.pack(fill=BOTH, expand=1)
cadre3.pack(fill=BOTH)
fenetre.mainloop
