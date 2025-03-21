def main():
    print("___________________Soma pares em faixa_____________________")
    limite = 0
    msg = ""
    while limite < 12:
        if msg:
            print(msg) # kkkk lógica mais intrínsica possível

        msg = "\nErro! Valor deve ser no mínimo 100!"

        limite = int(input("Informe o limite da faixa (mínimo 100): "))


    acc = 0
    for i in range(1,limite):
        if i % 2 == 0:
            acc += i

    resultado = f"Somatório valores pares: {acc}"
    print(resultado)

    with open("SomaParesFaixa_output.txt", "w") as output: # SomaParesFaixa_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em SomaParesFaixa_output.txt)
        output.write(resultado)

main()
