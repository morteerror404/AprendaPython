# Bibliotecas Essenciais em Python 📚

Guia organizado por domínios de aplicação com as principais bibliotecas do ecossistema Python.

---

## 🌐 **Desenvolvimento Web**
| Biblioteca      | Descrição                          | Exemplo de Uso                     |
|-----------------|------------------------------------|------------------------------------|
| `Flask`         | Microframework para APIs           | `app = Flask(__name__)`            |
| `Django`        | Framework full-stack               | `django-admin startproject`        |
| `FastAPI`       | Framework moderno para APIs rápidas| `@app.get("/items/{item_id}")`     |
| `Requests`      | HTTP client simples                | `requests.get('https://api.com')`  |

**Exemplo FastAPI:**
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

---

## 📊 **Ciência de Dados & IA**
### 🤖 **Machine Learning**
| Biblioteca      | Foco                               | Instalação                         |
|-----------------|------------------------------------|------------------------------------|
| `scikit-learn`  | Algoritmos clássicos               | `pip install scikit-learn`         |
| `TensorFlow`    | Redes neurais (Google)             | `pip install tensorflow`           |
| `PyTorch`       | Redes neurais (Facebook)           | `pip install torch`                |

### 📈 **Análise de Dados**
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'valores': np.random.randn(100),
    'categorias': ['A', 'B', 'C'] * 33
})
print(df.describe())
```

---

## 🎨 **Visualização de Dados**
| Biblioteca      | Estilo                  | Destaque                           |
|-----------------|-------------------------|------------------------------------|
| `Matplotlib`    | Gráficos tradicionais   | `plt.plot(x, y)`                   |
| `Seaborn`       | Estatística visual      | `sns.heatmap(data)`                |
| `Plotly`        | Interatividade          | `fig = px.scatter_3d(df, x,y,z)`   |

**Exemplo Seaborn:**
```python
import seaborn as sns
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
```

---

## 🛠 **Utilitários Gerais**
### 📦 **Manipulação de Dados**
```python
# Pandas para dados tabulares
df.groupby('categoria').mean()

# NumPy para arrays numéricos
arr = np.array([[1,2], [3,4]])
```

### ⏱ **Concorrência**
```python
# Threading
import threading
thread = threading.Thread(target=funcao)

# Asyncio
import asyncio
async def main():
    await asyncio.sleep(1)
```

---

## 🗃 **Banco de Dados**
| Biblioteca      | Banco                 | Exemplo                          |
|-----------------|-----------------------|----------------------------------|
| `SQLAlchemy`    | ORM para SQL          | `session.query(User).filter_by(name='Alice')` |
| `Psycopg2`      | PostgreSQL            | `conn = psycopg2.connect(DATABASE_URL)` |
| `MongoEngine`   | MongoDB               | `class User(Document): name = StringField()` |

---

## 🔍 **Web Scraping**
```python
from bs4 import BeautifulSoup
import requests

url = "http://exemplo.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
titulos = soup.find_all('h2')
```

---

## 🚀 **Boas Práticas**
1. **Ambientes Virtuais**
   ```bash
   python -m venv meu_env
   source meu_env/bin/activate  # Linux/Mac
   meu_env\Scripts\activate     # Windows
   ```

2. **Gerenciamento de Dependências**
   ```bash
   pip freeze > requirements.txt  # Exportar
   pip install -r requirements.txt  # Importar
   ```

3. **Documentação Oficial**
   - Sempre consulte:
     - [PyPI](https://pypi.org/)
     - Documentação da biblioteca

---

## 🧩 **Extensões Recomendadas por Área**
### 🤖 **Automação**
- `selenium` - Automação de navegadores
- `pyautogui` - Controle de mouse/teclado

### 🎮 **Games**
- `pygame` - Desenvolvimento de jogos 2D

### 📡 **IoT**
- `micropython` - Python para embarcados
- `paho-mqtt` - Protocolo MQTT

---

## 🛠 **Exemplo Integrado (Análise de Dados)**
```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar dados
df = pd.read_csv("dados.csv")

# 2. Processamento
media = df.groupby('cidade')['vendas'].mean()

# 3. Visualização
media.plot(kind='barh')
plt.title("Vendas Médias por Cidade")
plt.savefig('grafico.png')
```
---
## 📚 **Recursos para Aprender**
1. [Python Package Index (PyPI)](https://pypi.org/)
2. [Awesome Python](https://github.com/vinta/awesome-python)
3. [Real Python Tutorials](https://realpython.com/)
