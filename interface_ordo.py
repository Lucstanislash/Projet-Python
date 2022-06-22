from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox

fenetre=Tk()
fenetre.config(background="lightskyblue1")
##fenetre.attributes('-fullscreen', True)

fenetre.rowconfigure(1, weight=0)
fenetre.rowconfigure(2, weight=0)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=1)
fenetre.rowconfigure(7, weight=1)
fenetre.rowconfigure(8, weight=1)
fenetre.rowconfigure(9, weight=1)
fenetre.rowconfigure(10, weight=1)
fenetre.rowconfigure(11, weight=1)
fenetre.rowconfigure(12, weight=1)
fenetre.rowconfigure(13, weight=1)
fenetre.rowconfigure(14, weight=1)
fenetre.rowconfigure(15, weight=1)
fenetre.rowconfigure(16, weight=1)
fenetre.rowconfigure(17, weight=1)
fenetre.rowconfigure(18, weight=1)



fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)
fenetre.columnconfigure(3, weight=1)
fenetre.columnconfigure(4, weight=1)
fenetre.columnconfigure(5, weight=1)
fenetre.columnconfigure(6, weight=1)
fenetre.columnconfigure(7, weight=1)
fenetre.columnconfigure(8, weight=1)
fenetre.columnconfigure(9, weight=1)
fenetre.columnconfigure(10, weight=1)
fenetre.columnconfigure(11, weight=1)
fenetre.columnconfigure(12, weight=1)


Li=["Tourniquet","FIFO","PCTER","Priorite fixes","Algorithmes multifiles FIFO sans migration","Algorithmes multi files FIFO avec migration","Algorithmes multi files TOURNIQUET sans migration","Algorithmes multi files TOURNIQUET avec  migration"]


def debloq():

    formats=fenetre.menu.get()
    nbprocs['state']='normal'
    
    if formats=='Tourniquet' or formats=='Algorithmes multi files TOURNIQUET sans migration' or formats=='Algorithmes multi files TOURNIQUET avec  migration':
        Quantum['state']='normal'
    else:
        Quantum['state']='normal'
        Quantum.insert(0,"Donnée non utile")
        Quantum['state']='disabled'
       
        
def CtrlDonnee():
    
    nbprocessus=nbprocs.get()
    quantum=Quantum.get()


    if Quantum['state']=='disabled':

        if nbprocessus=='':
            messagebox.showinfo(title="Information",
                                                    message="Veuillez saisir une réponse")
            return(1)
        else:
            if "." in nbprocessus or "." in quantum :
                messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                return(1)
            else:
                
                ctrl=CtrlSyntaxe(str(nbprocessus),10,1,2,4,10)
                if ctrl==False:
                    messagebox.showinfo(title="Information",
                                                        message="Nombre de processus non compris dans l'intervalle")
                    return(1)
                else:
                    nbprocs['state']='disabled'
    else:

        if nbprocessus==''and quantum=="":

            messagebox.showinfo(title="Information",
                                                    message="Veuillez saisir une réponse")
            return(1)
        else:
            
            if "." in nbprocessus or "." in quantum :
                messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                return(1)
            else:
                ctrl=CtrlSyntaxe(str(nbprocessus),10,1,2,4,10)

                ctrl2=CtrlSyntaxe(str(quantum),10,1,2,1,4)
                if ctrl==False:
                    messagebox.showinfo(title="Information",
                                                        message="Nombre de processus non compris dans l'intervalle")
                    return(1)
                
                else:
                    if ctrl2==False:
                        messagebox.showinfo(title="Information",
                                                       message="Nombre de quantum non compris dans l'intervalle")
                        return(1)
                    else:
                        nbprocs['state']='disabled'
                        Quantum['state']='disabled'
                    
           
                   
                

def buttonGo():
    
    ok=CtrlDonnee()

    if not ok==1:
    
        print("yo")
    
fenetre.menu= tk.StringVar(fenetre)
menu= ttk.OptionMenu(fenetre,fenetre.menu,Li[0], *Li)
menu.grid(row=4, column=3,columnspan=5,sticky='w',ipady=10,ipadx=100)


ttmenu=Label(fenetre, text="Sélectionner le type \n ordonnancement voulue", font=("Courier", 20, "italic"), fg='black', bg='lightskyblue1')
ttmenu.grid(row=3, column=3,columnspan=5,sticky='w')

OK=Button(fenetre, text="Débloquer données", font=("calibri", 15, "bold",), fg='white', bg='#103985', width=17, height=0,command=lambda:debloq())
OK.grid(row=5, column=2,columnspan=3)

ttprocs=Label(fenetre, text="Nombre de \nprocessus", font=("Courier", 20, "italic"), fg='black', bg='lightskyblue1')#titre pour le nombre de processus
ttprocs.grid(row=3, column=5,columnspan=6,)

nbprocs=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le nombre de processus
nbprocs.grid(row=4, column=5,columnspan=6,ipady=15,ipadx=30)


ttQuantum=Label(fenetre, text="Quantum", font=("Courier", 20, "italic"), fg='black', bg='lightskyblue1')#titre pour le quantum
ttQuantum.grid(row=3, column=7,columnspan=8,)

Quantum=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le quantum
Quantum.grid(row=4, column=7,columnspan=8,ipady=15,ipadx=30)


GO=Button(fenetre, text="GO", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=5, height=0,command=lambda:buttonGo())
GO.grid(row=4, column=10,columnspan=12,sticky='n')



affcase=Button(fenetre, text="Afficher les cases", font=("calibri", 15, "bold"), fg='white', bg='#103985', width=17, height=0)
affcase.grid(row=17, column=2,columnspan=3)


titre=Label(fenetre, text="Ordonnancement", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  
soustitre=Label(fenetre, text="Quelques Indications:  ", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

titre.grid(row=1, column=4,columnspan=7)
soustitre.grid(row=2, column=3,columnspan=5,sticky='w',ipady=40)

B1=Button(fenetre, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B4=Button(fenetre, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,state='disabled')
 
B5=Button(fenetre, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fenetre.destroy)

B1.grid(row=18, column=3)
B2.grid(row=18, column=5)
B3.grid(row=18, column=7)
B4.grid(row=18, column=9)
B5.grid(row=18, column=12)

##############################################################Fenetre rappel####################################################################
def create():
        rappel = Toplevel(fenetre)
        rappel.config(background="lightskyblue1")
        titre=Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1')
        titre.grid(row=1, column=2,columnspan=3,sticky='s')

        txt1=Label(rappel, text="Multiplication :", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg='lightskyblue1',width=40, height=2)
        txt2=Label(rappel, text="Ajouter des 0 à la fin du nombre en base 2 donné", font=("courier", 16, "italic"), fg='darkslateblue', bg='lightskyblue1',width=60, height=2)
        txt3=Label(rappel, text="Division : ", font=("courier", 20, "italic",'bold'), fg='darkslateblue', bg= 'lightskyblue1',width=40, height=2)
        txt4=Label(rappel, text="Supprimer des 0 à la fin du nombre en base 2  donné", font=("courier", 16, "italic"), fg='darkslateblue', bg='lightskyblue1',width=60, height=2)

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



fenetre.mainloop()
