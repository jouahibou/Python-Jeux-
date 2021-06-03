import random
print("_________ Bienvenue dans notre jeux _____________")
nom1 = input("player 1 what's your name  \n ")
nom2 = input("player 2 what's your name  \n ")

Joueur1 = input(f"----- {nom1}  press any key to throw the dice ------ ")
dice1 = random.randint(1, 6)
print(f"{dice1}\n\n")
Joueur2 = input(
    f" -------- Now {nom2} press any key to throw the dice ----- ")

dice2 = random.randint(1, 6)
print(f"{dice2}\n\n")

if dice1 > dice2:
    print(f"{nom1} to win {nom2} xamo dara ")
elif dice1 < dice2:
    print(f"{nom2} to win {nom1} xamo dara ")
else:
    print(" null match ")
