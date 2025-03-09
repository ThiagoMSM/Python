
def define_maior(a: float,b: float,c: float):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def define_triangulo(a: float,b: float,c: float):

    if a == b == c:
        return "O triângulo é equilátero" # return antecipado (não precisa fazer os outros testes...)


    maior = define_maior(a,b,c)
    lista_valores = [a,b,c]
    lista_valores.remove(maior)

    x,y = lista_valores # restante... = os 2 não maiores

    if x + y > maior: #regra da desigualdade triangular

        #isosceles (pelo menos dois lados iguais):
        if x == y or x == maior or y == maior:
            return "O triâgulo é isósceles"
        else: #..tudo diferente
            return "O triângulo é escaleno"
    else:
        return "Os valores de a, b, c informados não constituem um triângulo."



def main():
    a = float(input("Informe o valor de A: "))
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))

    print(define_triangulo(a,b,c))

main()