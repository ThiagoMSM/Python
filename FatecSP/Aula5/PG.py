def calculaPG(N: int, R: int, P:int ):
    resultados = []
    valAtual = P # primeiro termo
    resultados.append(valAtual)
    while N > 1:
        valAtual *= R
        resultados.append(valAtual)
        N -= 1

    return resultados

def main():
    print("_____________PG - Calculadora__________________")
    N = int(input("Informe o N° de termos da progressão: "))
    R = int(input("Informe a razão da progressão: "))
    P = int(input("Informe o 1° termo da progressão: "))

    print(*calculaPG(N, R, P)) #abrir o array pra eliminar os brackets..
main()
