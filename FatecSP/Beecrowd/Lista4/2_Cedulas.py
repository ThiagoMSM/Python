
notas = [100,50,20,10,5,2,1]
qtdes = []
N = int(input())
aux = N
if 0 < N < 1000000:
    for nota in notas: # pra cada nota...
        qtdeAtual = N//nota
        N = N % nota # atualiza o N
        qtdes.append(qtdeAtual)

    print(aux)
    for i in range(len(qtdes)):
        print(f"{qtdes[i]} nota(s) de R$ {notas[i]},00")


