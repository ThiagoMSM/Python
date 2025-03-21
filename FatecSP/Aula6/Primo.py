def primo(num: int):
    divisores:list = []
    if num < 2:
        return "não é primo, pois é um ou nulo/negativo."

    for i in range(2, num):
        if num % i == 0:
            divisores.append(i)

    if divisores:
        return f"não é primo, pois é divisível por: {str(divisores)[1:-1]}"
    else:
        return "é primo"

def main():
    print("__________________Verifica Primo_____________________")
    num: int = int(input("Informe número um inteiro: "))

    resultado = f"O número {num} {primo(num)}"


    print(resultado)

    with open("Primo.txt", "w") as output: # Primo.txt = nome, w = metodo (write, daria overwrite se já existisse algo em Primo.txt)
        output.write(resultado)

main()
