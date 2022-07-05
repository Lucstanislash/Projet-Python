from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox

fenetre=Tk()
fenetre.config(background="lightskyblue1")
##fenetre.attributes('-fullscreen', True)
fenetre.geometry("1500x700")
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

man=2

Li=["Tourniquet","FIFO","PCTER","Priorite fixes","Algorithmes multi files FIFO sans migration","Algorithmes multi files FIFO avec migration","Algorithmes multi files TOURNIQUET sans migration","Algorithmes multi files TOURNIQUET avec  migration"]

#====================================================
def CalculMoy(lp):
    nb_proc= 10
    t_sejour = 0
    somme_sej=0
    for element in lp:
        t_sejour += element['d']
        #date_fin = t_sejour+element['date_arriv']
        somme_sej=somme_sej+ t_sejour
        #moysej=float(somme_sej)/nb_proc
    p1= somme_sej
    p2= nb_proc
   
    return (p1,p2)
#====================================================
def CalculRep(Duree,lp,Type,Quantum):
    cpt=0
    pret=[]
    ordo=[]
    execute=[]
    for t in range(Duree):
        ici=len(lp)
        for i in range(len(lp)):
            if lp[i]["da"]==t:
                pret.append(lp[i])
            else:
                ici=i
                break
        if Type=="Tourniquet":
            if execute!=[]:
                pret.append(execute[0])
                execute=[]
        if Type=="PCTER":
            pret=sorted(pret, key=lambda x: x["d"])
        if Type=="Priorite fixes":
            pret=sorted(pret, key=lambda x: x["prio"])
        lp=lp[ici: ]
        if pret==[]:
            break
        ordo.append({"temps":t, "nump":pret[0]["n"]})
        pret[0]["d"]-=1
        if pret[0]["d"]<=0:
            pret=pret[1:]
            if Type=="Tourniquet":
                cpt=0
        else:
            if Type=="Tourniquet":
                if cpt==Quantum-1:
                    execute.append(pret[0])
                    pret=pret[1:]
                    cpt=0
                else:
                    cpt+=1
    
    return(ordo)

def CalculRepFile(Duree,lp,Type):
    pretF1=[]
    pretF2=[]
    pretF3=[]
    ordo=[]
    executeF1=[]
    executeF2=[]
    executeF3=[]
    QF2=2
    QF3=3
    cptF2=0
    cptF3=0
  
    for t in range(Duree):
        ici=len(lp)
        
        for i in range(len(lp)):
           
            if Type=="Algorithmes multi files TOURNIQUET avec migration" or Type=="Algorithmes multi files FIFO avec migration":
                if lp[i]["da"]==t:
                    pretF1.append(lp[i])
        
                else:
                    ici=i
                    break
            elif Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
         
               
                if lp[i]["da"]==t and lp[i]["prio"]==1:
                    pretF1.append(lp[i])
                    
                elif lp[i]["da"]==t and lp[i]["prio"]==2:
                    pretF2.append(lp[i])
                   
                elif lp[i]["da"]==t and lp[i]["prio"]==3:
                    pretF3.append(lp[i])
                    
                else:
                    ici=i
                    break
        if Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
            if executeF1!=[]:
                pretF1.append(executeF1[0])
                
                executeF1=[]
            if executeF2!=[]:
                pretF2.append(executeF2[0])
                
                executeF2=[]
        if Type=="Algorithmes multi files TOURNIQUET sans migration" or "Algorithmes multi files TOURNIQUET avec migration":
            if executeF3!=[]:
                pretF3.append(executeF3[0])
                executeF3=[]

        lp=lp[ici: ]
        
        if pretF1!=[]:
            ordo.append({"temps":t, "nump":pretF1[0]["n"]})
            pretF1[0]["d"]-=1
            
            if pretF1[0]["d"]==0:
                pretF1=pretF1[1:]
            else:
                if Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
                    executeF1.append(pretF1[0])
                else:
                    pretF2.append(pretF1[0])
                pretF1=pretF1[1:]  
        elif pretF2!=[]:
            
            ordo.append({"temps":t, "nump":pretF2[0]["n"]})
            pretF2[0]["d"]-=1
            if pretF2[0]["d"]==0:
                pretF2=pretF2[1:]
                cptF2=0
            else:
                if cptF2==QF2-1:
                    if Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
                        executeF2.append(pretF2[0])
                    else:
                        pretF3.append(pretF2[0])
                    pretF2=pretF2[1:]
                    cptF2=0
                else:
                    cptF2+=1
        else:
            if pretF3==[]:
                break
            ordo.append({"temps":t, "nump":pretF3[0]["n"]})
            
            pretF3[0]["d"]-=1
            if pretF3[0]["d"]==0:
                pretF3=pretF3[1:]
                if Type=="Algorithmes multi files TOURNIQUET avec migration" or Type=="Algorithmes multi files TOURNIQUET sans migration":
                    cptF3=0
            else:
                if Type=="Algorithmes multi files TOURNIQUET avec migration" or Type=="Algorithmes multi files TOURNIQUET sans migration":
                    if cptF3==QF3-1:
                        executeF3.append(pretF3[0])
                        pretF3=pretF3[1:]
                        cptF3=0
                    else:
                        cptF3+=1
    return(ordo)
    


