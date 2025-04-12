
# Tipos de Variáveis em Python 🐍

Guia completo sobre os principais tipos de dados em Python, suas características e exemplos.

---

## 📌 **Tipos Básicos (Primitivos)**

### 1. **Números Inteiros (`int`)**
- **Descrição**: Armazenam números inteiros (positivos ou negativos).
- **Exemplo**:
  ```python
  idade = 25
  temperatura = -10
  ```
- **Operações comuns**: `+`, `-`, `*`, `//` (divisão inteira), `%` (módulo).

### 2. **Números Decimais (`float`)**
- **Descrição**: Armazenam números com ponto flutuante.
- **Exemplo**:
  ```python
  peso = 68.5
  pi = 3.14159
  ```
- **Cuidado**: Precisão limitada (ex: `0.1 + 0.2 != 0.3`).

### 3. **Strings (`str`)**
- **Descrição**: Sequências de caracteres (texto).
- **Exemplo**:
  ```python
  nome = "Alice"
  mensagem = 'Olá, mundo!'
  ```
- **Operações úteis**:
  ```python
  # Concatenação
  nome_completo = nome + " Silva"
  
  # F-strings (Python 3.6+)
  saudacao = f"Olá, {nome}!"
  
  # Métodos
  "python".upper()  # "PYTHON"
  ```

### 4. **Booleanos (`bool`)**
- **Descrição**: Representam `True` ou `False`.
- **Exemplo**:
  ```python
  eh_maior = idade > 18  # Retorna True ou False
  ligado = True
  ```

---

## 📌 **Tipos Compostos (Estruturas de Dados)**

### 1. **Listas (`list`)**
- **Descrição**: Coleções **mutáveis** e ordenadas.
- **Exemplo**:
  ```python
  frutas = ["maçã", "banana", "laranja"]
  numeros = [1, 2, 3]
  ```
- **Operações**:
  ```python
  frutas.append("uva")      # Adiciona item
  frutas[0] = "pera"       # Modifica item
  len(frutas)              # Tamanho da lista
  ```

### 2. **Tuplas (`tuple`)**
- **Descrição**: Coleções **imutáveis** e ordenadas.
- **Exemplo**:
  ```python
  coordenadas = (10, 20)
  cores_rgb = (255, 0, 0)
  ```
- **Uso típico**: Dados que não devem ser alterados (ex: constantes).

### 3. **Dicionários (`dict`)**
- **Descrição**: Pares **chave-valor** (não ordenados até Python 3.6+).
- **Exemplo**:
  ```python
  pessoa = {"nome": "Carlos", "idade": 30}
  ```
- **Operações**:
  ```python
  pessoa["profissao"] = "Engenheiro"  # Adiciona chave
  pessoa.get("nome", "Não existe")    # Busca segura
  ```

### 4. **Conjuntos (`set`)**
- **Descrição**: Coleções **não ordenadas** de itens **únicos**.
- **Exemplo**:
  ```python
  numeros = {1, 2, 3, 3}  # Vira {1, 2, 3}
  ```
- **Operações**:
  ```python
  a = {1, 2}; b = {2, 3}
  a.union(b)        # {1, 2, 3}
  a.intersection(b) # {2}
  ```

---

## 📌 **Tipos Especiais**

### 1. **`NoneType` (`None`)**
- **Descrição**: Representa a ausência de valor.
- **Exemplo**:
  ```python
  resultado = None
  ```

### 2. **Bytes (`bytes`)**
- **Descrição**: Sequências imutáveis de bytes (útil para dados binários).
- **Exemplo**:
  ```python
  dados = b"abc"
  ```

---

## 🔍 **Como Verificar o Tipo?**
Use a função `type()` ou `isinstance()`:
```python
type(idade)      # <class 'int'>
isinstance(10, int)  # True
```

---

## 💡 **Boas Práticas**
1. **Nomes descritivos**: `quantidade_produtos` em vez de `qp`.
2. **Conversão entre tipos**:
   ```python
   int("10")   # String → Inteiro
   str(3.14)   # Float → String
   ```
3. **Evite misturar tipos** em operações (ex: `"10" + 5` causa erro).

---

## 🛠 **Exemplo Prático**
```python
# Cadastro de produto
produto = {
    "nome": "Teclado",
    "preco": 99.90,
    "estoque": 50,
    "disponivel": True,
    "tags": {"eletrônico", "periférico"}
}
```

---

## 📚 **Para Aprofundar**
- [Documentação Oficial](https://docs.python.org/3/library/stdtypes.html)
- Livro: "Python Fluente" (Luciano Ramalho) - Cap. 2.
