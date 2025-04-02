listaNums = []
i = 1
print("________________________Lista Nums_________________________")
while True:
    num = int(input(f"insira o {i}° termo (ou 0 ou negativo para encerrar...): "))
    if num <= 0:
        print("Encerrando o programa...")
        break
    listaNums.append(num)
    i += 1


res = f"\nLista final: {listaNums}"
if not listaNums:
    res = f"\nLista sem elementos"
print(res)
