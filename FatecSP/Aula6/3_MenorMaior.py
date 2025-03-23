def main():
    print("________________Maior e Menor___________________")

    i = 0
    x: int = int(input("Informe quantos valores reais deseja inserir: "))

    menor = 0
    maior = 0
    while i < x:
        nums = float(input(f"Informe o {i+1}° valor: "))
        if i == 0:
            menor = nums
            maior = nums

        if nums < menor:
            menor = nums
        if nums > maior:
            maior = nums
        i += 1

    resultado = f"Menor: {menor}\nMaior: {maior}"


    print(resultado)

    with open("MenorMaior_output.txt", "w") as output: # MenorMaior_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em MenorMaior_output.txt)
        output.write(resultado)

main()
