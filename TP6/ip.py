from random import randint
def adresses_ip(classe:str="A") -> str:
    """
    Retourne une adresse ipv4 aléatoirement de classe 
    """
    if classe=="A":
        
def classe(adresse:str) -> str:
    """
    Retourne la classe de l'adresse ipv4 adresse
    """
    adr=adresse.split(".")
    if adr[0].isdigit() and 0<=int(adr[0])<=127:
        return "Classe A"
    elif adr[0].isdigit() and 128<=int(adr[0])<=191:
        return "Classe B"
    elif adr[0].isdigit() and 192<=int(adr[0])<=223:
        return "Classe C"
    elif adr[0].isdigit() and 224<=int(adr[0])<=239:
        return "Classe D"
    else:
        return "Classe E"
    

if __name__ == "__main__":
    adr = adresses_ip("A")
    print(f"{adr} est de classe {classe(adr)}")