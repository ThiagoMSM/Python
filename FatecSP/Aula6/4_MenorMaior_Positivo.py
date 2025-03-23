def main():
    print("___________________Maior e Menor (positivo)______________________")
    i = 0
    x: int = int(input("Informe quantos valores POSITIVOS reais deseja inserir: "))

    menor = "valor inicial"
    maior = "valor inicial"

    while i < x:
        nums = float(input(f"Informe o {i+1}° valor: "))
        if nums <= 0:
            print("Valor inválido! Número ignorado...")
        else:

            if menor == "valor inicial" or maior == "valor inicial": #teoricamente só precisa checar um, mas assim fica mais bonito e + entendível
                menor = nums
                maior = nums

            if nums < menor:
                menor = nums
            if nums > maior:
                maior = nums
        i += 1

    if menor == "valor inicial" or maior == "valor inicial":
        resultado = "\nOs números informados não suportam classificação"
    else:
        resultado = f"\nMenor: {menor}\nMaior: {maior}"

    print(resultado)

    with open("MenorMaiorPositivo_output.txt", "w") as output: # MenorMaiorPositivo_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em MenorMaiorPositivo_output.txt)
        output.write(resultado)

main()
