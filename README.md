# 🃏 Desafio Super Trunfo — MateCheck  

[![Python Tests](https://github.com/Cursos-TI/desafio-logica-super-trunfo-LogicaSuperTrunfo-Gabrielcosta0f/actions/workflows/py-tests.yml/badge.svg)](https://github.com/Cursos-TI/desafio-logica-super-trunfo-LogicaSuperTrunfo-Gabrielcosta0f/actions)
[![C Tests](https://github.com/Cursos-TI/desafio-logica-super-trunfo-LogicaSuperTrunfo-Gabrielcosta0f/actions/workflows/c-tests.yml/badge.svg)](https://github.com/Cursos-TI/desafio-logica-super-trunfo-LogicaSuperTrunfo-Gabrielcosta0f/actions)

Repositório contendo as soluções do desafio **Super Trunfo - Países** em **C** e **Python**, com testes automatizados via **GitHub Actions**.

---

## 📂 Estrutura do Projeto  

```
.
├── c-niveis/                 # Implementação em C
│   └── logicaSuperTrunfo.c
│
├── python/                   # Implementação em Python
│   ├── src/
│   │   └── super_trunfo.py
│   ├── cli.py
│   ├── tests/
│   │   └── test_super_trunfo.py
│   └── requirements.txt
│
├── inputs/                   # Entradas de teste automáticas (C)
│   ├── inputs1.txt
│   └── inputs2.txt
│
├── .github/
│   └── workflows/
│       ├── py-tests.yml      # Workflow Python
│       └── c-tests.yml       # Workflow C
│
└── README.md
```

---

## 🚀 Como Executar  

### 🔹 Versão em C  
```bash
gcc c-niveis/logicaSuperTrunfo.c -o super_trunfo
./super_trunfo
```

### 🔹 Versão em Python  
```bash
cd python
pip install -r requirements.txt
python cli.py
```

---

## ✅ Como Rodar os Testes Localmente  

### Python
```bash
cd python
pytest -q
```

### C
```bash
./super_trunfo < inputs/inputs1.txt
./super_trunfo < inputs/inputs2.txt
```

---

## ⚙️ Testes Automatizados no GitHub Actions  

Este repositório executa **testes automáticos para Python e C** a cada push/PR.

### 🔹 Testes em Python
- Arquivo: `.github/workflows/py-tests.yml`
- Executa `pytest` na pasta `python/`.

### 🔹 Testes em C
- Arquivo: `.github/workflows/c-tests.yml`
- Compila `c-niveis/logicaSuperTrunfo.c` e roda contra entradas em `inputs/`.

#### Exemplo do `inputs1.txt`
```txt
SP
SP01
SaoPaulo
12000000
1521
700000000
25
RJ
RJ01
RioDeJaneiro
6700000
1200
400000000
15
1
```

📌 O último número indica o atributo de comparação:  
- `1` → População  
- `2` → Área  
- `3` → PIB  
- `4` → Pontos turísticos  
- `5` → Densidade populacional  

---

## 👨‍💻 Autor  
**Gabriel Costa**  
Curso: Introdução à Programação de Computadores – Estácio (2025)  
