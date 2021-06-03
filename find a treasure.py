#import random
#nom = input("donne moi tous les noms afin que je choississe pour vous ")
#noms =nom.split(",")
# x=len(noms)
#i = random.randint(0,x)
#print(noms[i]+" va tout payer lol  ")
rows1 = ["🧐", "🧐", "🧐"]
rows2 = ["😎", "😎", "😎"]
rows3 = ["🤔", "🤔", "🤔"]
map = [rows1, rows2, rows3]


joueur1 = input("Player 1 what's your name \n\n")
joueur2 = input("Player 2 what's your name \n\n")

print(f"{rows1}\n{rows2}\n{rows3}")

print(f" ===== {joueur1} Hide your treasure ===  \n ")
ligne = (int(input("inform the colone where you want to hide your treasure "))) % 4
colonne = (
    int(input("fill in the line where you want to hide your treasure "))) % 4
map[colonne-1][ligne-1] = "X"

compteur = 0


print(f"=== {joueur2} you have 3 chances to find the treasure of {joueur1} === ")
while(compteur < 3):
    ligne1 = (
        int(input("inform the colone where you want to look for the treasure "))) % 4
    colon1 = (
        int(input("fill in the line where you want to look for the treasure "))) % 4

    if (ligne == ligne1 and colonne == colon1):
        print(f" Good game!!!\n\n {rows1}\n{rows2}\n{rows3}")
        import sys
        sys.exit()
    else:
        print(f"{joueur2} try again! ")
        compteur = compteur+1
print(f"Pity {joueur1} hid his treasure well")
