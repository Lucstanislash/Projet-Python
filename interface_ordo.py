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

Duree=100
def CreaCase(Duree):
    global ListNom
    frame_main = tk.Frame(fenetre, bg="lightskyblue1")
    frame_main.grid(column=6,row=7,columnspan=9)

    # Create a frame for the canvas with non-zero row&column weights
    frame_canvas = tk.Frame(frame_main)
    frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    frame_canvas.grid_propagate(False)

    # Add a canvas in that frame
    canvas = tk.Canvas(frame_canvas, bg="lightskyblue1")
    canvas.grid(row=0, column=0, sticky="news")

    # Link a scrollbar to the canvas
    vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=vsb.set)

    # Create a frame to contain the buttons
    frame_buttons = tk.Frame(canvas, bg="lightskyblue1")
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

    rows = 9
    columns = 10

    colmin=0
    colmax=9
    lignemin=0
    col=0
    ligne=0
    ListNom=[]
    for i in range(Duree):
        Nom=str("a"+str(i))
        ListNom.append(Nom)
    print(ListNom)
    print(ListNom[1])
    for i in range(Duree):
        ListNom[i]=Entry(frame_buttons,width=10)
        ListNom[i].grid(row=lignemin+ligne, column=colmin+col, pady=25)
        ValTemps=(str(i)+"-"+str(i+1))
        Temps=Label(frame_buttons, text=ValTemps ,font=("courier", 10), fg='black', bg='lightskyblue1')
        Temps.grid(row=lignemin+ligne, column=colmin+col,sticky='s')
        
        if colmin+col>=colmax:
            col=0
            ligne+=1
        else:
            col+=1

    # Update buttons frames idle tasks to let tkinter calculate buttons sizes       
    frame_buttons.update_idletasks()
    # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
    first5columns_width = sum([ListNom[j].winfo_width() for j in range(0, 10)])
    first5rows_height = sum([ListNom[i].winfo_height() for i in range(0, 5)])
    frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                        height=first5rows_height+100)
    # Set the canvas scrolling region
    canvas.config(scrollregion=canvas.bbox("all"))

def get():
    ok=True
    a=[]
    for i in range(len(ListNom)):
        a.append(ListNom[i].get())
    print(a)
   
    
def debloq():

    types=fenetre.menu.get()
    nbprocs['state']='normal'
    B1['state']='normal'
    menu.configure(state="disabled")
    OK['state']='disabled'
    
    if types=='Tourniquet' or types=='Algorithmes multi files TOURNIQUET sans migration' or types=='Algorithmes multi files TOURNIQUET avec  migration':
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
            messagebox.showerror(title="Information",
                                                    message="Veuillez saisir une réponse")
            return(1)
        else:
            if "." in nbprocessus  :
                messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                return(1)
            else:
                
                ctrl=CtrlSyntaxe(str(nbprocessus),10,1,2,4,10)
                if ctrl==False:
                    messagebox.showerror(title="Information",
                                                        message="Erreur de syntaxe ou intervalle non respectée dans nombre de processus")
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
                    messagebox.showerror(title="Information",
                                                        message="Erreur de syntaxe ou intervalle non respectée dans nombre de processus")
                    return(1)
                
                else:
                    if ctrl2==False:
                        messagebox.showerror(title="Information",
                                                       message="Erreur de syntaxe ou intervalle non respectée pour quantum")
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



affcase=Button(fenetre, text="Afficher les cases", font=("calibri", 15, "bold"), fg='white', bg='#103985', width=17, height=0,command=lambda:CreaCase(Duree))
affcase.grid(row=17, column=2,columnspan=3)


titre=Label(fenetre, text="Ordonnancement", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  
soustitre=Label(fenetre, text="Quelques Indications:  ", font=("courier", 20), fg='darkblue', bg='lightskyblue1') 

titre.grid(row=1, column=4,columnspan=7)
soustitre.grid(row=2, column=3,columnspan=5,sticky='w',ipady=40)

B1=Button(fenetre, text="Rappel", font=("courier", 18, "bold", 'underline'), fg='white', bg='#103985',state='disabled', width=15, height=2,command=lambda:create())

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
 
B3=Button(fenetre, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, command=lambda:get())
 
B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2)
 
B5=Button(fenetre, text="Quitter", font=("courier", 18), fg='white', bg='#103985', width=15, height=2,command=fenetre.destroy)

B1.grid(row=18, column=3)
B2.grid(row=18, column=5)
B3.grid(row=18, column=7)
B5.grid(row=18, column=9)
B4.grid(row=18, column=12)

