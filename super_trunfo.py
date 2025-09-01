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
    return (c.populacao / c.area) if c.area > 0 else 0.0

# Retorna -1 se A vence, 1 se B vence, 0 empate
def vencedor_por(atributo: int, A: Carta, B: Carta) -> int:
    if atributo == 1:  # População (maior vence)
        return 0 if A.populacao == B.populacao else (-1 if A.populacao > B.populacao else 1)
    if atributo == 2:  # Área (maior vence)
        return 0 if A.area == B.area else (-1 if A.area > B.area else 1)
    if atributo == 3:  # PIB (maior vence)
        return 0 if A.pib == B.pib else (-1 if A.pib > B.pib else 1)
    if atributo == 4:  # Pontos turísticos (maior vence)
        return 0 if A.pontos == B.pontos else (-1 if A.pontos > B.pontos else 1)
    if atributo == 5:  # Densidade (menor vence)
        dA, dB = densidade(A), densidade(B)
        return 0 if dA == dB else (-1 if dA < dB else 1)
    return 0

def atributo_nome(a: int) -> str:
    return {1:"População",2:"Área",3:"PIB",4:"Pontos turísticos",5:"Densidade"}.get(a,"Atributo")

def formata_carta(c: Carta) -> str:
    return f"[{c.estado}/{c.codigo}] {c.cidade} | Pop: {c.populacao} | Área: {c.area:.2f} | PIB: {c.pib:.2f} | Pontos: {c.pontos} | Dens.: {densidade(c):.2f}"
