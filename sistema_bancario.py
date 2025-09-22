# ... implementar apenas 3 operações: depósito, saque e extrato. + 

# Operação depósito:
# ... Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato +

# Operação saque:
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. +
# Caso não tenha saldo na conta, o sistema deve exibir uma mensagem. Todos os saques devem ser armazenados em uma variável e exibidos no extrato. +

# Operação extrato:
# ... deve listar todos os depósitos e saques realizados na conta. +
# No fim deve ser exibido o saldo atual da conta. +
# Caso não tenha operações, deverá exibir: "Não foram realizadas movimentações." +
# Osvalores devem ser exibidos utilizando R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45 + 

# minha tentativa:

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

numero_depositos = 0
total_depositado = 0

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito:")
        deposito = float(input("Digite o valor à ser depositado: "))
        if deposito <= 0:
            print("Essa operação não pode ser concluída.")
        else:
            saldo = saldo + deposito
            numero_depositos += 1
            total_depositado += deposito

    elif opcao == "2":
        print("Saque:")
        numero_saques += 1
        if numero_saques > 3:
            print("Você atingiu o limite de saques diários.")
        else:
            saque = float(input("Digite o valor à ser sacado: "))

            if saque > limite:
                print(f"O valor escolhido ultrapassa o limite de R$ {limite:.2f}")
                numero_saques -= 1
            elif saque > saldo or saque <= 0:
                print("Não será possível realizar esta operação.")
                numero_saques -= 1
            else: 
                saldo = saldo - saque

    elif opcao == "3":
        print("Extrato:")

        if numero_saques + numero_depositos <= 0:
            print("Não foram realizadas movimentações.")
        else:
            print(f"Foram realizados {numero_depositos} depósitos e {numero_saques} saques, hoje.")
            print(f"Seu valor total depositado foi: R$ {total_depositado:.2f}")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Saindo...")
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")

