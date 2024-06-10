def Main():
    while True:
        valores = input("Digite no mínimo 10 valores inteiros separados por UM separador *único!!* (exceto vírgula): ")
        separador = ''
        for c in valores:
            if not (c.isdigit() or c in [',']):
                separador = c
                break
        if separador == '':
            print("Erro ao identificar o separador, informe os números novamente...")
            continue

        valoresSep = valores.split(separador)
        if len(valoresSep) < 10:
            print("Erro ao identificar 10 valores inteiros. Certifique-se que está usando um único separador. Tente novamente...")
            continue
        
        valorVirgula = ','.join(valoresSep)
        print(f"os {len(valoresSep)} valores informados, agora separados por vírgula: {valorVirgula}")

        ordem = ''
        while True:
            ordem = input("Deseja listar os números em ordem crescente (c) ou decrescente (d)? ").lower()
            if ordem not in ['c', 'd']:
                print("Informe apenas crescente (c) ou decrescente (d)")
                continue
            else:
                break
            
        # Converte todos os elementos da lista valoresSep de strings para inteiros
        for i in range(len(valoresSep)):
            valoresSep[i] = int(valoresSep[i])

        # Bubble Sort
        n = len(valoresSep)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                # Ordena em ordem crescente se ordem == 'c'
                # Ordena em ordem decrescente se ordem == 'd'
                if (ordem == 'c' and valoresSep[j] > valoresSep[j + 1]) or (ordem == 'd' and valoresSep[j] < valoresSep[j + 1]):
                    # Troca os elementos de posição
                    valoresSep[j], valoresSep[j + 1] = valoresSep[j + 1], valoresSep[j] # Vai fazendo isso até trocar todos de posição e ordenar a lista

        # Converte todos os elementos da lista valoresSep de inteiros para strings
        for i in range(len(valoresSep)):
            valoresSep[i] = str(valoresSep[i])
            
        valorFinal = ','.join(valoresSep)
        print("lista ordenada:", valorFinal)

        while True:        
            escolha = input("Deseja continuar o programa? S/N: ").lower()
            if escolha not in ['s', 'n']:
                print("Informe apenas SIM (S) ou NÃO (N)")
                continue
            break
        if(escolha == 's'):
            continue
        else:
            break

Main()
