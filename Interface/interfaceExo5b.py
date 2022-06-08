from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox

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
        
        bit=randint(4,16)
        print(bit)
                
        min= 1-2**(bit-1)
        print(min)
        
        max= 2**(bit-1)-1
        print(max)
        
        if basedep=="SVA" :
                ent=AleaExAll(2,bit,bit)
        elif basedep=="C2":
                ent=AleaExAll(2,bit,bit)
                
        else:
                ent=AleaExAll(10,min,max)
                           
        return(ent,bit)



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

###############################################################INTERFACE###########################################################################
fenetre=tk.Tk()
fenetre.config(background="lightskyblue1")

fenetre.rowconfigure(1, weight=0)
fenetre.rowconfigure(2, weight=0)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=1)
fenetre.rowconfigure(7, weight=1)
fenetre.rowconfigure(8, weight=1)



fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=1)

man=2

if man==1:
        based=AleaFormatBi5(Li)
        basea=AleaFormatBis5(based)        

        
def Validation():

        ok=True
        saisie=control()
        
        if not saisie==1 :

                Bits=saisie[4]
                entier=saisie[0]
                
                if not Bits=='Appuyer sur Go':
                        rep=RepExB5(saisie[0],saisie[1],saisie[2])
                        
                        for i in range (int(Bits)-len(str(rep))):
        
                                rep="0"+rep
                               
                else:
                        rep=RepExB5(saisie[0],saisie[1],saisie[2])

                print("voici la rep",rep)
                util=saisie[3]
                
                Verif=VerifRep(str(rep),util)

                if ok==True:
                        
                        if Verif == 1:
                                B3['state']='disabled' #bloquer le bouton valider ==> Gagner
                                B2['state']='normal'
                                messagebox.showinfo(title="Information",
                                            message="Bonne Réponse, Bravo !! ")
                        elif Verif == -1:
                                B3['state']='disabled' #bloquer le bouton valider ==> Perdu
                                B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
                                messagebox.showinfo(title="Information",
                                            message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("".join(str(rep))))
                        elif Verif == 0:
                               messagebox.showinfo(title="Information",
                                            message="Mauvaise réponse, réessayer !")
        
def control():
        
        if man==2:

                basedep=fenetre.menud.get()
                basearriv=fenetre.menua.get()
                entier=Val.get()
                Bits=Nb.get()
                util=Resultats.get()

        else :
                
                basedep=menuD.get()
                entier=Val.get()
                basearriv=menuA.get()
                Bits='Appuyer sur Go'
                util=Resultats.get()
                bit=Nb.get()

           
        print("ici la base de départ",basedep)
        print("voici la base arrive",basearriv)
        
        if basedep=="SVA" or basedep=="C2":
                
                if entier=='' or  util=='' :
                        messagebox.showerror("showerror", "Toutes les valeurs ne sont pas saisie")
                        return(1)
                else:
                        ctrl=CtrlSyntaxe(entier,2,2,16)

                        if ctrl==True: 
                                if basearriv=="10":
                                        
                                        Bits='0'
                                        ctrlR=CtrlSyntaxe(util,10,0,5,-99999,99999)

                                        if not ctrlR==True:
                                                
                                                messagebox.showerror("showerror", "erreur de syntaxe dans la réponse")
                                                return(1)
                                else:
                                
                                        if man==2:
                                                ct=CtrlSyntaxe(str(Bits),10,1,10,4,16)
                                        else:
                                                Bits=bit
                                                ct=CtrlSyntaxe(str(Bits),10,1,10,4,16)

                                        if ct == True:
                                        
                                                ctrlR=CtrlSyntaxe(util,2,int(Bits), int(Bits))
                                                if ctrlR==True:
                                                        
                                                        if not len(str(entier))==len(str(util)):
                                                           
                                                                messagebox.showerror("showerror", "Les deux chaines non pas la même longueur")
                                                                return(1)
                                                else:
                                                        
                                                        messagebox.showerror("showerror", "erreur de syntaxe dans la réponse,ou ne correspond pas au nombre de bit")
                                                        return(1)
                                        else:
                                                messagebox.showerror("showerror", "Les bits ne sont pas dans la bonne intervalle")
                                                return(1)

                        else:                   
                                
                                messagebox.showerror("showerror", "erreur de syntaxe sur l'entier de départ")
                                return(1)


                                
        elif basedep=="10":
                
                if entier=='' or Bits==''  or  util=='':
                        messagebox.showerror("showerror", "Toutes les valeurs ne sont pas saisie")
                        return(1)
                else:


                        if man==2:
                                ct=CtrlSyntaxe(str(Bits),10,1,4,4,16)
                        else:
                                Bits=bit
                                print(Bits)
                                ct=CtrlSyntaxe(str(Bits),10,1,4,4,16)
        
                        if ct==True:
                                min= 1-2**(int(Bits)-1)
                                max= 2**(int(Bits)-1)-1
 
                                ctrl=CtrlSyntaxe(str(entier),10,1,10,min,max)
                          

                                if ctrl==True:
                                        ctrlR=CtrlSyntaxe(util,2,int(Bits),int(Bits))

                                        if not ctrlR==True:
                                                 messagebox.showerror("showerror", "erreur de syntaxe dans la réponse")
                                                 return(1)
                                        
                                else:
                                        messagebox.showerror("showerror", "erreur de syntaxe dans l'entier de départ")
                                        return(1)
                                        

                        else:
                                messagebox.showerror("showerror", "Bits non compris dans l'intervalle")
                                return(1)                
            
                
        return(basedep,entier,basearriv,util,Bits)

