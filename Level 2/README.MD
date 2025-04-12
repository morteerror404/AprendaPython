# Estruturas de Controle em Python 🔄

Guia completo sobre condicionais (`if-elif-else`) e loops (`for`, `while`) em Python.

---

## 📌 **Condicionais (`if`, `elif`, `else`)**

### 1. **Estrutura Básica**
```python
if condição:
    # Executa se a condição for True
elif outra_condição:  # Opcional
    # Executa se a primeira condição for False e esta for True
else:  # Opcional
    # Executa se todas as condições anteriores forem False
```

### 2. **Exemplos Práticos**
#### Verificação de Idade:
```python
idade = 18

if idade < 12:
    print("Criança")
elif 12 <= idade < 18:
    print("Adolescente")
else:
    print("Adulto")
```

#### Login Simples:
```python
senha_correta = "python123"
senha_digitada = input("Digite sua senha: ")

if senha_digitada == senha_correta:
    print("Acesso permitido!")
else:
    print("Senha incorreta!")
```

### 3. **Operadores Usados em Condicionais**
| Operador | Significado          | Exemplo           |
|----------|----------------------|-------------------|
| `==`     | Igualdade            | `if x == 10:`     |
| `!=`     | Diferente            | `if y != "ok":`   |
| `>`      | Maior que            | `if saldo > 0:`   |
| `<`      | Menor que            | `if idade < 18:`  |
| `and`    | E lógico             | `if x > 0 and y < 10:` |
| `or`     | OU lógico            | `if erro or timeout:` |
| `not`    | Negação              | `if not vazio:`   |

---

## 📌 **Loops (`for`, `while`)**

### 1. **Loop `for`**
#### Iteração em Sequências:
```python
# Lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta.upper())

# String
for letra in "Python":
    print(letra)

# Range (geração de números)
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)
```

#### Com `enumerate()` (índice + valor):
```python
for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}. {fruta}")
```

### 2. **Loop `while`**
#### Executa enquanto a condição for verdadeira:
```python
contador = 0
while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1  # Incremento para evitar loop infinito
```

#### Exemplo com `break`:
```python
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando.lower() == "sair":
        break  # Sai do loop
    print("Comando inválido!")
```

### 3. **Controle de Loops**
| Comando   | Efeito                              | Exemplo                     |
|-----------|-------------------------------------|-----------------------------|
| `break`   | Interrompe o loop imediatamente     | `if erro: break`            |
| `continue`| Pula para a próxima iteração        | `if x % 2 == 0: continue`   |
| `else`    | Executa se o loop **não** for interrompido por `break` | `for x in lista: ... else: print("Fim!")` |

---

## 🔄 **Padrões Comuns**

### 1. **Iteração em Dicionários**
```python
pessoa = {"nome": "Maria", "idade": 30}

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

### 2. **Loops Aninhados**
```python
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
```

### 3. **List Comprehension**
```python
# Filtra números pares
pares = [x for x in range(10) if x % 2 == 0]
```

---

## ⚠️ **Cuidados Importantes**
1. **Loops Infinitos**: Sempre garanta que um `while` tenha condição de saída.
   ```python
   # ❌ Errado (loop infinito)
   while saldo > 0:
       print("Gastando...")
       # Esqueceu de decrementar saldo!
   ```

2. **Modificar Listas Durante Iteração**:
   ```python
   # ❌ Evite (pode causar comportamentos inesperados)
   for item in lista:
       lista.remove(item)
   
   # ✅ Correto (crie uma cópia)
   for item in lista.copy():
       lista.remove(item)
   ```

---

## 🛠 **Exemplo Integrado**
```python
# Verifica números primos
numero = int(input("Digite um número: "))
eh_primo = True

for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        eh_primo = False
        break

print(f"{numero} é primo!" if eh_primo else "Não é primo.")
```

---

## 📚 **Para Aprofundar**
- [Documentação Oficial - Compound Statements](https://docs.python.org/3/reference/compound_stmts.html)
- Livro: "Python Crash Course" (Eric Matthes) - Cap. 5 e 7.