saldo = 0
extrato = ""

taxa_mensal = 0.05
meses = 5
anos = 1

while True:
    print("=== SISTEMA BANCÁRIO ===")
    print("")
    print("1 - Ver saldo ")
    print("2 - Depositar ")
    print("3 - Sacar ")
    print("4 - Ver extrato ")
    print("5 - Investimentos")
    print("6 - Meu porquinho")
    print("7 - Sacar valor do porquinho")
    print("8 - Sair")
    print("========================")

    Opcao = input("Digite seu interesse:  ")

    if Opcao == "1":
        print("Seu saldo atual é = ", saldo)

    elif Opcao == "2":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo = saldo + valor
            print("Deposito Realizado! ")
            extrato = extrato + f"Depósito de R$ {valor}\n"

        else:
            print("Valor Inválido! ")
    
    elif Opcao == "3":
        valor = float(input("Digite a quantia que deja sacar R$: "))
        if valor > 0:
            if saldo >= valor:
                saldo = saldo - valor
                print("Saque realizado !")
                extrato = extrato + f"Saque de R$ {valor}\n"
            else:
                print("Saldo Insuficiente! ")
        else:
            print("Valor Inválido! ")
    
    elif Opcao == "4":
        if extrato == "":
            print("Nenhuma movimentação")
        else:
            print(extrato)

    elif Opcao == "5":
        print("Digite o quanto você deseja investir: ")
        valor = float(input("Valor do investimento R$: "))
        if valor > 0:
            saldo = saldo - valor
            print("Investimento realizado! ")
            extrato = extrato + f"Investimento de R$ {valor}\n"

            meses_em_anos = anos * 12

            montante_meses = valor * (1 + taxa_mensal) ** meses
            montante_anos = valor * (1 + taxa_mensal) ** meses_em_anos

            print(f"Em {meses} meses, seu dinheiro vira: R$ {montante_meses:.2f}")
            print(f"Em {anos} anos, seu dinheiro vira: R$ {montante_anos:.2f}")
        else:
            print("Valor Inválido! ")

    elif Opcao == "6":
        print("Digite o quanto você deseja depositar no porquinho: ")
        valor = float(input("Valor do depósito R$: "))
        if valor > 0:
            saldo = saldo + valor
            print("Depósito realizado! ")
            extrato = extrato + f"Depósito de R$ {valor}\n"

            ganho_diario = 0.01
            dias_para_lucro_igual = int(round(valor * 100))
            print("Você ganha R$0.01 por dia no porquinho.")
            print(f"Levará {dias_para_lucro_igual} dias para lucrar R$ {valor:.2f}.")

    elif Opcao == "7":
        valor = float(input("Digite a quantia que deja sacar do seu porquinho R$: "))
        if valor > 0:
            if valor <= saldo:
                saldo = saldo - valor
                print("Saque realizado !")
                extrato = extrato + f"Saque de R$ {valor}\n"
            else:
                print("Saldo Insuficiente! ")

    elif Opcao == "8":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")