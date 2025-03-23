def main():
    print("___________________Min, Max, Soma, Média______________________")

    i = 0
    soma = 0

    print("Informe 0 ou um número negativo para encerrar a execução...")
    while True:
        nums = float(input(f"Informe o {i+1}° valor: "))

        if nums <= 0:
            print("Encerrando... Último valor não será contabilizado")
            break

        soma += nums
        if i == 0: #1a iteração
            menor = maior = nums

        if nums < menor:
            menor = nums
        if nums > maior:
            maior = nums
        i += 1

    qtde = 0
    media = 0
    if i != 0:
        qtde = i
        media = soma/qtde


    if qtde:
        resultado = f"\nMenor: {menor}\nMaior: {maior}\nQtde: {qtde}\nSoma: {soma}\nMédia: {media}"
    else:
        resultado = "\nNenhum valor informado"
    print(resultado)

    with open("PositivosMinMaxMediaSoma_output.txt", "w") as output: # PositivosMinMaxMediaSoma_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em PositivosMinMaxMediaSoma_output.txt)
       output.write(resultado)

main()
