def main():
    print("___________________Divisível por 5________________________")
    while True:
        x, y = input("Informe dois valores (mínimo e máximo) separados por espaço: ").split()
        x, y = int(x), int(y)

        if x < y: #sucesso
            break
        else:
            print("\nErro! Valor máximo deve ser menor que valor mínimo, insira novamente...")

    resultado = f"Os valores divisíveis por 5 que estão entre {x} e {y} são:"

    i = x
    while i < y:
        if i % 5 == 0:
            resultado += f"\n{i}"
        i+=1
    print(resultado)

    with open("DiviselPor5_output.txt", "w") as output: # DiviselPor5_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em DiviselPor5_output.txt)
        output.write(resultado)

main()
