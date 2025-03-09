def calcula_raiz(a,b,c):
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = ((b*-1) + delta**0.5)/(2*a)
        x2 = ((b*-1) - delta**0.5)/(2*a)

        return f"A equação possui delta positivo = {delta}, com duas raízes distintas, sendo: x1 = {x1} e x2 = {x2}"
    elif delta < 0:
        return f"A equação possui delta negativo = {delta}, e portanto, não possui soluções reais"
    else:
        x = (b*-1)/2*a
        return f"A equação possui delta nulo, portanto, possui apenas uma raiz, sendo ela = {x}"

def main():
    a = float(input("Informe o valor de A: "))
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))

    print(calcula_raiz(a,b,c))

main()