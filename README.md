# Sistema Bancário — Desafio DIO

**Descrição curta (para usar como descrição do repositório no GitHub):**

> Sistema bancário simples (Desafio DIO) — operações: depósito, saque (máx. 3 saques/dia, R\$ 500/saque) e extrato.

---

## Descrição

Projeto simples em Python desenvolvido como desafio da plataforma **DIO**. O objetivo é implementar um sistema bancário básico com três operações: **Depósito**, **Saque** e **Extrato** — respeitando as regras do enunciado do desafio.

Este repositório serve como projeto pessoal para demonstrar lógica básica de backend, controle de fluxo e validações em Python.

## Funcionalidades

* Depósito: aceita valores positivos e registra o depósito para exibição no extrato.
* Saque: permite até **3 saques diários** e **R\$ 500,00** por saque; valida saldo e valores inválidos; registra saques no extrato.
* Extrato: lista todas as movimentações (depósitos e saques) e mostra o saldo atual. Se não houver movimentações, exibe: "Não foram realizadas movimentações.".
* Formatação de valores em `R$ {valor:.2f}`.

## Requisitos

* Python 3.8 ou superior

## Como executar

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
```

2. Execute o script (supondo que o arquivo principal seja `main.py`):

```bash
python main.py
```

> Observação: o script roda em modo terminal/console e interage via `input()`.

## Exemplo de uso (exemplo de sessão no terminal)

```
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> 1
Depósito:
Digite o valor a ser depositado: 1500
Depósito de R$ 1500.00 realizado.

=> 2
Saque:
Digite o valor a ser sacado: 200
Saque de R$ 200.00 realizado.

=> 3
Extrato:
Depósito: R$ 1500.00
Saque: R$ 200.00
Saldo atual: R$ 1300.00
```

## Estrutura sugerida do repositório

```
├─ README.md
├─ main.py        # script com a lógica do sistema bancário
└─ .gitignore
```

## Código (versão sugerida)

Abaixo há uma versão sugerida e comentada do programa, que armazena cada movimentação em uma lista para imprimir o extrato linha a linha.

```python
# main.py

def main():
    menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

    saldo = 0.0
    limite = 500.0
    LIMITE_SAQUES = 3
    numero_saques = 0
    extrato = []  # lista que guarda as movimentações (strings)

    while True:
        opcao = input(menu).strip()

        if opcao == "1":
            try:
                valor = float(input("Digite o valor a ser depositado: ").replace(',', '.'))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            if valor <= 0:
                print("Essa operação não pode ser concluída.")
            else:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado.")

        elif opcao == "2":
            if numero_saques >= LIMITE_SAQUES:
                print("Você atingiu o limite de saques diários.")
                continue

            try:
                valor = float(input("Digite o valor a ser sacado: ").replace(',', '.'))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            if valor <= 0:
                print("Não será possível realizar esta operação.")
            elif valor > limite:
                print(f"O valor escolhido ultrapassa o limite de R$ {limite:.2f}")
            elif valor > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= valor
                numero_saques += 1
                extrato.append(f"Saque: R$ {valor:.2f}")
                print(f"Saque de R$ {valor:.2f} realizado.")

        elif opcao == "3":
            print("\n------- EXTRATO -------")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                for mov in extrato:
                    print(mov)
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("-----------------------\n")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
```

## Sugestões de melhorias (próximos passos)

* Persistir as movimentações em arquivo (JSON / CSV) para carregar o extrato entre execuções.
* Adicionar data/hora às transações.
* Implementar testes automatizados (pytest) para as regras: limite de saque, número de saques e formatação.
* Criar uma versão com interface web (Flask/FastAPI) para treinar APIs REST.

## Contribuição

Pull requests são bem-vindos. Se for enviar alterações, descreva claramente o que foi feito e mantenha o padrão de formatação do código.

## Licença

Escolha uma licença (por exemplo: MIT). Se quiser, posso adicionar um `LICENSE` ao repositório.
