lista: list = [0, 1]  # fazer ser recursive friendly, e acabou
acc:int = 0

def Fibonacci(max: int):
    global acc
    global lista
    for j in range(0,len(lista)):
        acc += lista[j]

    lista.append(acc)
    print(acc)

    if len(lista) <= max:
       Fibonacci(max-1)

    return lista

def main():
    print("__________________Fibonacci_____________________")
    max: int = int(input("Informe número um inteiro: "))

    print(Fibonacci(max))


    #print(resultado)

   # with open("Primo.txt", "w") as output: # Primo.txt = nome, w = metodo (write, daria overwrite se já existisse algo em Primo.txt)
   #     output.write(resultado)

main()
