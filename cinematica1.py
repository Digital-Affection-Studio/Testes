distancia = ['cm', 'm', 'Km']
tempo = ['s', 'min', 'h']
op1 = int(input("Qual unidade de medida você deseja usar para distânçia?\n\n1 - Centímetro(cm)\n2 - Metro(m)\n3 - Quilômetro(Km)\n\n>: "))
op2 = int(input("Qual unidade de medida você deseja usar para tempo?\n\n1 - Segundo(s)\n2 - Minuto(min)\n3 - Hora(h)\n\n>: "))
limite = float(input("\nQual é o limite de velocidade em {}/{}?\n\n>: ".format(distancia[op1-1], tempo[op2-1])))

def limiteTest(limite, velocidade, nCarro):
    if(velocidade>limite):
        return("O carro {} passou dos limites.".format(nCarro))
    elif(velocidade<=limite):
        return("O carro {} está de acordo nos limites.".format(nCarro))

op = int(input("O que você vai descobrir?\n\n1 - Velocidade\n2 - Distância\n3 - Tempo\n\n>: "))
if(op == 1):
    d1 = float(input("Distância percorrida pelo carro 1: "))
    d2 = float(input("Distância percorrida pelo carro 2: "))
    t1 = float(input("Tempo do carro 1: "))
    t2 = float(input("Tempo do carro 2: "))
    v1 = d1/t1
    v2 = d2/t2
    print("Velocidade do carro 1: {} {}/{}".format(v1, distancia[op1-1], tempo[op2-1]))
    print("Velocidade do carro 2: {} {}/{}".format(v2, distancia[op1-1], tempo[op2-1]))
    lim1 = limiteTest(limite, v1, 1)
    lim2 = limiteTest(limite, v2, 2)
    if((v1>limite) and (v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if((v1>limite) and not(v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if(not(v1>limite) and (v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if(not(v1>limite) and not(v2>limite)):
        print("{}\n{}". format(lim1, lim2))
elif(op == 2):
    v1 = float(input("Velocidadedo carro 1: "))
    v2 = float(input("Velocidadedo carro 2: "))
    t1 = float(input("Tempo do carro 1: "))
    t2 = float(input("Tempo do carro 2: "))
    d1 = v1*t1
    d2 = v2*t2
    print("Distância: {} {}".format(d, distancia[op1-1]))
    lim1 = limiteTest(limite, v1)
    lim2 = limiteTest(limite, v2)
    if((v1>limite) and (v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if((v1>limite) and not(v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if(not(v1>limite) and (v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if(not(v1>limite) and not(v2>limite)):
        print("{}\n{}". format(lim1, lim2))

elif(op == 3):
    v1 = float(input("Velocidade do carro 1: "))
    v2 = float(input("Velocidade do carro 2: ")) 
    d1 = float(input("Distância percorrida pelo carro 1: "))
    d2 = float(input("Distância percorrida pelo carro 2: "))
    t1 = d1/v1
    t2 = d2/v2
    print("Tempo: {} {}".format(t, tempo[op2-1]))
    lim1 = limiteTest(limite, v1)
    lim2 = limiteTest(limite, v2)
    if((v1>limite) and (v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if((v1>limite) and not(v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if(not(v1>limite) and (v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    if(not(v1>limite) and not(v2>limite)):
        print("{}\n{}". format(lim1, lim2))
    