def dicointolist(ordo):
    liste=[]
    for i in range(len(ordo)):
        liste.append(str(ordo[i]["nump"]))

    return(liste)   



if man==1:
   
    i=randrange(0,7)
    Type=Li[i]
    n=randrange(4,10)
    print("Nombre de processus : ",n)
    mini=0
    maxi=0
    cpt=0
    listarv=[]
    listdur=[]
    listprio=[]
    listp=[]
    listq=[]
    alea={}
    lp=[]
    
    for i in range (n):
        duree=randrange(1,10)
        cpt=cpt+1
        
        listdur.append(duree)
        listp.append(i+1)
        
        arv=randint(mini,maxi)
        listarv.append(arv)
        
        mini=arv
        
        prio=randrange(1,3)
        listprio.append(prio)
        
        maxi=maxi+duree
        q=randrange(1,4)
        quantum=q
        listq.append(quantum)
          
    for i in range(len(listp)):
        if Type=='Priorite fixes' or Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
            lp.append({"n":listp[i],"da":listarv[i],"d":listdur[i],"prio":listprio[i]})
        else :
            lp.append({"n":listp[i],"da":listarv[i],"d":listdur[i],"quantum":listq[i]})


def AleaTab(lp,mode,NbProc,n):
    if man==1:
        global Duree
        i=0
        j=0
        Duree=0
        if mode == "Tout":
            nbc=3
        else:
            nbc=2
        while i<NbProc*nbc and j<len(lp):
            if i+nbc>NbProc*nbc:
                break
            else:
                ListTabl[i].insert(0,lp[j]["da"])
                ListTabl[i+1].insert(0,lp[j]["d"])
                Duree+=(lp[j]["d"])
                
                if nbc==3:
                    ListTabl[i+2].insert(0,lp[j]["prio"])
                i+=nbc
                j+=1

def listintodico(liste):
    li=[]
    i=0
    cpt=0
    print(liste)
    if Type=='Priorite fixes' or Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files FIFO sans migration":
        while i<len(liste):
            if i+3>len(liste):
                break
            li.append({"n": int(liste[cpt]), "da": int(liste[i]), "d": int(liste[i+1]), "prio": int(liste[i+2])})
            cpt+=1
            i=i+3
    else:
        while i<len(liste):
            if i+2>len(liste):
                break
            li.append({"n": int(liste[cpt]), "da": int(liste[i]), "d": int(liste[i+1])})
            cpt+=1
            i=i+2
    return(li)

def ctrltab():
    global Ltab
    global ct
    global Duree
    global lp
    Ltab=[]
    err=[]
    ok=True
    ct=0
    synerror=[]

    
    
    for j in range(len(ListTabl)):

        val=ListTabl[j].get()
        val=Raccourcir(val)

        Ltab.append(val) 

        
        if Ltab[j]=='' or Ltab[j]=='None' :
            messagebox.showinfo(title="Information",
                                                   message="Veuillez remplir toutes les cases")
            ok=False
            return(1)
        
        else :
  
            if not Ltab[0]=='0':
                messagebox.showinfo(title="Information",
                                                 message="Premier processus doit arriver à 0 ")
                return(1)
           
               
            else:
                if "." in Ltab[j] :
                    messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                    ok=False
                    return(1)
                else:
                   ctrl=CtrlSyntaxe(str(Ltab[j]),10,1,2,0,10)
                   
                   if ctrl==False:
                        synerror.append(j)  
                        ListTabl[j].config(bg= "crimson")
                        ct =ct+1
                        ok=False
                
                   else:
                        ListTabl[j].config(bg= "white")
                    
    if ct >= 1:
            messagebox.showinfo(title="Information",
                            message="Erreur de syntaxe ou d'intervalle ")
            return(1)
        
    for i in range(len(ListTabl)):
        lp=listintodico(Ltab)
        Duree=0
        i=0
    while i<len(lp):
        
        Duree+=int(lp[i]["d"])
        
        i=i+1
     
                
