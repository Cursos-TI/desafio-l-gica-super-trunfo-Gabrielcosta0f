import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from super_trunfo import *

def carta(pop, area, pib, pontos, cidade="X", uf="SP", cod="A01"):
    return Carta(uf, cod, cidade, pop, area, pib, pontos)

def test_densidade_rule_menor_vence():
    A = carta(1000, 100, 10.0, 5)   # dens 10
    B = carta(1000, 50,  10.0, 5)   # dens 20
    assert vencedor_por(5, A, B) == -1  # A vence (menor densidade)

def test_populacao_maior_vence():
    A = carta(2000, 100, 10.0, 5)
    B = carta(1000, 100, 10.0, 5)
    assert vencedor_por(1, A, B) == -1  # A vence

def test_empate_total():
    A = carta(1000, 100, 10.0, 5)
    B = carta(1000, 100, 10.0, 5)
    for atr in [1,2,3,4,5]:
        assert vencedor_por(atr, A, B) == 0
