print("===love calculator===")
nom1 = input("What is your name ")
nom2 = input("What's his name ")
nom = nom1+nom2
Chiffre1 = nom.count("t") + nom.count("r") + nom.count("u")+nom.count("e")
Chiffre2 = nom.count("l") + nom.count("o")+nom.count("v")+nom.count("e")
Pourcentage = str(Chiffre1)+str(Chiffre2)
if int(Pourcentage) > 90 or int(Pourcentage) < 10:
    print(f" your degree of love is {Pourcentage},it's not the right one")
elif int(Pourcentage) > 40 and int(Pourcentage) < 50:
    print(f"your degree of love is {Pourcentage},it's the good one")
else:
    print(f"your degree of love is {Pourcentage},it may be the right one")
