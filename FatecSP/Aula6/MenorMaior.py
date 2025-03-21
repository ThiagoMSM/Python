def main():
    print("________________Maior e Menor___________________")

    i = 1
    listaNums :list = []
    x: int = int(input("Informe quantos valores reais deseja inserir: "))
    while i <= x:
        listaNums.append(float(input(f"Informe o {i}° valor: ")))
        i += 1

    resultado: str = f"\nMenor: {min(listaNums)}, Maior: {max(listaNums)}"


    print(resultado)

    with open("MenorMaior_output.txt", "w") as output: # MenorMaior_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em MenorMaior_output.txt)
        output.write(resultado)

main()
