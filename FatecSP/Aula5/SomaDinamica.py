def main():
    print("________________Soma Dinâmica____________________")
    i = int(input("Informe quantos números deseja somar: "))
    soma: float = 0
    cont = 1
    while i >= 1:
        num = float(input(f"Informe o {cont}° número real: "))
        soma += num
        cont += 1
        i-= 1
    print(f"\nSoma: {soma}")
main()