def go(): # permet d'afficher ou non le nombre de bits et de calculer la valeur absolu
        GO['state']='disabled'


        if man==1:                
                based=menuD.get()
                basea=menuA.get()
                donne=AleaExB5(based)
                val=donne[0]
                bit=donne[1]
                        
                print("go base dep",based)
                print("go base arriv",basea)
                print("voici l'entier",val)
                
                if basea=="SVA"or basea=="C2":
                        if based=="C2" or based=="SVA":

                                Nb.configure(state="normal")
                                Nb.delete(0,END)
                                Nb.insert(0,bit)
                                
                
                        elif based=="10":

                                Nb.configure(state="normal")
                                Nb.delete(0,END)
                                Nb.insert(0,bit)

                               
                elif basea=="10":
                        Nb.configure(state="normal")
                        Nb.delete(0,END)
                        Nb.insert(0,"Donnée non utile")
                        Nb.configure(state="disabled")
                                
                
                Val.configure(state="normal")
                Val.delete(0,END)
                Val.insert(0, val)
                
        
        if man==2:
               
                              
                if fenetre.menud.get()==fenetre.menua.get():
                        messagebox.showerror("showerror", "La base de départ ne peut pas être identique à la base d'arrivée")
                        GO['state']='normal'

                else :
                        Val.configure(state="normal")
                        Val.delete(0,END)

                        if fenetre.menua.get()=="10":
                                
                                Nb.configure(state="normal")
                                Nb.delete(0,END)
                                Nb.insert(0,"Donnée inutile")
                                Nb.configure(state="disabled")
                                                       
                        else:
                                
                                Nb.configure(state="normal")
                                Nb.delete(0,END)

                        GO['state']='disabled'
                 
                

def nouveau():

    B3['state']='normal'
    B2['state']='disabled'
    GO['state']='normal'

    if man ==2 :
            
        Val.delete(0,END)
        Val.insert(0, "Appuyer sur Go")
        Val.configure(state="readonly")
        
        Nb.configure(state="normal")
        Nb.delete(0,END)
        Nb.insert(0, "Appuyer sur Go")
        Nb.configure(state="readonly")
     
        Resultats.delete(0,END)
        
    elif man==1:
       
        based=AleaFormatBi5(Li)
        basea=AleaFormatBis5(based)
      
        Resultats.delete(0,END)
        
        Val.delete(0,END)
        Val.insert(0, "Appuyer sur Go")
        Val.configure(state="readonly")
        
        Nb.configure(state="normal")
        Nb.delete(0,END)
        Nb.insert(0, "Appuyer sur Go")
        Nb.configure(state="readonly")

        menuA.configure(state="normal")
        menuA.delete(0,END)
        menuA.insert(0, basea)
        menuA.configure(state="readonly")

        menuD.configure(state="normal")
        menuD.delete(0,END)
        menuD.insert(0, based)
        menuD.configure(state="readonly")

        
        
        
