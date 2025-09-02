# Desafio Super Trunfo — Países 🌍

Este repositório contém as soluções do desafio **Super Trunfo - Países**, com implementação em **C** e **Python**.  
O objetivo é criar um sistema de **comparação de cartas** (cidades/países) utilizando estruturas de decisão, repetição e funções.

---

## 📌 Estrutura do Projeto

```
.
├── c-niveis/               # Código-fonte em C
│   └── logicaSuperTrunfo.c
│
├── python/                 
│   ├── src/                # Código principal em Python
│   │   └── super_trunfo.py
│   ├── tests/              # Testes automáticos
│   │   └── test_super_trunfo.py
│   └── requirements.txt    # Dependências do Python
│
├── .github/workflows/      # Integração contínua (GitHub Actions)
│   └── py-tests.yml
│
└── README.md               # Documentação do projeto
```

---

## 🏅 Desafios

### 🔹 Nível Novato
- Cadastro de cartas (estado, código, cidade, população, área, PIB, pontos turísticos).
- Comparação de dois atributos (ex.: população, área).
- Exibição da carta vencedora.

### 🔹 Nível Aventureiro
- Inclusão de **menu interativo** (escolha do atributo).
- Comparações aninhadas usando `if` e `switch`.
- Saídas organizadas com a explicação do critério de vitória.

### 🔹 Nível Mestre
- Escolha de **dois atributos simultâneos**.
- Uso de **operadores ternários** e lógicas avançadas.
- Tratamento de **empates**.

---

## ▶️ Como Executar

### 🔹 Em C
```bash
cd c-niveis
gcc logicaSuperTrunfo.c -o supertrunfo
./supertrunfo
```

### 🔹 Em Python
```bash
cd python
pip install -r requirements.txt
python src/cli.py
```

### 🔹 Rodando os testes
```bash
pytest -q
```

---

## ✅ Funcionalidades
- Cadastro interativo das cartas.
- Comparação clara entre atributos.
- Definição automática da carta vencedora.
- Estrutura de código documentada e modular.

---

## 👨‍💻 Autor
**Gabriel Costa**  
Desafios de Lógica de Programação — Estácio • 2025
