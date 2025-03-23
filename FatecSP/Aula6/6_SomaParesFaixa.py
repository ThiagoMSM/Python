def main():
    print("___________________Soma pares em faixa_____________________")
    limite = 0
    msg = ""
    while limite < 100:
        if msg: #vazia de inicio...
            print(msg)

        msg = "\nErro! Valor deve ser no mínimo 100!"

        limite = int(input("Informe o limite da faixa (mínimo 100): "))


    acc = 0
    i = 1
    while i <= limite:
        if i % 2 == 0:
            acc += i
        i+=1

    resultado = f"Somatório valores pares: {acc}"
    print(resultado)

    with open("SomaParesFaixa_output.txt", "w") as output: # SomaParesFaixa_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em SomaParesFaixa_output.txt)
        output.write(resultado)

main()