def CreaCase():
    global ListNom
    global mycanvas
    global vsb
    global frame_main
 
    if man==2:    
        ok=ctrltab()
    else:
        ok=0

    if ok!=1:
        
        print(Duree)
        frame_main = tk.Frame(fenetre, bg="lightskyblue1")
        frame_main.grid(column=6,row=6,columnspan=9,sticky='nw',pady=40)
        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = tk.Frame(frame_main)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        mycanvas = tk.Canvas(frame_canvas, bg="lightskyblue1")
        mycanvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        vsb = ttk.Scrollbar(frame_canvas, orient="vertical", command=mycanvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
      
        
        mycanvas.configure(yscrollcommand=vsb.set,highlightcolor='lightskyblue1',highlightbackground='lightskyblue1')

        # Create a frame to contain the buttons
        frame_buttons = tk.Frame(mycanvas, bg="lightskyblue1")
        mycanvas.create_window((0, 0), window=frame_buttons, anchor='nw')

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
        if Duree>10:
            c=10
        else:
            c=Duree
        first5columns_width = sum([ListNom[j].winfo_width() for j in range(0, c)])
        first5rows_height = sum([ListNom[i].winfo_height() for i in range(0, 1)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height+200)
        # Set the canvas scrolling region
        mycanvas.config(scrollregion=mycanvas.bbox("all"))    

        tmr['state']='normal'
        affcase['state']='disabled'
            
    
def debloq():
        global Type
        Type=fenetre.menu.get()
        nbprocs['state']='normal'
        B1['state']='normal'
        menu.configure(state="disabled")
        OK['state']='disabled'
        GO['state']='normal'
    
    
        if Type=='Tourniquet' or Type=='Algorithmes multi files TOURNIQUET sans migration' or Type=='Algorithmes multi files TOURNIQUET avec  migration':

            Quantum['state']='normal'
        else:
            Quantum['state']='normal'
            Quantum.insert(0,"Donnée non utile")
            Quantum['state']='disabled'

        
def CtrlDonnee():
    global quantum
    global nbprocessus
    nbprocessus=nbprocs.get()
    nbprocessus=Raccourcir(nbprocessus)
    quantum=Quantum.get()
    quantum=Raccourcir( quantum)



    if Quantum['state']=='disabled':

        if nbprocessus=='':
            messagebox.showerror(title="Information",
                                                    message="Veuillez saisir une réponse")
            return(1)
        else:
            quantum=0
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
                    
                   
                

   
def buttonGo(Type):
    global ListTabl
    global Frame_main
    if man==2:
        ok=CtrlDonnee()
       
    else:
        ok=0
      
    if ok!=1:
        affcase['state']='normal'
        GO['state']='disabled'   
        
        if man==1:
            NbProc = int(n)
        else:    
            NbProc = int(nbprocessus)
        
       
       
        if Type=='Priorite fixes' or Type=='Algorithmes multi files TOURNIQUET sans migration' or Type=='Algorithmes multi files FIFO sans migration':
            mode="Tout"
            NbCaseT = NbProc*3
            NbCaseL = 3
        else:
            mode="None"
            NbCaseT = NbProc*2
            NbCaseL = 2
        
        Frame_main = tk.Frame(fenetre, bg="lightskyblue1")
        Frame_main.grid(column=2,row=6,columnspan=5,pady=40)
     

        # Create a frame for the canvas with non-zero row&column weights
        frame_canvas = tk.Frame(Frame_main)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        canvas = tk.Canvas(frame_canvas, bg="lightskyblue1")
        canvas.grid(row=0, column=0, sticky="news")

        canvas.configure(highlightcolor='lightskyblue1',highlightbackground='lightskyblue1')

        # Create a frame to contain the buttons
        frame_buttons = tk.Frame(canvas, bg="lightskyblue1")
        canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

        # Add 9-by-5 buttons to the frame
        rows = 9
        columns = 10

        colmin=1
        colmax=NbCaseL+1
        lignemin=1
        lignemax=10
        col=0
        ligne=0
        ListTabl=[]
  
        for i in range(NbCaseT):
            Process=str("g"+str(i))
            ListTabl.append(Process)
           
        
        #============titres de colonnes===============
        ProcT=Label(frame_buttons, text="Processus" ,font=("courier", 9), fg='black', bg='white',width=17)
        ProcT.grid(row=lignemin-1, column=col,sticky='s')
        ArrT=Label(frame_buttons, text="Arrivée" ,font=("courier", 9), fg='black', bg='white',width=17)
        ArrT.grid(row=lignemin-1, column=col+1,sticky='s')
        DureeT=Label(frame_buttons, text="Durée" ,font=("courier", 9), fg='black', bg='white',width=17)
        DureeT.grid(row=lignemin-1, column=col+2,sticky='s')
        if mode == "Tout":
            PrioT=Label(frame_buttons, text="Priorité initiale" ,font=("courier", 9), fg='black', bg='white',width=17)
            PrioT.grid(row=lignemin-1, column=col+3,sticky='s')
        #=================Première colonnes des Processus==========================
        for i in range(NbProc):
            Proc=Label(frame_buttons, text="p"+str(i+1) ,font=("courier", 8), fg='black', bg='white',width=17)
            Proc.grid(row=lignemin+ligne, column=col,sticky='s')

            if lignemin+ligne>=lignemax:
                ligne=lignemax
            else:
                ligne+=1
        colmin=1
        colmax=NbCaseL
        lignemin=1
        lignemax=10
        col=0
        ligne=0
            #=================Case vides==========================
        for i in range(NbCaseT):
            ListTabl[i]=Entry(frame_buttons,width=20)
            ListTabl[i].grid(row=lignemin+ligne, column=colmin+col)
        
        
            if colmin+col>=colmax:
                col=0
                ligne+=1
             
            else:
                col+=1
                

        frame_canvas.config(width=520,height=250)
 
        canvas.config(scrollregion=canvas.bbox("all"))
        
        
    if man==1:
        AleaTab(lp,mode,NbProc,n)
 

         
     
       


def CtrlCase():
    global Lutil
    global ct
    
    Lutil=[]
    err=[]
    ok=True
    ct=0
    synerror=[]


    for i in range(len(ListNom)):
        
        val=ListNom[i].get()
        val=Raccourcir( val)

        Lutil.append(val)
        
        if Lutil[i]=='':
            messagebox.showinfo(title="Information",
                                                   message="Veuillez remplir toutes les cases")
            ok=False
            return(1)
               
        else:
            if "." in Lutil[i] :
                messagebox.showerror("showerror", "Erreur de saisie les points ne sont pas acceptés")
                ok=False
                return(1)
            else:
               ctrl=CtrlSyntaxe(str(Lutil[i]),10,1,2,0,10)
               
               if ctrl==False:
                    synerror.append(i)  
                    ListNom[i].config(bg= "crimson")
                    ct =ct+1
                    ok=False
            
               else:
                    ListNom[i].config(bg= "white")
                    i=i+1
                    
    if ct >= 1:
            messagebox.showinfo(title="Information",
                            message="Erreur de syntaxe ou d'intervalle ")
            return(1)
      
def Crepe(Type,Duree,lp):
    print(Type)
    print(lp)
    print("salut",Duree)
    if Type=="Tourniquet"or Type=="FIFO"or Type=="PCTER"or Type=="Priorite fixes":
        rep0=CalculRep(Duree,lp,Type,int(quantum))
        print(rep0)
        rep=dicointolist(rep0)
        print("Voici la rep",rep)

    elif Type=="Algorithmes multi files FIFO sans migration" or Type=="Algorithmes multi files FIFO avec migration"or Type=="Algorithmes multi files TOURNIQUET sans migration" or Type=="Algorithmes multi files TOURNIQUET avec  migration":
        rep0=CalculRepFile(Duree,lp,Type)
        print(rep0)
        rep=dicointolist(rep0)
        print("Voici la rep",rep)

    return(rep,Duree)
    
def validerSaisie(Duree):

    rep=[] 
    reponse=Crepe(Type,Duree,lp)
    rep=reponse[0]
    

    print(rep)
     
    controleC=CtrlCase()
    
    if  controleC != 1 :
            Verif=VerifRep(rep,Lutil)

            if Verif == 1:
                messagebox.showinfo(title="Information",
                                    message="Bonne Réponse,\n\n Veuillez saisir le temps moyen de réponse !! ")
                B3['state']='normal'
                tmr['state']='disabled'
                deno['state']='normal'
                numer['state']='normal'
               
                        
            elif Verif == -1:
                B3['state']='disabled' #bloquer le bouton valider ==> Perdu
                B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
                tmr['state']='disabled'
                messagebox.showinfo(title="Information",
                                    message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("".join(str(rep))))
            elif Verif == 0:
           
                for j in range(Duree):
                    print(Duree)
                    if rep[j]!=Lutil[j]:
                        erreur.append(j)  
                        ListNom[j].config(bg= "crimson")                
                    else:
                        ListNom[j].config(bg= "white")
                        

                messagebox.showinfo(title="Information",
                                    message="Mauvaise réponse, réessayer ")

    
def Valider():
    
        controleTemps=CtrlTmpRep()
        
        if controleTemps!=1:
            
            tmp=CalculMoy(lp)
            numerateur=tmp[0]
            print("chiffre du haut",numerateur)
            denominateur=tmp[1]
            print("chiffre du bas",denominateur)
            
            denomi=deno.get()
            print("voici ton chiffre du bas",denomi)
            numera=numer.get()
            print("voici ton chiffre du haut",numera)
                
            Verif1=VerifRep(numerateur,numera)
            
            Verif2=VerifRep(denominateur,denomi)

            if Verif1 == 1 and Verif2==1:
                B3['state']='disabled' 
                B2['state']='normal'
                messagebox.showinfo(title="Information",
                                message="Bonne Réponse, Bravo !! ")
            elif Verif1 == -1 or Verif2==-1:
                B3['state']='disabled' 
                B2['state']='normal'  
                messagebox.showinfo(title="Information",
                                    message=" Mauvaise réponse, vous avez perdu !\n \n Le résultat est: \n" +("Numérateur ".join(str(numerateur)))+("  Denominateur".join(str(denominateur))))
            elif Verif1 == 0 or Verif2==0:
           
                messagebox.showinfo(title="Information",
                                    message="Mauvaise réponse dans la fraction, réessayer ")  
  
    
def CtrlTmpRep():
    global numera
    global denomi

    denomi=deno.get()
    numera=numer.get()
    
    if numera =='' or denomi=='':
        
            messagebox.showinfo(title="Information",
                                               message="Veuillez remplir la fraction")
            return(1)
               
    else:
            if "." in numera or "." in  denomi :
                messagebox.showerror("showerror", "Erreur pas de points dans la fraction")
                return(1)
            else:
               ctrl2=CtrlSyntaxe(str(denomi),10,1,10,0,20)
               ctrl1=CtrlSyntaxe(str(numera),10,1,10,0,1000)
               
               if ctrl1==False:
                    messagebox.showerror("showerror", "Erreur dans le numerateur")
                    return(1)
               elif ctrl2==False:
                    messagebox.showerror("showerror", "Erreur dans le denominateur")
                    return(1)
                    
                
      
def nouveau():
    if man==2:
        
        OK['state']='normal'
        
        nbprocs['state']='normal'
        nbprocs.delete(0,END)
        nbprocs['state']='disabled'
        
        Quantum['state']='normal'
        Quantum.delete(0,END)
        Quantum['state']='disabled'

        B1['state']='disabled'

        deno['state']='normal'
        deno.delete(0,END)
        deno['state']='disabled'
        
        numer['state']='normal'
        numer.delete(0,END)
        numer['state']='disabled'

        B2['state']='disabled'
        B3['state']='disabled'
        
        Frame_main.destroy()

        frame_main.destroy()

        menu.configure(state="normal")
    
    
    


if man==2:
      
    fenetre.menu= tk.StringVar(fenetre)
    menu= ttk.OptionMenu(fenetre,fenetre.menu,Li[6], *Li)
else:
    menu=Label(fenetre, text=Type, font=("courier", 11), fg='black', bg='white',width=10, height=1)

menu.grid(row=4, column=3,columnspan=3,sticky='nsew',pady=40,padx=20)



tmr=Label(fenetre, text="Temps moyen de réponse", font=("Courier", 15), fg='black', bg='lightskyblue1')
tmr.grid(row=8, column=6,columnspan=7,sticky='w')

deno=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le nombre de processus
deno.grid(row=9,column=6,columnspan=7,sticky='n',ipady=2)

numer=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le nombre de processus
numer.grid(row=7,column=6,columnspan=7,sticky='n',ipady=2)

ligne=Label(fenetre, text="—————————", font=("cadratin", 12), fg='black', bg='lightskyblue1')

ligne.grid(row=8, column=6,columnspan=7,sticky='n',ipady=1)

tmr=Button(fenetre, text="Valider\n saisie ", state='disabled',font=("calibri", 15,"bold",), fg='white', bg='steelblue', width=13, height=0,command=lambda:validerSaisie(Duree))
tmr.grid(row=6, column=11,sticky='e')

ttmenu=Label(fenetre, text="    Sélectionner le type \n   d'ordonnancement voulue", font=("Courier", 20, "italic"), fg='black', bg='lightskyblue1')
ttmenu.grid(row=3, column=3,columnspan=3,sticky='w')


tt=Label(fenetre, text="", font=("Courier", 20), fg='black', bg='lightskyblue1', width=33 ,height=7)
tt.grid(column=2,row=6,columnspan=5,pady=40,sticky='s')


if man ==2:
    
    OK=Button(fenetre, text="Débloquer données", font=("calibri", 15, "bold",), fg='white', bg='steelblue', width=17, height=0,command=lambda:debloq())
    OK.grid(row=5, column=3,columnspan=3)

ttprocs=Label(fenetre, text="Nombre de \nprocessus", font=("Courier", 20, "italic"), fg='black', bg='lightskyblue1')#titre pour le nombre de processus
ttprocs.grid(row=3, column=5,columnspan=6,)


if man==2:
    
    nbprocs=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le nombre de processus   

else:
    nbprocs=Label(fenetre, text=n, font=("courier", 15, "italic"), fg='black', bg='white',width=10, height=1)

nbprocs.grid(row=4, column=5,columnspan=6,ipady=15,ipadx=30)


ttQuantum=Label(fenetre, text="Quantum", font=("Courier", 20, "italic"), fg='black', bg='lightskyblue1')#titre pour le quantum
ttQuantum.grid(row=3, column=7,columnspan=8,)

if man==2:
    
    Quantum=Entry(justify='center',borderwidth=3,state='disabled')#case de saisie pour le quantum

else:

    if Type=='Tourniquet' or Type=='Algorithmes multi files TOURNIQUET sans migration' or Type=='Algorithmes multi files TOURNIQUET avec  migration':

        Quantum=Label(fenetre, text=quantum, font=("courier", 12, "italic"), fg='black', bg='white',width=10, height=1)
    else:
        Quantum=Label(fenetre, text="Données inutiles", font=("courier", 12, "italic"), fg='black', bg='white',width=10, height=1)


Quantum.grid(row=4, column=7,columnspan=8,ipady=15,ipadx=30)


if man==2:
    
    GO=Button(fenetre, text="GO", font=("calibri", 18, "bold", 'underline'), fg='white', bg='steelblue',state='disabled', width=5, height=0,command=lambda:buttonGo(Type))
    GO.grid(row=4, column=10,columnspan=12)
else:
    GO=Button(fenetre, text="GO", font=("calibri", 18, "bold", 'underline'), fg='white', bg='steelblue', width=5, height=0,command=lambda:buttonGo(Type))
    GO.grid(row=4, column=10,columnspan=12)



affcase=Button(fenetre, text="Afficher les cases",state='disabled', font=("calibri", 15, "bold"), fg='white', bg='steelblue', width=17, height=0,command=lambda:CreaCase())
affcase.grid(row=8,column=3,columnspan=3)


titre=Label(fenetre, text="Ordonnancement", font=("Courier", 40, "italic"), fg='black', bg='lightskyblue1')  
soustitre=Label(fenetre, text="Quelques Indications: Nombres de processus compris entre 4-10\n                             Durée d’un processus entre 1-10, Quantum max 4", font=("courier", 17), fg='darkblue', bg='lightskyblue1')

titre.grid(row=1, column=4,columnspan=7)
soustitre.grid(row=2, column=3,columnspan=11,sticky='w',ipady=20,ipadx=50)

if man==1:
    B1=Button(fenetre, text="Rappel", font=("courier", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2,command=lambda:create())

else:
    
    B1=Button(fenetre, text="Rappel", font=("courier", 18, "bold", 'underline'), fg='white', bg='#103985',state='disabled', width=15, height=2,command=lambda:create())

B2=Button(fenetre, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:nouveau())
 
B3=Button(fenetre, text="Valider", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2,command=lambda:Valider())
 
B4=Button(fenetre, text="Menu", font=("courier", 18, "italic"), fg='white', bg='grey', width=15, height=2)
 
B5=Button(fenetre, text="Quitter", font=("courier", 18), fg='white', bg='#103985', width=15, height=2,command=fenetre.destroy)

B1.grid(row=18, column=3,pady=10)
B2.grid(row=18, column=5,pady=10)
B3.grid(row=18, column=7,pady=10)
B5.grid(row=18, column=9,pady=10)
B4.grid(row=18, column=11,pady=10)

##############################################################Fenetre rappel####################################################################
def create():
        if man==1:
            types=typeAl
        else:    
            types=fenetre.menu.get()
            
        rappel = Toplevel(fenetre)
        rappel.config(background="lightskyblue1")
     
            
        Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1').grid(row=1, column=1, columnspan=3)
        
        if types=='Tourniquet':
   
            i="Tourniquet :\n"
            a="Le processus sélectionné est celui en top de liste \net chaque nouveau processus est ajouté en fin de liste\n"
            j="Un processus en cours s'exécute pendant un temps (q)\n et se met en fin de file s’il n’a pas fini \n"
            c="L’arrivée d’un processus avec une plus grande priorité \nentraîne l’arrêt du processus en cours et s'exécute.\n"                      
            
        elif types=='FIFO':
            
            i="FIFO :\n"
            a="FIFO = First-In, First-Out , le premier processus\n arrivé est le premier à s'exécuter\n"
            j="Temps de réponse pour un processus = \nDate de fin - Date d'arrivée \n"
            c="Temps moyen de réponse = somme des temps de réponse \nde chaque processus divisé par nombre de processus\n"                      
            


        elif types=='PCTER':
            
            i="PCTER :\n"
            a="Le processus sélectionné est celui qui a le\n plus court temps d'exécution restant\n"
            j="\n"
            c="\n"                      
            

        elif types=='Priorite fixes':

            i="Priorités fixes :\n"
            a="Comparaison des processus pour trouver celui avec la plus grande priorité\n"
            j="Respecter l’ordre de priorité : si une nouvelle tâche à une plus \n grande priorité le processus est interrompu\n"
            c="Lorsque deux processus ont la même priorités, la règle du FIFO s’applique\n"                      


        else :

            i="Algorithmes multifiles :\n"
            a="Quand une file est ordonnancée par un quantum n elle applique \n son algorithme d'ordonnancement pendant n unités de temps\n\n\n sauf si elle se retrouve vide avant l'expiration du quantum \ndans ce cas la file suivante prend le relai \n\n\n Quand une file est interrompue, elle reprend là où elle en était \n donc si un processus navait pas fini son quantum, il le termine.\n"
            j="FIFO = First-In, First-Out , le premier processus\n arrivé est le premier à s'exécuter\n"
            e="Migration"
            c="Une fois qu'un processus c'est éxcuter 1 fois il passe à la file suivante"
            
            Label(rappel, text=e, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16,'bold')).grid(row=7, column=1, columnspan=3)
          
            
       
       
        
        Label(rappel, text=i, bg='lightskyblue1', fg='darkslateblue', font=('Courier',20,'bold')).grid(row=4, column=1, columnspan=3)                   
        Label(rappel, text=a, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=5, column=1, columnspan=3)
                    
              
        Label(rappel, text=j, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=6, column=1, columnspan=3)

        Label(rappel, text=c, bg='lightskyblue1', fg='darkslateblue', font=('Courier',16)).grid(row=8, column=1, columnspan=3)
        
        
       

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
