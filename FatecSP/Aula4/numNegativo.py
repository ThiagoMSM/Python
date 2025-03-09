def main():
    num = int(input("Informe um número inteiro: "))
    resultado = f"O número {num} é "
    if num < 0:
        resultado += "negativo"
    elif num == 0:
        resultado += "zero"
    else:
        resultado += "positivo"

    print(resultado)

main()