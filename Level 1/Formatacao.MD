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

# **Conversão de Tipos em Python**  

Este guia explica como **alterar o tipo de uma variável** em Python, incluindo métodos nativos, boas práticas e exemplos práticos.  

---

## **📌 Tipos de Dados em Python**  
Python possui vários tipos de dados básicos:  

| **Tipo**      | **Descrição**           | **Exemplo**       |
|--------------|------------------------|------------------|
| `int`        | Números inteiros        | `10`, `-5`       |
| `float`      | Números decimais        | `3.14`, `-0.5`   |
| `str`        | Texto (strings)         | `"Python"`       |
| `bool`       | Valores lógicos         | `True`, `False`  |
| `list`       | Listas mutáveis         | `[1, 2, 3]`      |
| `tuple`      | Tuplas imutáveis        | `(1, 2, 3)`      |
| `dict`       | Dicionários (chave-valor) | `{"nome": "João"}` |

---

## **🔄 Como Converter Tipos?**  

### **1️⃣ `int()` → Converte para inteiro**  
```python
numero_str = "10"
numero_int = int(numero_str)  # Converte str para int
print(numero_int, type(numero_int))  # Saída: 10 <class 'int'>

# Cuidado: Se não for um número válido, causa erro!
# int("dez") → ValueError
```

### **2️⃣ `float()` → Converte para decimal**  
```python
numero_str = "3.14"
numero_float = float(numero_str)  # Converte str para float
print(numero_float, type(numero_float))  # Saída: 3.14 <class 'float'>
```

### **3️⃣ `str()` → Converte para string**  
```python
numero = 42
texto = str(numero)  # Converte int para str
print(texto, type(texto))  # Saída: "42" <class 'str'>
```

### **4️⃣ `bool()` → Converte para booleano**  
```python
valor = 10
valor_bool = bool(valor)  # Converte para True/False
print(valor_bool, type(valor_bool))  # Saída: True <class 'bool'>

# Valores que viram False:
# 0, "", [], None, False
```

### **5️⃣ `list()`, `tuple()`, `dict()` → Conversão entre coleções**  
```python
lista = [1, 2, 3]
tupla = tuple(lista)  # Converte lista em tupla
print(tupla)  # Saída: (1, 2, 3)

texto = "Python"
lista_chars = list(texto)  # Converte str em lista
print(lista_chars)  # Saída: ['P', 'y', 't', 'h', 'o', 'n']
```

---

## **⚠️ Cuidados na Conversão**  

### **1. Conversões inválidas causam `ValueError`**  
```python
# int("abc") → ValueError
# float("3,14") → ValueError (use "3.14")
```

### **2. Perda de precisão em `int` → `float`**  
```python
numero = 3.99
print(int(numero))  # Saída: 3 (perde a parte decimal)
```

### **3. Conversão implícita em operações**  
```python
resultado = 5 + 2.0  # int + float → float
print(resultado, type(resultado))  # 7.0 <class 'float'>
```

---

## **📌 Exemplos Práticos**  

### **1. Convertendo entrada do usuário**  
```python
idade = input("Digite sua idade: ")  # Retorna str
idade_int = int(idade)  # Converte para int

if idade_int >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade.")
```

### **2. Convertendo lista em string**  
```python
frutas = ["maçã", "banana", "laranja"]
frutas_str = ", ".join(frutas)  # Converte lista em str
print(frutas_str)  # Saída: "maçã, banana, laranja"
```

### **3. Verificando tipos com `type()`**  
```python
valor = 10.5
print(type(valor))  # <class 'float'>

if type(valor) == float:
    print("É um float!")
```

---

## **📚 Resumo das Funções de Conversão**  

| **Função** | **Converte para** | **Exemplo** |
|------------|------------------|-------------|
| `int()`    | Inteiro          | `int("10") → 10` |
| `float()`  | Decimal          | `float("3.14") → 3.14` |
| `str()`    | String           | `str(42) → "42"` |
| `bool()`   | Booleano         | `bool(1) → True` |
| `list()`   | Lista            | `list("abc") → ['a', 'b', 'c']` |
| `tuple()`  | Tupla            | `tuple([1, 2]) → (1, 2)` |
| `dict()`   | Dicionário       | `dict([("a", 1), ("b", 2)]) → {"a": 1, "b": 2}` |

---

## **🚀 Conclusão**  
- Use `int()`, `float()`, `str()`, etc., para converter tipos.  
- Sempre valide entradas antes de converter.  
- Cuidado com perda de dados em conversões (`float` → `int`).  
