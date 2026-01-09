mot=str(input("Mot ? "))
repetition=int(input("Nombre de répétition ? "))
print("Voici",repetition,"repetitions : ",end=" ")
for _ in range(repetition):
    print(mot,end=" ")
    