##############################################################Fenetre rappel####################################################################
def create():
        types=fenetre.menu.get()
        rappel = Toplevel(fenetre)
        rappel.config(background="lightskyblue1")
     
            
        Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1').grid(row=1, column=1, columnspan=3)

        if types=='Tourniquet':
            
            i="Tourniquet :\n"
            a="Le processus sélectionné est celui en top de liste \net chaque nouveau processus est ajouté en fin de liste\n"
            j="Un processus en cours s'exécute pendant un temps (q)\n et se met en fin de file s’il n’a pas fini :\n"
            c="L’arrivée d’un processus avec une plus grande priorité \nentraîne l’arrêt du processus en cours et s'exécute.\n"                      
            
        elif types=='FIFO':
            
            i="FIFO :\n"
            a="FIFO = First-In, First-Out , le premier processus\n arrivé est le premier à s'exécuter\n"
            j="Temps de réponse pour un processus = \nDate de fin - Date d'arrivée :\n"
            c="Temps moyen de réponse = somme des temps de réponse \nde chaque processus divisé par nombre de processus\n"                      
            


        elif types=='PCTER':
            
            i="PCTER :\n"
            a="Le processus sélectionné est celui qui a le plus court temps d'exécution restant\n"
            j=" :\n"
            c="\n"                      
            

        elif types=='Priorite fixes':

            i="Priorités fixes :\n"
            a="Comparaison des processus pour trouver celui avec la plus grande priorité\n"
            j="Respecter l’ordre de priorité : si une nouvelle tâche à une plus grande priorité, le processus est interrompu:\n"
            c="Lorsque deux processus ont la même priorités, la règle du FIFO s’applique\n"                      


        elif types=='Algorithmes multi files FIFO avec migration':

            i="Algorithmes multifiles FIFO avec migration:\n"
            a="Quand une file est ordonnancée par un quantum n, elle applique son algorithme d'ordonnancement pendant n unités de temps\nsauf si elle se retrouve vide avant l'expiration du quantum dans ce cas la file suivante prend le relai \n"
            j=":Quand une file est interrompue, elle reprend là où elle en était, donc si un processus n'avait pas fini son quantum, il le termine.\n"
            c="\n"                      
            
        elif types=='Algorithmes multifiles FIFO sans migration':

            i="Algorithmes multifiles FIFO sans migration :\n"
            a="Le processus sélectionné est celui en top de liste \net chaque nouveau processus est ajouté en fin de liste\n"
            j="Un processus en cours s'exécute pendant un temps (q)\n et se met en fin de file s’il n’a pas fini :\n"
            c="L’arrivée d’un processus avec une plus grande priorité \nentraîne l’arrêt du processus en cours et s'exécute.\n"                      
            

        elif types =='Algorithmes multi files TOURNIQUET sans migration':

            i="Algorithmes multifiles TOURNIQUET sans migration :\n"
            a="Le processus sélectionné est celui en top de liste \net chaque nouveau processus est ajouté en fin de liste\n"
            j="Un processus en cours s'exécute pendant un temps (q)\n et se met en fin de file s’il n’a pas fini :\n"
            c="L’arrivée d’un processus avec une plus grande priorité \nentraîne l’arrêt du processus en cours et s'exécute.\n"                      
            

        elif types=='Algorithmes multi files TOURNIQUET avec  migration':

            i="Algorithmes multifiles TOURNIQUET avec migration :\n"
            a="Le processus sélectionné est celui en top de liste \net chaque nouveau processus est ajouté en fin de liste\n"
            j="Un processus en cours s'exécute pendant un temps (q)\n et se met en fin de file s’il n’a pas fini :\n"
            c="L’arrivée d’un processus avec une plus grande priorité \nentraîne l’arrêt du processus en cours et s'exécute.\n"                      
            
       
        
        Label(rappel, text=i, bg='lightskyblue1', fg='darkslateblue', font=('Courier',20,'bold')).grid(row=4, column=1, columnspan=3)                   
        Label(rappel, text=a, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=5, column=1, columnspan=3)
        
                          
        Label(rappel, text=j, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=6, column=1, columnspan=3)                  
        Label(rappel, text=c, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=7, column=1, columnspan=3)
       

        rappel.rowconfigure(1, weight=1)
        rappel.rowconfigure(2, weight=1)
        rappel.rowconfigure(3, weight=1)
        rappel.rowconfigure(4, weight=1)
        rappel.rowconfigure(5, weight=1)
        rappel.rowconfigure(6, weight=1)
        rappel.rowconfigure(7, weight=1)
        rappel.rowconfigure(8, weight=1)
        rappel.rowconfigure(9, weight=1)
        rappel.rowconfigure(10, weight=1)
        rappel.rowconfigure(11, weight=1)
        rappel.rowconfigure(12, weight=1)

        rappel.columnconfigure(1, weight=0)
        rappel.columnconfigure(2, weight=1)
        rappel.columnconfigure(3, weight=0)    

        def exit_btn():

            rappel.destroy()
            rappel.update()

        btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
        btn.grid(row=12, column=1,columnspan=3,sticky='n')


fenetre.mainloop()
