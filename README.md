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

## Sugestões de melhorias (próximos passos)

* Persistir as movimentações em arquivo (JSON / CSV) para carregar o extrato entre execuções.
* Adicionar data/hora às transações.
* Implementar testes automatizados (pytest) para as regras: limite de saque, número de saques e formatação.
* Criar uma versão com interface web (Flask/FastAPI) para treinar APIs REST.

## Contribuição

Pull requests são bem-vindos. Se for enviar alterações, descreva claramente o que foi feito e mantenha o padrão de formatação do código.

## Licença

Escolha uma licença (por exemplo: MIT). Se quiser, posso adicionar um `LICENSE` ao repositório.
