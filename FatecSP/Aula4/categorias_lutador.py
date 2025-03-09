def main():
    nome = input("Nome fornecido: ")
    peso = float(input("Peso fornecido: "))
    categoria = f"O lutador {nome} pesa {peso} e se enquadra na categoria "

    if peso < 65:
        categoria += "Pena"
    elif peso >= 65 and peso < 72:
        categoria += "Leve"
    elif peso >= 72 and peso < 79:
        categoria += "Ligeiro"
    elif peso >= 79 and peso < 86:
        categoria += "Meio médio"
    elif peso >= 86 and peso < 93:
        categoria += "Médio"
    elif peso >= 93 and peso < 100:
        categoria += "Médio pesado"
    else:
        categoria += "Pesado"

    print(categoria)

main()