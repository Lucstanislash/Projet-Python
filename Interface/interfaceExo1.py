from tkinter import *
import tkinter as tk
from tkinter import ttk
from Outils import*
import random
from tkinter import messagebox

#======================================================================================== Saisie Manuel
def SaisiEx1():
    base=[10,2,8,16]
    for i in base:
        basedep=base[i]
        basearr=base[i]
        entier=""
        if basedep!=basearr:
            if base[i]==8:
                ok=CtrlSyntaxe(entier,8,1,10)
            elif base[i]==16:
                ok=CtrlSyntaxe(entier,16,1,8)
            elif base[i]==2:
                ok=CtrlSyntaxe(entier,2,1,32)
            elif base[i]==10:
                ok=CtrlSyntaxe(entier,10,1,10,1,10000)
    return(basedep,entier,basearr) 
#========================================================================================       
fen=tk.Tk()
fen.config(background="lightskyblue1")

fen.rowconfigure(1, weight=0)
fen.rowconfigure(2, weight=0)
fen.rowconfigure(3, weight=1)
fen.rowconfigure(4, weight=1)
fen.rowconfigure(5, weight=1)
fen.rowconfigure(6, weight=1)
fen.rowconfigure(7, weight=1)
fen.rowconfigure(8, weight=1)
fen.rowconfigure(9, weight=1)

fen.columnconfigure(0, weight=1)
fen.columnconfigure(1, weight=1)
fen.columnconfigure(2, weight=1)
fen.columnconfigure(3, weight=1)
fen.columnconfigure(4, weight=1)
fen.columnconfigure(5, weight=1)
fen.columnconfigure(6, weight=1)

#======================= Rappel =================================
#https://apcpedagogie.com/rappels-sur-les-nombres-binaires/
#https://www.iro.umontreal.ca/~monnier/1215/notes-numberbases.pdf
#https://electrotoile.eu/conversion_numeration.php#:~:text=Pour%20r%C3%A9aliser%20cette%20conversion%20il,%3A%201001%200101(2).

