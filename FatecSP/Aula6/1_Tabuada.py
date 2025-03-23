def main():
    print("_____________Gera Tabuada____________________")
    num: int = int(input("Informe número um inteiro: "))

    resultado: str = ""
    i = 1
    while i <= 10:
        resultado += f"{num} x {i} = {num*i}\n"
        i+= 1
    print(resultado)

    with open("tabuada_output.txt", "w") as output: # tabuada_Output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em tabuada_output.txt)
        output.write(resultado)

main()
