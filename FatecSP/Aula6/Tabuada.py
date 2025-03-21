def main():
    print("_____________Gera Tabuada____________________")
    num: int = int(input("Informe número um inteiro: "))

    resultado: str = ""
    for i in range(1,11):
        resultado += f"{num} x {i} = {num*i}\n"

    print(resultado)

    with open("tabuada_output.txt", "w") as output: # tabuada_Output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em tabuada_output.txt)
        output.write(resultado)

main()
