N = int(input())
i = 0

C = 0
R = 0
S = 0
while i < N:
    quantia, tipo = input().split()
    quantia = int(quantia)

    if tipo.upper() == 'C':
        C += quantia
    elif tipo.upper() == 'R':
        R += quantia
    elif tipo.upper() == 'S':
        S += quantia
    i+=1

total = C+R+S
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")


print(f"Percentual de coelhos: {(C*100)/total:.2f} %")
print(f"Percentual de ratos: {(R*100)/total:.2f} %")
print(f"Percentual de sapos: {(S*100)/total:.2f} %")
