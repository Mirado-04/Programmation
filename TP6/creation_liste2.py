from random import randint

def liste_utilisateur(n=5):
    li=[]
    for _ in range(5):
        li.append(int(input("Saississez un entier: ")))
    return li

def liste_aleatoire(n=5, bornemin=0, bornemax=100):
    liste_aleatoire=[randint(bornemin,bornemax) for _ in range(n)]
    return liste_aleatoire


if __name__ == "__main__":
    l1=liste_utilisateur(4)
    print(l1)
    l2=liste_aleatoire(4)
    print(l2)