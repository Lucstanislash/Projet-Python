
def decimal(floateur,FMantisse):
    #transforme la partie décimal d'un float en binaire avec pour longueur FMantisse
    ch_dec=""
    dec=str(floateur).replace(str(int(floateur)),'0')
    float(dec)
    for i in range(FMantisse+1):
        dec=float(dec)*2
        if int(dec) >= 1:
            dec-=1
            ch_dec+='1'
        else:
            ch_dec+='0'
    return(ch_dec)
            
        
        
    
