def main():
    print("__________________Fibonacci_____________________")
    max: int = int(input("Informe número um inteiro: "))
    prim: int = int(input("Informe o prim: "))
    res = 0
    el1 = 0
    el2 = 1 # [0,1]
    i = 0

    resultado = ""
    while i < max:
        if(res > prim):
            resultado += f"{res} " #0, 1, 1, 2
        res = el1 + el2 #res = el1(0) + el2(1) =1/res = el1(1) + el2(0) = 1/res = el1(1) + el2(1) = 2

        el2 = el1 # el2(1) = el1(0) = 0/ el2(0) = el1(1) = 1/el2(1) = el1(1) = 1/
        el1 = res # el1(0) = res(1) = 1/ el1(1) = res(1) = 1/el1(1) = res(2) = 2/
        i += 1
        #troca pra ficar atual (res = último, el1 vira o último, el2 vira o penúltimo)

    print(resultado)

    with open("FibonacciPrim_output.txt", "w") as output: # FibonacciPrim_output.txt = nome, w = metodo (write, daria overwrite se já existisse algo em FibonacciPrim_output.txt)
        output.write(resultado)

main()
