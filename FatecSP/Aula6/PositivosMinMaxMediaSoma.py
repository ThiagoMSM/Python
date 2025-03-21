def main():
    print("___________________Min, Max, Soma, Média______________________")

    i = 1
    soma = 0
    listaNums = []


    print("Informe 0 ou um número negativo para encerrar a execução...")
    while True:
        num = int(input(f"Informe o {i}° valor: "))

        if num <= 0:
            break
        else:
            listaNums.append(num)
            soma += num
        i += 1

    menor = min(listaNums)
    maior = max(listaNums)
    qtde = len(listaNums)
    media = soma/qtde



    resultado = f"Menor: {menor}\nMaior: {maior}\nQtde: {qtde}\nSoma: {soma}\nMédia: {media}"
    print(resultado)

    with open("PositivosMinMaxMediaSoma_output.txt", "w") as output: # PositivosMinMaxMediaSoma_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em PositivosMinMaxMediaSoma_output.txt)
       output.write(resultado)

main()
