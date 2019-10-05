print("nossa, que louco")
distancia = ['cm', 'm', 'Km']
tempo = ['s', 'min', 'h']
op1 = int(input("Qual unidade de medida você deseja usar para distânçia?\n\n1 - Centímetro(cm)\n2 - Metro(m)\n3 - Quilômetro(Km)\n\n>: "))
op2 = int(input("Qual unidade de medida você deseja usar para tempo?\n\n1 - Segundo(s)\n2 - Minuto(min)\n3 - Hora(h)\n\n>: "))
op = int(input("O que você vai descobrir?\n\n1 - Velocidade\n2 - Distância\n3 - Tempo\n\n>: "))

if(op == 1):

    
    d1 = float(input("Distância percorrida pelo carro 1: "))
    t1 = float(input("Tempo do carro 1: "))
    v1 = d1/t1
    print("Velocidade do carro 1: {} {}/{}".format(v1, distancia[op1-1], tempo[op2-1]))

    d2 = float(input("Distância percorrida pelo carro 2: "))
    t2 = float(input("Tempo do carro 2: "))
    v2 = d2/t2
    print("Velocidade do carro 2: {} {}/{}".format(v2, distancia[op1-1], tempo[op2-1]))

    limite=float(input("Qual era o limite de velocidade em {}/{}\n\n".format(distancia[op1-1],tempo[op2-1])))
    
    if((v1>limite) and (v2>limite)):
        print("\nMeu Deus, são dois delinquentes.Inadmissível\n\n")
    elif((v1>limite) and (not(v2>limite))):
        print("\nOk, só o carro 1 tem um delinquente no volante, menos mal\n\n")
    elif((not(v1>limite)) and (v2>limite)):
        print("\nOk, só o carro 2 tem um delinquente no volalente, menos mal\n\n")        
    elif((not(v1>limite)) and (not(v2>limite))):
        print("\nQue lindo, ambos os dois motoristas são bons cidadãos\n\n")
        
elif(op == 2):
    v = float(input("Velocidade: "))
    t = float(input("Tempo: "))
    d = v*t
    print("Distância: {} {}".format(d, distancia[op1-1]))
elif(op == 3):
    v = float(input("Velocidade: "))
    d = float(input("Distância percorrida: "))
    t = d/v
    print("Tempo: {} {}".format(t, tempo[op2-1]))




