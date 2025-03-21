def main():
    print("___________________Divisíveis por 2 e 3_____________________")
    i = 1
    num = 1
    listaNums = []
    while num != 0:
        num = float(input(f"Informe o {i}° valor, ou digite 0 para finalizar o loop: "))
        if (num % 2 == 0 or num % 3 == 0) and num != 0:
            if num not in listaNums:
                listaNums.append(num)
        i += 1


    resultado = "Valores divisíveis por 2 ou 3:\n"
    if len(listaNums) > 0:
        resultado += str(listaNums)[1:-1] #pega entre o 2 elemento e o último... (elimina os brackets, pq por algum motivo DIVINO, o python nao aceita * aqui...)
    else:
        resultado += "Nenhum valor"

    print(resultado)

    with open("Divisiveis2e3_output.txt", "w") as output: # Divisiveis2e3_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em Divisiveis2e3_output.txt)
        output.write(resultado)

main()
