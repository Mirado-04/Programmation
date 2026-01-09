nbr=0
attempt=0
while nbr!=70:
    nbr=int(input("Saissiez un nombre : "))
    attempt+=1
    if nbr<70:
        essai=-1
        print(nbr," est trop petit")
    elif nbr>70:
        print(nbr,"est trop grand")
    if attempt==10:
        print("Bien joué, vous avez fait",attempt,"tentative(s)")
        print("Vous avez atteint le nombre maximum de tentatives, le nombre à trouver est 70")
