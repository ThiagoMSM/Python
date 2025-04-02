listaElem = list()
i = 1
print("_____________________Lista inversa________________________")
while i <= 10:
    num = input(f"insira o {i}°/10 termo: ")
    listaElem.append(num)
    i += 1

listaInversa = []

j = len(listaElem)
while j > 0:
    listaInversa.append(listaElem[j-1]) # -1 pq o index começa em 0
    j -= 1

#ou usar listaElem.reverse()
print(f"\nLista inversa: {listaInversa}")
