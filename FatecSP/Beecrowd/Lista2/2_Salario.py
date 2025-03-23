salario = float(input())
fator = 0.04

if salario >= 0 :
    if salario <= 400:
        fator = 0.15
    elif salario <= 800:
        fator = 0.12
    elif salario <= 1200:
        fator = 0.10
    elif salario <= 2000:
        fator = 0.07

reajuste = salario*fator

print(f"Novo salario: {salario+reajuste:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {fator*100:.0f} %")