#======================Aléatoire=================================
man=1
entier=0
basedep=0
basearr=0
def alea(man):
    global basedep
    global basearr
    global entier
    if man ==1:
        base=(2,8,10,16)
        basedep=randint(0,3)
        basearr=randint(0,3)
        while basedep==basearr:
            basedep=randint(0,3)
            basearr=randint(0,3)
        basedep=base[basedep]
        basearr=base[basearr]
        dicoNb={}
        dicoNb[2]='disabled','normal','disabled','disabled','Gainsboro','salmon','Gainsboro','Gainsboro'
        dicoNb[8]='disabled','disabled','disabled','normal','Gainsboro','Gainsboro','Gainsboro','salmon'
        dicoNb[10]='normal','disabled','disabled','disabled','salmon','Gainsboro','Gainsboro','Gainsboro'
        dicoNb[16]='disabled','disabled','normal','disabled','Gainsboro','Gainsboro','salmon','Gainsboro'
        A1=Radiobutton(fen,text="Décimal",selectcolor=dicoNb[basedep][4],state=dicoNb[basedep][0], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
        A2=Radiobutton(fen,text="Binaire",selectcolor=dicoNb[basedep][5],state=dicoNb[basedep][1], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
        A3=Radiobutton(fen,text="Hexadécimal",selectcolor=dicoNb[basedep][6],state=dicoNb[basedep][2], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
        A4=Radiobutton(fen,text="Octal",selectcolor=dicoNb[basedep][7],state=dicoNb[basedep][3], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
        
        A1['state']='normal'
        A5=Radiobutton(fen,text="Décimal",selectcolor=dicoNb[basearr][4],state=dicoNb[basearr][0], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
        A6=Radiobutton(fen,text="Binaire",selectcolor=dicoNb[basearr][5],state=dicoNb[basearr][1], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
        A7=Radiobutton(fen,text="Hexadécimal",selectcolor=dicoNb[basearr][6],state=dicoNb[basearr][2], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')
        A8=Radiobutton(fen,text="Octal",selectcolor=dicoNb[basearr][7],state=dicoNb[basearr][3], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2')

        A1.grid(row = 5, column = 2, rowspan=2, pady=5)
        A2.grid(row = 6, column = 2, pady=5)
        A3.grid(row = 6, column = 2, rowspan=2, pady=5)
        A4.grid(row = 7, column = 2, pady=5)

        A5.grid(row = 5, column = 4, rowspan=2, pady=5)
        A6.grid(row = 6, column = 4, pady=5)
        A7.grid(row = 6, column = 4, rowspan=2, pady=5)
        A8.grid(row = 7, column = 4, pady=5)

        if basedep==2:
            entier=AleaExAll(2,1,32)
        if basedep==8:
            entier=AleaExAll(8,1,10)
        if basedep==10:
            entier=AleaExAll(10,1,5)
        if basedep==16:
            entier=AleaExAll(16,1,8)
        Esaisie=Label(fen, text=entier , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
        Esaisie.grid(row=3, column=2,columnspan=3, rowspan=2, ipadx=200,ipady=10)

alea(man)
def RepEx1(donne):
    dico={}
    dico[2]='b'
    dico[8]='o'
    dico[16]='x'
    if donne[0] == 10:
        print(dico[donne[1]])
        rep=format(int(donne[2]),dico[donne[1]])
        rep=rep.upper()
    elif donne[1] == 10:
        rep=str(int(donne[2],donne[0]))
        print(donne[1])
    else:
        rep=int(donne[2],donne[0])
        rep=format(rep,dico[donne[1]])
        rep=rep.upper()
    return(rep)

#==================================Manuel===================    
def get(basedep,basearr,entier,man):
    util = Résultats.get()
    util=util.upper()
    if man==2:
        entier = Esaisie.get()
        basedep=basedepart.get()
        basearr=basearrivee.get()
        print(entier)
        print(basedep)
        print(basearr)
    if entier=='' or basearr==0 or basedep == 0:
        messagebox.showerror(title="Information",
                    message="Erreur : Veuillez saisir toutes les valeurs")
        return 1
    Lmax={}
    Lmax[10]=5
    Lmax[2]=32
    Lmax[8]=10
    Lmax[16]=8
    entier=str(entier).upper()
    donnee=(basedep,basearr,entier)
    ok=CtrlSyntaxe(entier,basedep,1,Lmax[basedep])
    ok2=CtrlSyntaxe(util,basearr,1,Lmax[basearr])
    if ok==True and ok2==True:
        if basedep!=basearr:
            rep=RepEx1(donnee)
        else:
            messagebox.showerror(title="Information",
                            message="Erreur : Problème dans la sélection des bases.")
            return(1)
    else:
        #except (NameError, ValueError, SyntaxError, TypeError):                        #Permet d'exclure une/plusieurs erreur(s) et d'effectuer alors des instructions    
        messagebox.showerror(title="Information",
                                message='Erreur : Vous avez fait une erreur de syntaxe')
        return(1)
    
    Verif=VerifRep(rep,util)
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
       
#===========================INTERFACE===============================

titre=Label(fen, text="Entiers non signées", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
titre.grid(row=1, column=2,columnspan=3)
soustitre=Label(fen, text="Quelques Indications: ", font=("courier", 25), fg='red', bg='lightskyblue1') 
soustitre.grid(row=2, column=1,columnspan=3,sticky='w') 

#Création de menu déroulant d'entrée
lab1=Label(fen,text="Valeur à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
lab1.grid(row=2, column=2,columnspan=3, rowspan=2)   #Créé du texte Label(text=''), spécifie la fenêtre concernée, donne une couleur de fond (bg='') et le place dans la fenêtre avec .pack()
if man==2:
    global Esaisie                                  #Définit une variable utilisable dans tout le programme
    Esaisie=Entry(fen)                              #Créé une entrée que l'utilisateur pourra remplir de texte et spécifie la fenêtre concernée
    Esaisie.grid(row=3, column=2,columnspan=3, rowspan=2, ipadx=200,ipady=10)                        #.pack() permet de placer le widget dans la fenêtre ou la Frame sélectionnée
    Esaisie.focus()                                 #focus() permet ici de placer directement le curseur à l'intérieur de la zone de texte
    #Esaisie.insert(INSERT, 'Mettez la valeur à convertir en respectant les contraintes')      #Insert dans la saisie le texte entre guillemets
    Esaisie.selection_range(0, END)                 #Sélectionne le contenu entier de la saisie


    basedepart=IntVar()
    basearrivee=IntVar()#Définit une variable utilisée pour les Radiobuttons
    #Radiobutton créé un bouton qui permet un choix. Il prend comme paramètres un texte, une couleur de fond, une variable et sa valeur. En plus indicatoron change son aspect, width sa largeur, cursor le curseur et activebackground sa couleur quand "cliqué"

    Radiobutton(fen,text="Décimal", fg='#103985', bg='Gainsboro',variable=basedepart,value=10,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 5, column = 2, rowspan=2, pady=5)
    Radiobutton(fen,text="Binaire", fg='#103985', bg='Gainsboro',variable=basedepart,value=2,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 2, pady=5)
    Radiobutton(fen,text="Hexadécimal", fg='#103985', bg='Gainsboro',variable=basedepart,value=16,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 2, rowspan=2, pady=5)
    Radiobutton(fen,text="Octal", fg='#103985', bg='Gainsboro',variable=basedepart,value=8,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 7, column = 2, pady=5)

    Radiobutton(fen,text="Décimal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=10,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 5, column = 4, rowspan=2, pady=5)
    Radiobutton(fen,text="Binaire", fg='#103985', bg='Gainsboro',variable=basearrivee,value=2,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 4, pady=5)
    Radiobutton(fen,text="Hexadécimal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=16,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 4, rowspan=2, pady=5)
    Radiobutton(fen,text="Octal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=8,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 7, column = 4, pady=5)
 



lab2=Label(fen,text="Base de départ", font=("courier", 17), fg='black', bg='lightskyblue1')
lab2.grid(row=5, column=2)

lab3=Label(fen,text="Base d'arrivée", font=("courier", 17), fg='black', bg='lightskyblue1')
lab3.grid(row = 5, column =4)

lab4=Label(fen,text="Résultats", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
lab4.grid(row = 7, column = 2, pady=3, columnspan=3, rowspan=2)
Résultats=Entry(fen) # Création de la zone de résultats
Résultats.grid(row = 8, column = 2, columnspan=3, ipadx=200, ipady=10)
Résultats.selection_range(0, END)
#====================================
def nouveau(man):
    B2['state']='disabled'
    B3['state']='normal'
    if man==2:
        Esaisie.delete(0,END)
    Résultats.delete(0,END)
    alea(man)
    
    
img1=PhotoImage(file="img1.gif")
imag=PhotoImage(file="imag.gif")

def create():
    rappel = Toplevel(fen, background="white")
    #rappel.config(background="lightskyblue1")
    Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='white').grid(row=1, column=1, columnspan=3)

    Label(rappel, text="Dans un système en base X, il faut X symboles différents pour représenter les chiffres de 0 à X-1", font=("Courier", 14), fg='blue4', bg='white').grid(row=2, column=1,columnspan=3)
    Label(rappel, image= img1).grid(row=3, column=1,columnspan=3)
##    
    i="╠═══════{Conversion du nombre N exprimé en base 10 vers une base X}═══════╣\n"
    a="Diviser le nombre N par la base X jusqu’à obtenir un quotient égal à 0. La conversion est donc\n"
    b="obtenue en notant les restes de chacune des divisions effectuées depuis la dernière division."
    Label(rappel, text=i, bg='white', fg='darkslateblue', font=('Courier',14)).grid(row=4, column=1)                   
    Label(rappel, text=a+b, bg='white', fg='firebrick3', font=('Segoe Print',10)).grid(row=5, column=1)
    #Label(rappel, image= img2).grid(row=4, column=2, columnspan=2) 
##    
    j="╠═══════{Conversion du nombre N exprimé en base X vers la base 10}═══════╣\n"
    c="Multiplier chaque digit par la base Xn, puis Additionner.\n"
    d="100111 = 1x2^5 + 0x2^4 + 0x2^3 + 1x2^2 + 1x2^1 + 1x2^0\n"
    e="100111 =  32   +   0   +   0   +   4   +   2   +   1 = 39\n"                      
                        
    Label(rappel, text=j, bg='white', fg='darkslateblue', font=('Courier',14)).grid(row=6, column=1)                  
    Label(rappel, text=c+d+e, bg='white', fg='firebrick3', font=('Segoe Print',10)).grid(row=7, column=1)
    
##    
    k="╠═══════{Conversion du nombre N exprimé dans la base 8 vers la base 2}═══════╣\n"
    m=" - Convertir un nombre N en base 8 vers la base 2 s’effectue en remplaçant chacun des chiffres du nombre par leur équivalent binaire sur 3 bits.\n"
    n="- Convertir un nombre N en base 2 vers base 8 s’effectue en découpant la chaîne binaire N en paquet de 3 bits depuis le bit de poids faible.\n"

    Label(rappel, text=k, bg='white', fg='darkslateblue', font=('Courier',14)).grid(row=8, column=1)               
    Label(rappel, text=m+n, bg='white', fg='firebrick3', font=('Segoe Print',10)).grid(row=9, column=1)
    #Label(rappel, image= img4).grid(row=7, column=2) 
##
    l="╠═══════{Conversion du nombre N exprimé dans la base 16 vers la base 2}═══════╣\n"
    o=" - Convertir un nombre N en base 16 vers la base 2 s’effectue en remplaçant chacun des chiffres du nombre par leur équivalent binaire sur 4 bits. \n"
    p="– Convertir un nombre N en base 2 vers la base 16 s’effectue en découpant la chaîne binaire N en paquet de 4 bits depuis le bit de poids faible.\n"

    Label(rappel, text=l, bg='white', fg='darkslateblue', font=('Courier',14)).grid(row=10, column=1)               
    Label(rappel, text=o+p, bg='white', fg='firebrick3', font=('Segoe Print',10)).grid(row=11, column=1)
    Label(rappel, image= imag).grid(row=4, column=2, rowspan=8) 

    def exit_btn():

        rappel.destroy()
        rappel.update()

    btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
    btn.grid(row=12, column=1,columnspan=3,sticky='n')
    
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

B1=Button(fen, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2, command=create)
B1.grid(row=9, column=1)
B2=Button(fen, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, command=lambda:(nouveau(man)))
B2.grid(row=9, column=2)
B3=Button(fen, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, command=lambda:(get(basedep,basearr,entier,man)))
B3.grid(row=9, column=3)
B4=Button(fen, text="Score", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
B4.grid(row=9, column=4)
B5=Button(fen, text="Quitter", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2,command=fen.destroy)
B5.grid(row=9, column=5)

fen.mainloop()
##from tkinter import *
##import tkinter as tk
##from tkinter import ttk
##from Outils import*
##import random
##from tkinter import messagebox
##
###======================================================================================== Saisie Manuel
##def SaisiEx1():
##    base=[10,2,8,16]
##    for i in base:
##        basedep=base[i]
##        basearr=base[i]
##        entier=""
##        if basedep!=basearr:
##            if base[i]==8:
##                ok=CtrlSyntaxe(entier,8,1,10)
##            elif base[i]==16:
##                ok=CtrlSyntaxe(entier,16,1,8)
##            elif base[i]==2:
##                ok=CtrlSyntaxe(entier,2,1,32)
##            elif base[i]==10:
##                ok=CtrlSyntaxe(entier,10,1,10,1,10000)
##    return(basedep,entier,basearr)
###========================================================================================
##        
##fen=tk.Tk()
##fen.config(background="lightskyblue1")
##
##
##fen.rowconfigure(1, weight=0)
##fen.rowconfigure(2, weight=0)
##fen.rowconfigure(3, weight=1)
##fen.rowconfigure(4, weight=1)
##fen.rowconfigure(5, weight=1)
##fen.rowconfigure(6, weight=1)
##fen.rowconfigure(7, weight=1)
##fen.rowconfigure(8, weight=1)
##fen.rowconfigure(9, weight=1)
##
##fen.columnconfigure(0, weight=1)
##fen.columnconfigure(1, weight=1)
##fen.columnconfigure(2, weight=1)
##fen.columnconfigure(3, weight=1)
##fen.columnconfigure(4, weight=1)
##fen.columnconfigure(5, weight=1)
##fen.columnconfigure(6, weight=1)
##
###======================= Rappel =================================
###https://apcpedagogie.com/rappels-sur-les-nombres-binaires/
###https://www.iro.umontreal.ca/~monnier/1215/notes-numberbases.pdf
###https://electrotoile.eu/conversion_numeration.php#:~:text=Pour%20r%C3%A9aliser%20cette%20conversion%20il,%3A%201001%200101(2).
##
###======================Aléatoire=================================
##man=1 #===================================1Aléatoire=1 / Manuel=2
##if man==1:
##    base=(2,8,10,16)
##    basedep=randint(0,3)
##    basearr=randint(0,3)
##    while basedep==basearr:
##        basedep=randint(0,3)
##        basearr=randint(0,3)
##    basedep=base[basedep]
##    basearr=base[basearr]
##    dicoNb={}
##    dicoNb[2]='disabled','normal','disabled','disabled','Gainsboro','salmon','Gainsboro','Gainsboro'
##    dicoNb[8]='disabled','disabled','disabled','normal','Gainsboro','Gainsboro','Gainsboro','salmon'
##    dicoNb[10]='normal','disabled','disabled','disabled','salmon','Gainsboro','Gainsboro','Gainsboro'
##    dicoNb[16]='disabled','disabled','normal','disabled','Gainsboro','Gainsboro','salmon','Gainsboro'
##    Radiobutton(fen,text="Décimal",selectcolor=dicoNb[basedep][4],state=dicoNb[basedep][0], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 5, column = 2, rowspan=2, pady=5)
##    Radiobutton(fen,text="Binaire",selectcolor=dicoNb[basedep][5],state=dicoNb[basedep][1], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 2, pady=5)
##    Radiobutton(fen,text="Hexadécimal",selectcolor=dicoNb[basedep][6],state=dicoNb[basedep][2], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 2, rowspan=2, pady=5)
##    Radiobutton(fen,text="Octal",selectcolor=dicoNb[basedep][7],state=dicoNb[basedep][3], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 7, column = 2, pady=5)
##
##    Radiobutton(fen,text="Décimal",selectcolor=dicoNb[basearr][4],state=dicoNb[basearr][0], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 5, column = 4, rowspan=2, pady=5)
##    Radiobutton(fen,text="Binaire",selectcolor=dicoNb[basearr][5],state=dicoNb[basearr][1], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 4, pady=5)
##    Radiobutton(fen,text="Hexadécimal",selectcolor=dicoNb[basearr][6],state=dicoNb[basearr][2], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 4, rowspan=2, pady=5)
##    Radiobutton(fen,text="Octal",selectcolor=dicoNb[basearr][7],state=dicoNb[basearr][3], fg='#103985', bg='Gainsboro',indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 7, column = 4, pady=5)
##    if basedep==2:
##        entier=AleaExAll(2,1,32)
##    if basedep==8:
##        entier=AleaExAll(8,1,10)
##    if basedep==10:
##        entier=AleaExAll(10,1,5)
##    if basedep==16:
##        entier=AleaExAll(16,1,8)
##
##def RepEx1(donne):
##    dico={}
##    dico[2]='b'
##    dico[8]='o'
##    dico[16]='x'
##    if donne[0] == 10:
##        print(dico[donne[1]])
##        rep=format(int(donne[2]),dico[donne[1]])
##        rep=rep.upper()
##    elif donne[1] == 10:
##        rep=str(int(donne[2],donne[0]))
##        print(donne[1])
##    else:
##        rep=int(donne[2],donne[0])
##        rep=format(rep,dico[donne[1]])
##        rep=rep.upper()
##    return(rep)
##
###==================================Manuel===================    
##def get():
##    util = Résultats.get()
##    util=util.upper()
##    if man==2:
##        entier = Esaisie.get()
##        basedep=basedepart.get()
##        basearr=basearrivee.get()
##        print(util)
##        Lmax={}
##        Lmax[10]=5
##        Lmax[2]=32
##        Lmax[8]=10
##        Lmax[16]=8
##        entier=entier.upper()
##        donnee=(basedep,basearr,entier)
##        ok=CtrlSyntaxe(entier,basedep,1,Lmax[basedep])
##        ok2=CtrlSyntaxe(util,basearr,1,Lmax[basearr])
##        if ok==True and ok2==True:
##            #try:                                    #try permet de faire des exceptions en fonction de ce qui suit
##            print (ok)
##            print(ok2)
##            if basedep!=basearr:
##                rep=RepEx1(donnee)
##                print(rep)
##            else:
##                messagebox.showerror(title="Information",
##                            message="Erreur : Problème dans la sélection des bases.")
##                return(1)
##        else :
##            print(ok)
##            print(ok2)
##            #except (NameError, ValueError, SyntaxError, TypeError):                        #Permet d'exclure une/plusieurs erreur(s) et d'effectuer alors des instructions    
##            messagebox.showerror(title="Information",
##                                message='Erreur : Vous avez fait une erreur de syntaxe')
##            return(1)
##    
##        Verif=VerifRep(rep,util)
##        if Verif == 1:
##            B3['state']='disabled' #bloquer le bouton valider ==> Gagner
##            messagebox.showinfo(title="Information",
##                                message="Bonne Réponse, Bravo !! ")
##            B2['state']='normal'
##        elif Verif == -1:
##            B3['state']='disabled' #bloquer le bouton valider ==> Perdu
##            B2['state']='normal'  #débloquer le bouton nouveau ==> recommencer
##            messagebox.showinfo(title="Information",
##                                message=" Mauvaise réponse, vous avez perdu !\n \n ╠═══════════{Le Résultat est}═══════════╣ \n" +("".join(str(rep))))
##        elif Verif == 0:
##           messagebox.showinfo(title="Information",
##                                message="Mauvaise réponse, réessayer !")
##       
###===========================INTERFACE===============================
##
##titre=Label(fen, text="Entiers non signées", font=("Courier", 40, "italic"), fg='blue4', bg='lightskyblue1') # 
##titre.grid(row=1, column=2,columnspan=3)
##soustitre=Label(fen, text="Quelques Indications: ", font=("courier", 25), fg='red', bg='lightskyblue1') 
##soustitre.grid(row=2, column=1,columnspan=3,sticky='w') 
##
##
###Création de menu déroulant d'entrée
##lab1=Label(fen,text="Valeur à convertir", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
##lab1.grid(row=2, column=2,columnspan=3, rowspan=2)   #Créé du texte Label(text=''), spécifie la fenêtre concernée, donne une couleur de fond (bg='') et le place dans la fenêtre avec .pack()
##if man==2:
##    global Esaisie                                  #Définit une variable utilisable dans tout le programme
##    Esaisie=Entry(fen)                              #Créé une entrée que l'utilisateur pourra remplir de texte et spécifie la fenêtre concernée
##    Esaisie.grid(row=3, column=2,columnspan=3, rowspan=2, ipadx=200,ipady=10)                        #.pack() permet de placer le widget dans la fenêtre ou la Frame sélectionnée
##    Esaisie.focus()                                 #focus() permet ici de placer directement le curseur à l'intérieur de la zone de texte
##    #Esaisie.insert(INSERT, 'Mettez la valeur à convertir en respectant les contraintes')      #Insert dans la saisie le texte entre guillemets
##    Esaisie.selection_range(0, END)                 #Sélectionne le contenu entier de la saisie
##
##
##    basedepart=IntVar()
##    basearrivee=IntVar()#Définit une variable utilisée pour les Radiobuttons
##    #Radiobutton créé un bouton qui permet un choix. Il prend comme paramètres un texte, une couleur de fond, une variable et sa valeur. En plus indicatoron change son aspect, width sa largeur, cursor le curseur et activebackground sa couleur quand "cliqué"
##
##    Radiobutton(fen,text="Décimal", fg='#103985', bg='Gainsboro',variable=basedepart,value=10,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 5, column = 2, rowspan=2, pady=5)
##    Radiobutton(fen,text="Binaire", fg='#103985', bg='Gainsboro',variable=basedepart,value=2,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 2, pady=5)
##    Radiobutton(fen,text="Hexadécimal", fg='#103985', bg='Gainsboro',variable=basedepart,value=16,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 2, rowspan=2, pady=5)
##    Radiobutton(fen,text="Octal", fg='#103985', bg='Gainsboro',variable=basedepart,value=8,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 7, column = 2, pady=5)
##
##    Radiobutton(fen,text="Décimal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=10,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 5, column = 4, rowspan=2, pady=5)
##    Radiobutton(fen,text="Binaire", fg='#103985', bg='Gainsboro',variable=basearrivee,value=2,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 4, pady=5)
##    Radiobutton(fen,text="Hexadécimal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=16,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 6, column = 4, rowspan=2, pady=5)
##    Radiobutton(fen,text="Octal", fg='#103985', bg='Gainsboro',variable=basearrivee,value=8,indicatoron=0,width=26, height=2, cursor='hand2').grid(row = 7, column = 4, pady=5)
##
##else:
##    Esaisie=Label(fen, text=entier , font=("courier", 14, "italic"), fg='black', bg='white',borderwidth=3, relief="sunken",width=10)
##    Esaisie.grid(row=3, column=2,columnspan=3, rowspan=2, ipadx=200,ipady=10)
##
##lab2=Label(fen,text="Base de départ", font=("courier", 17), fg='black', bg='lightskyblue1')
##lab2.grid(row=5, column=2)
##
##lab3=Label(fen,text="Base d'arrivée", font=("courier", 17), fg='black', bg='lightskyblue1')
##lab3.grid(row = 5, column =4)
##
##lab4=Label(fen,text="Résultats", font=("courier", 25, "italic"), fg='black', bg='lightskyblue1')
##lab4.grid(row = 7, column = 2, pady=3, columnspan=3, rowspan=2)
##Résultats=Entry(fen) # Création de la zone de résultats
##Résultats.grid(row = 8, column = 2, columnspan=3, ipadx=200, ipady=10)
##Résultats.selection_range(0, END)
###==================================
##def nouveau():
##    if (B3['state']=='normal'):
##        B2['state']='disabled'
##    else:
##        B2['state']='normal'
##
##
##img1=PhotoImage(file="img1.gif")
##imag=PhotoImage(file="imag.gif")
##
##def create():
##    rappel = Toplevel(fen, background="white")
##    #rappel.config(background="lightskyblue1")
##    Label(rappel,text="Rappel", font=("Courier", 40, "italic"), fg='blue4', bg='white').grid(row=1, column=1, columnspan=3)
##
##    Label(rappel, text="Dans un système en base X, il faut X symboles différents pour représenter les chiffres de 0 à X-1", font=("Courier", 14), fg='blue4', bg='white').grid(row=2, column=1,columnspan=3)
##    Label(rappel, image= img1).grid(row=3, column=1,columnspan=3)
####    
##    i="╠═══════{Conversion du nombre N exprimé en base 10 vers une base X}═══════╣\n"
##    a="Diviser le nombre N par la base X jusqu’à obtenir un quotient égal à 0. La conversion est donc\n"
##    b="obtenue en notant les restes de chacune des divisions effectuées depuis la dernière division."
##    Label(rappel, text=i, bg='white', fg='darkslateblue', font=('Courier',14)).grid(row=4, column=1)                   
##    Label(rappel, text=a+b, bg='white', fg='firebrick3', font=('Segoe Print',10)).grid(row=5, column=1)
##    #Label(rappel, image= img2).grid(row=4, column=2, columnspan=2) 
####    
##    j="╠═══════{Conversion du nombre N exprimé en base X vers la base 10}═══════╣\n"
##    c="Multiplier chaque digit par la base Xn, puis Additionner.\n"
##    d="100111 = 1x2^5 + 0x2^4 + 0x2^3 + 1x2^2 + 1x2^1 + 1x2^0\n"
##    e="100111 =  32   +   0   +   0   +   4   +   2   +   1 = 39\n"                      
##                        
##    Label(rappel, text=j, bg='white', fg='darkslateblue', font=('Courier',14)).grid(row=6, column=1)                  
##    Label(rappel, text=c+d+e, bg='white', fg='firebrick3', font=('Segoe Print',10)).grid(row=7, column=1)
##    
####    
##    k="╠═══════{Conversion du nombre N exprimé dans la base 8 vers la base 2}═══════╣\n"
##    m="- Convertir un nombre N en base 8 vers la base 2 s’effectue en remplaçant chacun des chiffres du nombre par leur équivalent binaire sur 3 bits.\n"
##    n="- Convertir un nombre N en base 2 vers base 8 s’effectue en découpant la chaîne binaire N en paquet de 3 bits depuis le bit de poids faible.\n"
##
##    Label(rappel, text=k, bg='white', fg='darkslateblue', font=('Courier',14)).grid(row=8, column=1)               
##    Label(rappel, text=m+n, bg='white', fg='firebrick3', font=('Segoe Print',10)).grid(row=9, column=1)
##    #Label(rappel, image= img4).grid(row=7, column=2) 
####
##    l="╠═══════{Conversion du nombre N exprimé dans la base 16 vers la base 2}═══════╣\n"
##    o="- Convertir un nombre N en base 16 vers la base 2 s’effectue en remplaçant chacun des chiffres du nombre par leur équivalent binaire sur 4 bits. \n"
##    p="– Convertir un nombre N en base 2 vers la base 16 s’effectue en découpant la chaîne binaire N en paquet de 4 bits depuis le bit de poids faible.\n"
##
##    Label(rappel, text=l, bg='white', fg='darkslateblue', font=('Courier',14)).grid(row=10, column=1)               
##    Label(rappel, text=o+p, bg='white', fg='firebrick3', font=('Segoe Print',10)).grid(row=11, column=1)
##    Label(rappel, image= imag).grid(row=4, column=2, rowspan=8) 
##
##    def exit_btn():
##
##        rappel.destroy()
##        rappel.update()
##
##    btn = Button(rappel,text='Quitter',command=exit_btn,font=("calibri", 18, "bold"), fg='white', bg='#103985', width=15, height=2)
##    btn.grid(row=12, column=1,columnspan=3,sticky='n')
##    
##    rappel.rowconfigure(1, weight=1)
##    rappel.rowconfigure(2, weight=1)
##    rappel.rowconfigure(3, weight=1)
##    rappel.rowconfigure(4, weight=1)
##    rappel.rowconfigure(5, weight=1)
##    rappel.rowconfigure(6, weight=1)
##    rappel.rowconfigure(7, weight=1)
##    rappel.rowconfigure(8, weight=1)
##    rappel.rowconfigure(9, weight=1)
##    rappel.rowconfigure(10, weight=1)
##    rappel.rowconfigure(11, weight=1)
##    rappel.rowconfigure(12, weight=1)
##
##    rappel.columnconfigure(1, weight=0)
##    rappel.columnconfigure(2, weight=1)
##    rappel.columnconfigure(3, weight=0)
##
##  
##
##B1=Button(fen, text="Rappel", font=("calibri", 18, "bold", 'underline'), fg='white', bg='#103985', width=15, height=2, command=create)
##B1.grid(row=9, column=1)
##B2=Button(fen, text="Nouveau", state='disabled', font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2)
##B2.grid(row=9, column=2)
##B3=Button(fen, text="Valider", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, command=get)
##B3.grid(row=9, column=3)
##B4=Button(fen, text="Quitter", font=("courier", 18, "italic"), fg='white', bg='#103985', width=15, height=2, command=fen.destroy)
##B4.grid(row=9, column=4)
##B5=Button(fen, text="Menu", font=("calibri", 18, "bold"), fg='white', bg='grey', width=15, height=2)
##B5.grid(row=9, column=5)
##
##fen.mainloop()
##
###https://sites.google.com/site/pythonpasapas/modules/modules-de-la-bibliotheque-standard/tkinter/tkinter-radiobutton

