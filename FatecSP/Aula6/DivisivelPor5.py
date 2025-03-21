def main():
    print("___________________Divisível por 5________________________")
    while True:
        x, y = input("Informe dois valores (mínimo e máximo) separados por espaço: ").split()
        x, y = int(x), int(y)

        if x < y:
            break
        else:
            print("\nErro! Valor máximo deve ser menor que valor mínimo, insira novamente...")

    resultado = f"Os valores divisíveis por 5 que estão entre {x} e {y} são:"
    for i in range(x+1,y):
        if i % 5 == 0:
            resultado += f"\n{i}"

    print(resultado)

    with open("DiviselPor5_output.txt", "w") as output: # DiviselPor5_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em DiviselPor5_output.txt)
        output.write(resultado)

main()
