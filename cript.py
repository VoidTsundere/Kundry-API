def alpha(method, passwrd):
    alp = "acegikmoqsuwy"
    alpr = "ACEGIKMOQSUWY"
    bet = "bdfhjlnprtvxz"
    betr = "BDFHJLNPRTVXZ"
    if "encrypt" in method:
        pastr = []
        for lnumber, letter in enumerate(passwrd):
            if letter in alp:
                pastr.append("-"+str((ord(letter)-96)/2))
                
            elif letter in bet:
                pastr.append("+"+str((ord(letter)-96)*2))
                
            if letter in alpr:
                pastr.append("+"+str((ord(letter)-64)*2))

            if letter in betr:
                pastr.append("-"+str((ord(letter)-64)/2))
                
        return pastr

#print("".join(alpha("encrypt", "AaBbCc")))


reverse = "a1, b2, c3, d4, e5, f6, g7, h8, i9, j10, k11, l12, m13, n14, o15, p16, q17, r18, s19, t20, u21, v22, w23, x24, y25, z26"

def beta(method):
    alp = "acegikmoqsuwy"
    alpr = "ACEGIKMOQSUWY"
    bet = "bdfhjlnprtvxz"
    betr = "BDFHJLNPRTVXZ"
    
    return
