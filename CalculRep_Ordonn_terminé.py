lp=[{"n": 1, "da": 0, "d": 6, "prio": 1},
    {"n": 2, "da": 0, "d": 7, "prio": 2},
    {"n": 3, "da": 1, "d": 3, "prio": 1},
    {"n": 4, "da": 1, "d": 4, "prio": 3},
    {"n": 5, "da": 2, "d": 1, "prio": 2},
    {"n": 6, "da": 11, "d": 2, "prio": 1},
    {"n": 7, "da": 16, "d": 3, "prio": 2},
    {"n": 8, "da": 21, "d": 2, "prio": 1},
    {"n": 9, "da": 24, "d": 1, "prio": 3},
    {"n": 10, "da": 25, "d": 4, "prio": 1}]

Li=["Tourniquet","FIFO","PCTER","Priorite fixes","Algorithmes multi files FIFO sans migration","Algorithmes multi files FIFO avec migration","Algorithmes multi files TOURNIQUET sans migration","Algorithmes multi files TOURNIQUET avec  migration"]

#====================================================
#FIFO
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










