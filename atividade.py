copas = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
campeoes = ["Alemanha", "Brasil", "França", "Brasil", "Itália", "Espanha", "Alemanha", "França"]
sedes = ["Itália", "Estados Unidos", "França", "Coreia do Sul", "Alemanha", "África do Sul", "Brasil", "Rússia"]
cont = 0

nA = copas.index(2010)
nB = copas.index(2002)
nC = copas.index(2018)

print("2ª questão.\n")
print("Campeões...\n2010 - {}\n2002 - {}\n2018 - {}".format(campeoes[nA], campeoes[nB], campeoes[nC]))

print("\n3ª questão.\n")
print("Copas ganhas por...\n")
for i, campeao in enumerate(campeoes):
    if campeao == "Espanha":
        print("Espanha - {}".format(copas[i]))
    if campeao == "França":
        print("França - {}".format(copas[i]))
    if campeao == "Alemanha":
        print("Alemanha - {}".format(copas[i]))

nA = sedes.index("Alemanha")
nB = sedes.index("África do Sul")
nC = sedes.index("Brasil")

print("\n4ª questão.\n")
print("A seleção que ganhou nas sedes...\nAlemanha - {}\nÁfrica do Sul - {}\nBrasil - {}".format(campeoes[nA], campeoes[nB], campeoes[nC]))

print("\n5ª questão.\nCampeões e anos...")
while cont < len(campeoes):
    print("{} - {}".format(campeoes[cont], copas[cont]))
    cont = cont + 1

cont = 0
print("\n6ª questão.\nAnos e campeões...")
while cont < len(copas):
    print("{} - {}".format(copas[cont], campeoes[cont]))
    cont = cont + 1

cont = 0
print("\n7ª questão.\n")
while cont < len(copas):
    print("A copa de {}\nFoi realizada em {}\nVencida pela seleção {}\n\n".format(copas[cont], campeoes[cont], sedes[cont]))
    cont = cont + 1


