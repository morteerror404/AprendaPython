# **Documentação Completa de Orientação a Objetos em Python**  

## **📌 Introdução**  
A **Programação Orientada a Objetos (POO)** em Python permite estruturar código de forma modular, reutilizável e organizada. Este guia aborda:  

✅ **Classes e Objetos**  
✅ **Atributos e Métodos**  
✅ **Herança e Polimorfismo**  
✅ **Encapsulamento**  
✅ **Métodos Especiais**  
✅ **Classes Abstratas**  

---

## **1️⃣ Classes e Objetos**  

### **📌 Definindo uma Classe**  
```python
class Carro:
    # Atributo de classe (compartilhado entre instâncias)
    rodas = 4  

    # Método construtor (__init__)
    def __init__(self, marca, modelo, ano):
        self.marca = marca    # Atributo de instância
        self.modelo = modelo  
        self.ano = ano        
        self.ligado = False   

    # Método de instância
    def ligar(self):
        self.ligado = True
        print(f"{self.modelo} ligado!")

# Criando um objeto (instância)
meu_carro = Carro("Toyota", "Corolla", 2022)
meu_carro.ligar()  # Saída: "Corolla ligado!"
```

### **📌 Acessando Atributos**  
```python
print(meu_carro.marca)  # Toyota
print(meu_carro.rodas)  # 4 (atributo de classe)
```

---

## **2️⃣ Herança e Polimorfismo**  

### **📌 Herança Simples**  
```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("Acelerando...")

class Carro(Veiculo):  # Herda de Veiculo
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)  # Chama o construtor da classe pai
        self.portas = portas

    # Sobrescreve o método acelerar (Polimorfismo)
    def acelerar(self):
        print(f"{self.modelo} acelerando rápido!")

carro = Carro("Ford", "Mustang", 2)
carro.acelerar()  # Saída: "Mustang acelerando rápido!"
```

### **📌 Herança Múltipla**  
```python
class Motor:
    def ligar(self):
        print("Motor ligado")

class Radio:
    def tocar_musica(self):
        print("Tocando música")

class Carro(Motor, Radio):  # Herda de múltiplas classes
    pass

meu_carro = Carro()
meu_carro.ligar()        # Motor ligado
meu_carro.tocar_musica() # Tocando música
```

---

## **3️⃣ Encapsulamento (Atributos Privados)**  

### **📌 Atributos Privados (`_` e `__`)**  
```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado (__)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado.")

    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.ver_saldo())  # 1500
# print(conta.__saldo)  # Erro! Atributo privado.
```

---

## **4️⃣ Métodos Especiais (Dunder Methods)**  

### **📌 `__str__` (Representação em String)**  
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

p = Pessoa("Ana", 30)
print(p)  # Saída: "Ana, 30 anos"
```

### **📌 `__eq__` (Comparação de Objetos)**  
```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

p1 = Ponto(1, 2)
p2 = Ponto(1, 2)
print(p1 == p2)  # True (sem __eq__, seria False)
```

---

## **5️⃣ Classes Abstratas (`ABC`)**  

### **📌 Definindo uma Classe Abstrata**  
```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Classe abstrata
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

# animal = Animal()  # Erro! Não pode instanciar classe abstrata.
cachorro = Cachorro()
cachorro.emitir_som()  # Au au!
```

---

## **📌 Resumo de Conceitos**  

| **Conceito**      | **Descrição** | **Exemplo** |
|------------------|-------------|------------|
| **Classe**       | Modelo de objeto | `class Carro:` |
| **Objeto**       | Instância de uma classe | `meu_carro = Carro()` |
| **Herança**      | Reutilizar código de outra classe | `class Carro(Veiculo):` |
| **Polimorfismo** | Sobrescrever métodos | `def acelerar(self):` |
| **Encapsulamento** | Proteger atributos | `self.__saldo` |
| **Métodos Mágicos** | Comportamento especial | `__str__`, `__eq__` |
| **Classe Abstrata** | Define métodos obrigatórios | `@abstractmethod` |

---

## **📚 Exemplo Completo**  

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco * (1 - percentual / 100)

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def __str__(self):
        return f"Livro: {self.nome} ({self.autor}), R${self.preco}"

livro = Livro("Python Essentials", 100, "João Silva")
print(livro)  # Saída: "Livro: Python Essentials (João Silva), R$100"
print(f"Preço com 10% de desconto: R${livro.desconto(10):.2f}")
```

---

## **🚀 Conclusão**  
A **POO em Python** permite criar sistemas robustos e organizados. Pratique com:  
✅ **Classes e objetos**  
✅ **Herança e polimorfismo**  
✅ **Encapsulamento**  
✅ **Métodos especiais**  

Quer aprofundar em algum tópico específico? Comente abaixo! 🚀