import random
lettre = ['A', 'B', 'C', 'D', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['&', '(', '-', '_', 'à', ')', '=',
          '}', '~', 'é', '#', '{', '|', '^', '@']

print(" -----Welcome jouahibou will find you a very rebellious password------- \n\n")
nbLettre = int(input("how many letters will be your password ? \n"))
nbnumero = int(input("How many number will your password be dialed ? \n "))
nbsymbol = int(input("How many symbol will be your password  ?\n "))
password = []

for char in range(1, nbLettre + 1):
    password += random.choice(lettre)
for char in range(1, nbnumero + 1):
    password += random.choice(numero)
for char in range(1, nbsymbol + 1):
    password += random.choice(symbol)

joua = ""
for i in range(0, len(password)):
    joua = joua + password[i]
random.shuffle(password)
str = ' '.join(password)

print(str)