Val=Entry(justify='center',borderwidth=3)
Val.insert(0, "Appuyer sur Go")
Val.configure(state="readonly")
Val.grid(row=6, column=2,ipadx=200,columnspan=4,ipady=15)        

Nb=Entry(justify='center',borderwidth=3)
Nb.insert(0, "Appuyer sur Go")
Nb.configure(state="readonly")

Nb.grid(row=5, column=2,ipadx=200,columnspan=4,ipady=15)

                
titre=Label(fenetre, text="Conversion", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  

soustitre=Label(fenetre, text="Quelques Indications: valeur 1000000000 impossible à convertir, pas de bits avant 4\n pour les valeurs pas de , mais un .", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

txt1=Label(fenetre, text="Format de départ", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
if man==2:
   
    fenetre.menud= tk.StringVar(fenetre)
    menuD = ttk.OptionMenu(fenetre,fenetre.menud,Li[0], *Li)
else:
    menuD=Entry(fenetre,justify='center',borderwidth=3)
    menuD.insert(0, based)
    menuD.configure(state="readonly")


txt2=Label(fenetre, text="Format d'arrivée", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')
if man==2:
   
    fenetre.menua= tk.StringVar(fenetre)
    menuA = ttk.OptionMenu(fenetre,fenetre.menua,Li[0], *Li)
else:
    menuA=Entry(fenetre,justify='center',borderwidth=3)
    menuA.insert(0, basea)
    menuA.configure(state="readonly")



txt3=Label(fenetre, text="Nombre de bits", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')


txt4=Label(fenetre, text="Valeur de départ", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')



txt5=Label(fenetre, text="Résultats", font=("courier", 27, "italic"), fg='black', bg='lightskyblue1')

Resultats=Entry(fenetre,justify='center',borderwidth=3)



def create():
    rappel = Toplevel(fenetre)
    rappel.config(background="lightskyblue1")
    titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
    titre.grid(row=1, column=2,columnspan=3,sticky='s')

    txt1=Label(rappel, text="Si l’entier codé en SVA/C2 commence par 1 : \n son signe est négatif.", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt2=Label(rappel, text="Si l’entier codé en SVA/C2 commence par 0 : \n son signe est positif.", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)
    txt3=Label(rappel, text="Pour convertir un nombre négatif de C2 vers \n SVA: on soustrait 1,puis on inverse les bits\nen faisant attention au signe.", font=("courier", 25, "italic"), fg='black', bg= 'lightskyblue1',width=40, height=2)
    txt4=Label(rappel, text="Pour coder un entier négatif en C2 :on part \nde la valeur absolue,on inverse les bits puis\n on ajoute 1", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1',width=40, height=2)

    txt1.grid(row=2, column=3,ipadx=50,ipady=40)
    txt2.grid(row=3, column=3,ipadx=50,ipady=40)
    txt3.grid(row=4, column=3,ipadx=50,ipady=40)
    txt4.grid(row=5, column=3,ipadx=50,ipady=40)

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



        
B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Validation())
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,state='disabled')
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fenetre.destroy)


GO=Button(fenetre, text="Go!", font=("calibri", 18, "bold"), fg='white', bg='#103985', width=10, height=0,command=lambda:go())        
GO.grid(row=4, column=5,sticky='n')

titre.grid(row=1, column=2,columnspan=3)
soustitre.grid(row=2, column=1,columnspan=5,sticky='w',ipady=40)

txt1.grid(row=3, column=1,columnspan=2,sticky='w')
menuD.grid(row=3, column=2,ipadx=200,columnspan=4,ipady=15)

txt2.grid(row=4, column=1,columnspan=2,sticky='w')
menuA.grid(row=4, column=2,ipadx=200,columnspan=4,ipady=15)


txt3.grid(row=5, column=1,columnspan=2,sticky='w')


txt4.grid(row=6, column=1,columnspan=2,sticky='w')



txt5.grid(row=7, column=1,columnspan=2,sticky='w')
Resultats.grid(row=7, column=2,ipadx=200,columnspan=4,ipady=15)



#bouton#
B1.grid(row=8, column=1)
B2.grid(row=8, column=2)
B3.grid(row=8, column=3)
B4.grid(row=8, column=4)
B5.grid(row=8, column=5)

fenetre.mainloop()
