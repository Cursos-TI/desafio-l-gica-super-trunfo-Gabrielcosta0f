# 🃏 Desafio Super Trunfo — MateCheck

[![Python Tests](https://github.com/Cursos-TI/desafio-logica-super-trunfo-LogicaSuperTrunfo-Gabrielcosta0f/actions/workflows/py-tests.yml/badge.svg)](https://github.com/Cursos-TI/desafio-logica-super-trunfo-LogicaSuperTrunfo-Gabrielcosta0f/actions)

Implementação do desafio **Super Trunfo - Países** em **C** e **Python**.

## Estrutura
- `c-niveis/logicaSuperTrunfo.c` → versão em C
- `python/src/super_trunfo.py` → funções em Python
- `python/cli.py` → interface de linha de comando Python
- `python/tests/test_super_trunfo.py` → testes automatizados
- `.github/workflows/py-tests.yml` → CI no GitHub Actions

## Como rodar

### C
```bash
gcc c-niveis/logicaSuperTrunfo.c -o supertrunfo
./supertrunfo
```

### Python
```bash
cd python
pip install -r requirements.txt
python cli.py
```

### Testes
```bash
cd python
pytest -q
```

---
Autor: Gabriel Costa • Estácio 2025
