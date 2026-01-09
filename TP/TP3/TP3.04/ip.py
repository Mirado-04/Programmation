adresse=str(input("Adresse IP ?"))
l=adresse.split(".")
if l[0].isdigit() and 0<=int(l[0])<=127:
    print(" L'adresse",adresse,"est de classe A")
elif l[0].isdigit() and 128<=int(l[0])<=191:
    print(" L'adresse",adresse,"est de classe B")
elif l[0].isdigit() and 192<=int(l[0])<=223:
    print(" L'adresse",adresse,"est de classe C")
elif l[0].isdigit() and 224<=int(l[0])<=239:
    print(" L'adresse",adresse,"est de classe D")
else:
    print("L'adresse",adresse,"es de classe E")
