def main():
    print("________________________Total Números Inteiros______________________________")
    posi = 0
    neg = 0
    i = 1
    while True:
        num = int(input(f"Informe o {i}° número inteiro (ou 0 para finalizar e visualizar o resultado): "))
        if (num == 0):
            break

        if num < 0:
            neg += num
        else:
            posi += num

        i += 1

    print(f"\n\nTotal dos positivos = {posi}")
    print(f"Total dos negativos = {neg}")
main()