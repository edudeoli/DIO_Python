menu = ("""
  [d] depositar
  [s] sacar
  [e] extrato
  [q] sair
""")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
valor = ()

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Vo ê não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque ecede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Npumero mpaximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "e":
        print("\n================= EXTRATO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")

    elif opcao == "q":
        break

else:
    print("Opção inválida. Por favor escolha novamente uma opção válida.")
