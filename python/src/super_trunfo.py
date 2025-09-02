from dataclasses import dataclass

@dataclass
class Carta:
    estado: str
    codigo: str
    cidade: str
    populacao: int
    area: float
    pib: float
    pontos: int

def densidade(c: Carta) -> float:
    return (c.populacao/c.area) if c.area>0 else 0

def vencedor_por(attr:int,A:Carta,B:Carta)->int:
    if attr==1: return 0 if A.populacao==B.populacao else (-1 if A.populacao>B.populacao else 1)
    if attr==2: return 0 if A.area==B.area else (-1 if A.area>B.area else 1)
    if attr==3: return 0 if A.pib==B.pib else (-1 if A.pib>B.pib else 1)
    if attr==4: return 0 if A.pontos==B.pontos else (-1 if A.pontos>B.pontos else 1)
    if attr==5: 
        dA,dB=densidade(A),densidade(B)
        return 0 if dA==dB else (-1 if dA<dB else 1)
    return 0
