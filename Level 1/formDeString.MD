# Formatação de Saídas e Entradas no Terminal Python

## 📝 Introdução
Este guia ensina técnicas profissionais para formatar saídas no terminal e receber entradas de usuário de forma eficiente em Python.

## 🖥️ Formatação de Saídas no Terminal

### 1. F-strings (Python 3.6+)
```python
nome = "João"
idade = 25
print(f"Olá, {nome}! Você tem {idade} anos.")
```

### 2. Método format()
```python
print("Olá, {}! Você tem {} anos.".format(nome, idade))
print("Preço: R${:.2f}".format(99.9876))  # Duas casas decimais
```

### 3. Alinhamento de Texto
```python
# < alinhado à esquerda, ^ centralizado, > alinhado à direita
print("{:<10} | {:^10} | {:>10}".format("Item", "Qtd", "Preço"))
print("{:<10} | {:^10} | {:>10}".format("Maçã", "5", "R$2.50"))
```

### 4. Cores no Terminal (usando Colorama)
```python
from colorama import Fore, Back, Style

print(Fore.RED + "Erro: Arquivo não encontrado" + Style.RESET_ALL)
print(Back.GREEN + Fore.WHITE + "Sucesso!" + Style.RESET_ALL)
```

### 5. Barra de Progresso
```python
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.02)  # Simula processamento
```

### 6. Tabelas Formatadas
```python
from tabulate import tabulate

dados = [
    ["Python", "3.9", "Popular"],
    ["JavaScript", "ES6", "Web"],
    ["Go", "1.17", "Rápido"]
]

print(tabulate(dados, headers=["Linguagem", "Versão", "Característica"]))
```

## ⌨️ Recebendo Entradas do Usuário

### 1. Input Básico
```python
nome = input("Digite seu nome: ")
print(f"Bem-vindo, {nome}!")
```

### 2. Validação de Entrada
```python
while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Por favor, digite um número válido!")
```

### 3. Menu Interativo
```python
def menu():
    print("\n=== MENU ===")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Sair")
    
    while True:
        escolha = input("Escolha uma opção: ")
        if escolha in ('1', '2', '3'):
            return escolha
        print("Opção inválida!")

opcao = menu()
```

### 4. Senha sem Eco
```python
from getpass import getpass

senha = getpass("Digite sua senha: ")
```

### 5. Entrada com Timeout
```python
import sys
import select

print("Você tem 5 segundos para responder...")
pergunta = "Qual é o seu animal favorito? "

if sys.stdin in select.select([sys.stdin], [], [], 5)[0]:
    resposta = input(pergunta)
else:
    resposta = None
    print("\nTempo esgotado!")
```

## 🛠️ Boas Práticas

1. **Mensagens claras**: Sempre indique o que você espera do usuário
2. **Tratamento de erros**: Antecipe entradas inválidas
3. **Formatação consistente**: Mantenha um padrão visual
4. **Feedback visual**: Confirme ações importantes

## 📚 Exemplo Completo
```python
from colorama import init, Fore
init(autoreset=True)

def formulario_contato():
    print(Fore.BLUE + "\n=== FORMULÁRIO DE CONTATO ===")
    
    # Recebendo dados
    nome = input(Fore.GREEN + "Nome completo: " + Fore.RESET)
    while not nome.strip():
        print(Fore.RED + "O nome não pode estar vazio!")
        nome = input(Fore.GREEN + "Nome completo: " + Fore.RESET)
    
    while True:
        try:
            idade = int(input(Fore.GREEN + "Idade: " + Fore.RESET))
            break
        except ValueError:
            print(Fore.RED + "Digite um número válido!")
    
    email = input(Fore.GREEN + "E-mail: " + Fore.RESET)
    
    # Exibindo resumo
    print(Fore.BLUE + "\n=== RESUMO ===")
    print(f"{Fore.YELLOW}Nome:{Fore.RESET} {nome}")
    print(f"{Fore.YELLOW}Idade:{Fore.RESET} {idade}")
    print(f"{Fore.YELLOW}E-mail:{Fore.RESET} {email}")

formulario_contato()
```

## 📌 Pacotes Úteis
- `colorama`: Para cores no terminal
- `tqdm`: Para barras de progresso
- `tabulate`: Para formatação de tabelas
- `getpass`: Para entrada de senhas seguras

