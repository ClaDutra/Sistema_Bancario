#SISTEMA BANCÁRIO

#MENU

menu = """
[1] DEPOSITAR 
[2] SACAR
[3] EXTRATO
[4] SAIR

"""
#CONTA

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques= 3

#DEPOSITO

while True: 
    opcao = input(menu)

    if opcao == "1": 
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else: 
            print("Operação falhou! O valor informado é inválido.")
#SAQUE
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Opereção falhou! Você não tem saldo suficente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else: 
            print("Operação falhou! O valor inserido é inválido.")
    elif opcao == "3":
        print("\n=====EXTRATO=====")
        print("Não foram realizadas movimentações." if not	extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================") 
    elif opcao == "4":
        break
else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
               

