nbr=0
attempt=0
while nbr!=70:
    nbr=int(input("Saissiez un nombre : "))
    attempt+=1
    if nbr<70:
        print(nbr," est trop petit")
    elif nbr>70:
        print(nbr,"est trop grand")
print("Bien joué, vous avez fait",attempt,"tentative(s)")