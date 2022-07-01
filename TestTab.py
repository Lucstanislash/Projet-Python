from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox

fenetre=Tk()
fenetre.rowconfigure(1, weight=1)
fenetre.rowconfigure(2, weight=1)
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
fenetre.columnconfigure(13, weight=1)
fenetre.columnconfigure(14, weight=1)
fenetre.columnconfigure(15, weight=1)

NbProc = 10
mode = "Tout"
def Tableau(NbProc):
    global ListTabl
    if mode == "Tout":
        NbCaseT = NbProc*3
        NbCaseL = 3
    else:
        NbCaseT = NbProc*2
        NbCaseL = 2
    
    frame_main = tk.Frame(fenetre, bg="lightskyblue1")
    frame_main.grid(column=2,row=6,columnspan=5)

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
    ProcT=Label(frame_buttons, text="Processus" ,font=("courier", 8), fg='black', bg='white',width=17)
    ProcT.grid(row=lignemin-1, column=col,sticky='s')
    ArrT=Label(frame_buttons, text="Arrivée" ,font=("courier", 8), fg='black', bg='white',width=17)
    ArrT.grid(row=lignemin-1, column=col+1,sticky='s')
    DureeT=Label(frame_buttons, text="Durée" ,font=("courier", 8), fg='black', bg='white',width=17)
    DureeT.grid(row=lignemin-1, column=col+2,sticky='s')
    if mode == "Tout":
        PrioT=Label(frame_buttons, text="Priorité initiale" ,font=("courier", 8), fg='black', bg='white',width=17)
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

##    # Update buttons frames idle tasks to let tkinter calculate buttons sizes       
##    frame_buttons.update_idletasks()
##    # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
##    first4columns_width = sum([ListTabl[j].winfo_width() for j in range(0, 4)])
##    first4rows_height = sum([ListTabl[i].winfo_height() for i in range(0, 10)])

    frame_canvas.config(width=550,height=250)
    # Set the canvas scrolling region
    canvas.config(scrollregion=canvas.bbox("all"))

B=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='red',command=lambda:Tableau(NbProc))
B.grid(row=4, column=4)
C=Button(fenetre, text="CLICK!", font=("courier", 18, "italic",'bold'), fg='white', bg='green',command=lambda:get())
C.grid(row=4, column=3)

def recup():
    li=[]
    for i in range(len(ListTabl)):
        a=ListTabl[i].get()
        li.append(a)
    return(li)

def listintodico(liste):
    li=[]
    i=0
    cpt=0
    while i<len(liste):
        if i+3>len(liste):
            break
        li.append(str({"n": liste[cpt], "da": liste[i], "d": liste[i+1], "prio": liste[i+2]}))
        cpt+=1
        i=i+3
    return(li)

def get():
    liste=recup()
    li=listintodico(liste)
    print(li)

ListTabl[i].configure(state="disabled")
ListTab1[i].insert(0,1)

fenetre.mainloop
