# Super Trunfo — Versão Python (CLI + Testes)

Este módulo implementa o desafio **Super Trunfo – Países/Cidades** em **Python**, com:
- **Funções puras** para comparação de cartas (testáveis)
- **CLI interativo** para os três níveis (Novato, Aventureiro e Mestre)
- **Testes automatizados** com `pytest`
- **GitHub Actions** para rodar testes a cada push

## 📂 Estrutura
```
python/
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ super_trunfo.py   # funções puras (comparação, densidade, utilidades)
│  └─ cli.py            # menu interativo (3 modos: Novato, Aventureiro, Mestre)
└─ tests/
   └─ test_super_trunfo.py
```

## ▶️ Como rodar
```bash
cd python
pip install -r requirements.txt
python src/cli.py
```

### Modos do CLI
- **1 — Novato:** atributo fixo (definido no código) → maior vence, exceto densidade (menor vence)
- **2 — Aventureiro:** menu para escolher 1 atributo; empate resolve com um segundo critério
- **3 — Mestre:** escolha de **2 atributos** (principal + desempate), repete até sair
- **0 — Sair**

> Atributos (1–5): 1=População, 2=Área, 3=PIB, 4=Pontos turísticos, 5=Densidade (menor vence).

## 🧪 Testes
```bash
cd python
pytest -q
```

## ⚙️ CI
O workflow em `.github/workflows/py-tests.yml` roda os testes da pasta `python/` a cada push/PR.
