salario = float(input())

if salario <= 2000:
    print("Isento")
else:
    imposto = 0
    faixa1 = 1000  # 2000 - 3000
    faixa2 = 1500  # 3000 - 4500

    if salario > 4500:
        imposto += (salario - 4500) * 0.28
        salario = 4500
    if salario > 3000:
        imposto += (salario - 3000) * 0.18
        salario = 3000
    if salario > 2000:
        imposto += (salario - 2000) * 0.08

    print(f"R$ {imposto:.2f}")
