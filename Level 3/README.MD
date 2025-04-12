# Funções e Métodos em Python 🛠️

Guia completo sobre definição, uso e padrões com funções e métodos em Python.

---

## 📌 **Funções Básicas**

### 1. **Definindo Funções (`def`)**
```python
def saudacao(nome):
    """Documentação: Retorna uma mensagem de saudação."""
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao("Maria")
```

### 2. **Parâmetros e Argumentos**
| Tipo               | Exemplo                      | Descrição                          |
|--------------------|------------------------------|------------------------------------|
| Posicionais        | `funcao(x, y)`               | Ordem importa                      |
| Nomeados           | `funcao(y=2, x=1)`           | Ordem não importa                  |
| Default            | `def funcao(x=10)`           | Valor padrão se não fornecido      |
| Arbitrários (`*args`) | `def funcao(*args)`       | Recebe tupla de argumentos posicionais |
| Arbitrários (`**kwargs`) | `def funcao(**kwargs)` | Recebe dicionário de argumentos nomeados |

**Exemplo Avançado:**
```python
def calcular(operacao, *nums, **opcoes):
    """Calcula valores com flexibilidade."""
    if opcoes.get("arredondar"):
        return round(sum(nums), 2)
    return sum(nums)

calcular("soma", 1.1, 2.2, 3.3, arredondar=True)
```

---

## 📌 **Escopo de Variáveis**

### 1. **Escopo Local vs Global**
```python
total = 0  # Variável global

def contador():
    global total  # Referencia a variável global
    total += 1
    x = 10  # Variável local

contador()
print(total)  # 1
# print(x)  # Erro! x não existe aqui
```

### 2. **Nonlocal (em closures)**
```python
def externa():
    x = 10
    def interna():
        nonlocal x  # Refere-se ao x da função externa
        x += 1
    interna()
    print(x)  # 11
```

---

## 📌 **Métodos vs Funções**

### 1. **Métodos de Instância**
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def cumprimentar(self):  # Método de instância
        return f"Oi, eu sou {self.nome}"

maria = Pessoa("Maria")
maria.cumprimentar()  # Chamada do método
```

### 2. **Métodos Estáticos e de Classe**
```python
class Calculadora:
    @staticmethod
    def somar(a, b):  # Não acessa classe/instância
        return a + b

    @classmethod
    def criar(cls):  # Recebe a classe como 1º arg
        return cls()
```

---

## 📌 **Funções como Objetos (First-Class Citizens)**

### 1. **Atribuindo Funções a Variáveis**
```python
def quadrado(x):
    return x ** 2

funcao = quadrado  # Sem parênteses!
print(funcao(5))  # 25
```

### 2. **Funções como Argumentos**
```python
def aplicar(funcao, valor):
    return funcao(valor)

aplicar(quadrado, 3)  # 9
```

### 3. **Funções Anônimas (`lambda`)**
```python
dobro = lambda x: x * 2
sorted([(1, 'z'), (2, 'a')], key=lambda x: x[1])  # Ordena pelo segundo item
```

---

## 📌 **Decoradores**

### 1. **Sintaxe Básica**
```python
def decorador(funcao):
    def wrapper(*args, **kwargs):
        print("Antes da execução")
        resultado = funcao(*args, **kwargs)
        print("Depois da execução")
        return resultado
    return wrapper

@decorador
def teste():
    print("Função original")

teste()
```

### 2. **Decorador com Parâmetros**
```python
def repetir(n=2):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                resultado = funcao(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(n=3)
def dizer_oi():
    print("Oi!")
```

---

## 📌 **Boas Práticas**

### 1. **Documentação (Docstrings)**
```python
def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    
    Args:
        peso (float): Peso em quilogramas
        altura (float): Altura em metros
        
    Returns:
        float: Valor do IMC arredondado
    """
    return round(peso / (altura ** 2), 2)
```

### 2. **Type Hints (Python 3.5+)**
```python
def dividir(a: float, b: float) -> float:
    """Divide dois números, retornando float."""
    return a / b
```

### 3. **Princípios SOLID para Funções**
- **Single Responsibility**: Uma função = uma tarefa
- **Open/Closed**: Aberta para extensão, fechada para modificação
- **DRY (Don't Repeat Yourself)**: Evite duplicação

---

## 🛠 **Exemplo Prático Completo**
```python
def processar_dados(
    dados: list[float], 
    *,  # Força argumentos posteriores a serem nomeados
    operacao: str = "soma",
    fator: float = 1.0
) -> float:
    """
    Processa lista de números conforme operação especificada.
    
    Operações suportadas: 'soma', 'media', 'max'
    """
    if not dados:
        raise ValueError("Lista de dados vazia")
    
    match operacao:
        case "soma":
            resultado = sum(dados) * fator
        case "media":
            resultado = (sum(dados) / len(dados)) * fator
        case "max":
            resultado = max(dados) * fator
        case _:
            raise ValueError(f"Operação inválida: {operacao}")
    
    return round(resultado, 2)

# Uso
processar_dados([1.5, 2.3, 4.1], operacao="media", fator=1.1)
```

---

## 📚 **Para Aprofundar**
- [Documentação Oficial - Funções](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- Livro "Fluent Python" - Capítulos 5 (First-Class Functions) e 7 (Function Decorators)
- PEP 484 (Type Hints): [pep-0484](https://peps.python.org/pep-0484/)
