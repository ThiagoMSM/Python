def Main():
	while True:
		try:
			pcunit = float(input("Informe o valor unitário: "))
			qtde = int(input("Informe a qtde: "))
			total = pcunit * qtde
			aliq = 0.18
			vsi = total / (aliq + 1)
			imposto = total - vsi
			print(f'Total: R$ {total:.2f}')
			print(f'Imposto: R$ {imposto:.2f}')
			print(f'VSI: R$ {vsi:.2f}')
		except:
			print("deu ruim")
Main()
