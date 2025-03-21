def main():
    print("___________________Maior e Menor (positivo)______________________")

    i:int = 1
    listaNums:list = []
    x:int = int(input("Informe quantos valores POSITIVOS reais deseja inserir: "))
    while i <= x:
        num = float(input(f"Informe o {i}° valor: "))
        if num <= 0:
            print("número inválido")
        else:
            listaNums.append(num)
        i += 1

    if len(listaNums) > 0:
        resultado = f"\nMenor: {min(listaNums)}, Maior: {max(listaNums)}"
    else:
        resultado = "Os números informados não suportam classificação"

    print(resultado)

    with open("MenorMaiorPositivo_output.txt", "w") as output: # MenorMaiorPositivo_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em MenorMaiorPositivo_output.txt)
        output.write(resultado)

main()
