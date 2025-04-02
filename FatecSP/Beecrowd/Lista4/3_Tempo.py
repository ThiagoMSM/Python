
horarios = [3600,60,1]
qtdes = []
N = int(input())

for horario in horarios: # pra cada horario...
    qtdeAtual = N//horario
    N = N % horario # atualiza o N
    qtdes.append(qtdeAtual)

acc = ""
for qtde in qtdes:
    acc += f'{qtde}'
    if qtde != qtdes[len(qtdes)-1]:
        acc += ":"

print(acc)



