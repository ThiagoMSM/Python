def primo(num: int):
    divisores: str = ""
    i = 2
    if num < 2:
        return "não é primo, pois é um ou nulo/negativo."

    while i < num:
        if num % i == 0:
            divisores += f"{i} "
        i+=1

    if divisores:
        return f"não é primo, pois é divisível por: {divisores}"
    else:
        return "é primo"

def main():
    print("__________________Verifica Primo_____________________")
    num: int = int(input("Informe número um inteiro: "))

    resultado = f"O número {num} {primo(num)}"


    print(resultado)

    with open("Primo_output.txt", "w") as output: # Primo_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em Primo_output.txt)
        output.write(resultado)

main()
