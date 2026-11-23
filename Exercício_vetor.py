vetor = []
ADM = []
for i in range(1):
    a = int(input("Digite a quantidade de chamados registrado na Segunda-Feira :"))
    a.append(vetor)
    if a < 0 :
        print("Valor invalido")
        a = int(input("Digite a quantidade de chamados registrado na Segunda-Feira :"))
    b = int(input("Digite a quantidade de chamados registrado na Terça-Feira :"))
    b.append(vetor)
    if b < 0 :
        print("Valor invalido")
        b = int(input("Digite a quantidade de chamados registrado na Terça-Feira :"))
    c = int(input("Digite a quantidade de chamados registrado na Quarta-Feira :"))
    c.append(vetor)
    if c < 0 :
        print("Valor invalido")
        c = int(input("Digite a quantidade de chamados registrado na Quarta-Feira :"))
    d = int(input("Digite a quantidade de chamados registrado na Quinta-Feira :"))
    d.append(vetor)
    if d < 0 :
        print("Valor invalido")
        d = int(input("Digite a quantidade de chamados registrado na Quinta-Feira :"))
    e = int(input("Digite a quantidade de chamados registrado na Sexta-Feira :"))
    e.append(vetor)
    if e < 0 :
        print("Valor invalido")
        e = int(input("Digite a quantidade de chamados registrado na Sexta-Feira :"))
    if a > g :
        a.append(ADM)
    elif b > g :
        b.append(ADM)
    elif c > g :
        c.append(ADM)
    elif d > g :
        d.append(ADM)
    elif e > g :
        e.append(ADM)
    f = a+b+c+d+e
    g = (a+b+c+d+e)/5
print(f"O número de chamados na Segunda-Feira é : {a}")
print(f"O número de chamados na Terça-Feira é : {b}")
print(f"O número de chamados Quarta-Feira é : {c}")
print(f"O número de chamados na Quinta-Feira é : {d}")
print(f"O número de chamados na Sexta-Feira é : {e}")
print(f"O total de Chamados é igual a {f}:")
print(f"A média é : {g}")
print(f"Os dia(s) acima da média foram/foi : {ADM}")
print(vetor)
