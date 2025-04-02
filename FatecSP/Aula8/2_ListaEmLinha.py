listaNums = []
i = 1
print("_____________________Lista Nums em linha________________________")
while True:
    num = int(input(f"insira o {i}° termo (ou 0 ou negativo para encerrar...): "))
    if num <= 0:
        print("Encerrando o programa...")
        break
    listaNums.append(num)
    i += 1
print("\nSaída:")

if listaNums:
    for j in range(0,len(listaNums)):
        print(listaNums[j])
else:
    print("Lista sem elementos")
