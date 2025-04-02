def montaListas(index):
    listaNums = list()
    i = 1
    print(f"{index}ª lista:")
    while i <= 10:
        num = int(input(f"insira o {i}°/10 termo da {index}ª lista: "))
        listaNums.append(num)
        i += 1

    print("___________________________________________________\n") #Quebra de linha visual etc
    return listaNums

print("_____________________Junta listas________________________")
print("Insira duas listas de tamanho 10 para efetuar a junção.")

lista1:list = montaListas(1)
lista2:list = montaListas(2)

print(f"Lista final:\n{lista1+lista2}")
