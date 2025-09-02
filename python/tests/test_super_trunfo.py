import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..','src')))
from super_trunfo import Carta,vencedor_por

def carta(p,a,pib,pt): return Carta("SP","A1","X",p,a,pib,pt)

def test_populacao():
    A=carta(2000,100,10,5); B=carta(1000,100,10,5)
    assert vencedor_por(1,A,B)==-1

def test_densidade():
    A=carta(1000,100,10,5); B=carta(1000,50,10,5)
    assert vencedor_por(5,A,B)==-1

def test_empate():
    A=carta(1000,100,10,5); B=carta(1000,100,10,5)
    for atr in [1,2,3,4,5]:
        assert vencedor_por(atr,A,B)==0
