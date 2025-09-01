from super_trunfo import *

def ler_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("Valor inválido. Tente novamente.")

def ler_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Tente novamente.")

def ler_token(msg: str, maxlen: int) -> str:
    while True:
        s = input(msg).strip()
        if 0 < len(s) <= maxlen:
            return s
        print("Texto inválido.")

def ler_carta_guiada(titulo: str) -> Carta:
    print(f"\n=== Cadastro da carta {titulo} ===")
    uf = ler_token("UF (2 letras, ex.: SP): ", 2)
    codigo = ler_token("Código (ex.: A01): ", 7)
    cidade = ler_token("Cidade (sem espaços, ex.: Sao_Paulo): ", 63)
    pop = ler_int("População (habitantes): ")
    area = ler_float("Área (km2): ")
    pib = ler_float("PIB (bilhões): ")
    pontos = ler_int("Nº de pontos turísticos: ")
    return Carta(uf, codigo, cidade, pop, area, pib, pontos)

def imprime_duas_cartas(A: Carta, B: Carta):
    print("\n--- Cartas cadastradas ---")
    print(formata_carta(A))
    print(formata_carta(B))

def novato(A: Carta, B: Carta, ATRIBUTO: int = 1):
    imprime_duas_cartas(A, B)
    print(f"\nComparando pelo atributo {ATRIBUTO} ({atributo_nome(ATRIBUTO)})...")
    v = vencedor_por(ATRIBUTO, A, B)
    if v == -1: print(f"Vencedora: A ({A.cidade})")
    elif v == 1: print(f"Vencedora: B ({B.cidade})")
    else: print("Empate!")

def aventureiro(A: Carta, B: Carta):
    imprime_duas_cartas(A, B)
    print("\nMenu de comparação:")
    print("1) População (maior)")
    print("2) Área (maior)")
    print("3) PIB (maior)")
    print("4) Pontos turísticos (maior)")
    print("5) Densidade (menor)")
    op = ler_int("Escolha o atributo (1-5): ")
    if op < 1 or op > 5:
        print("Opção inválida."); return
    v = vencedor_por(op, A, B)
    if v != 0:
        ganhador = "A" if v == -1 else "B"
        print(f"Vencedora: {ganhador} ({atributo_nome(op)})")
    else:
        # desempates aninhados (exemplo simples): usa PIB, depois Área
        print("Empate! Desempate por PIB...")
        v = vencedor_por(3, A, B)
        if v == 0:
            print("Permanece empate. Desempate por Área...")
            v = vencedor_por(2, A, B)
        if v == 0: print("Empate total!")
        else:
            ganhador = "A" if v == -1 else "B"
            print(f"Vencedora: {ganhador} (desempate)")

def mestre(A: Carta, B: Carta):
    imprime_duas_cartas(A, B)
    while True:
        print("\nAtributos: 1) Pop  2) Área  3) PIB  4) Pontos  5) Densidade  |  0) Sair")
        a1 = ler_int("1º atributo (0 para sair): ")
        if a1 == 0: break
        a2 = ler_int("2º atributo (desempate): ")
        v = vencedor_por(a1, A, B)
        v = v if v != 0 else vencedor_por(a2, A, B)  # "ternário" na prática
        rotulo = atributo_nome(a1)
        if v == -1: print(f"\nComparação por {rotulo} → Vencedora: A ({A.cidade})")
        elif v == 1: print(f"\nComparação por {rotulo} → Vencedora: B ({B.cidade})")
        else: print(f"\nComparação por {rotulo} → Empate!")

def main():
    print("Super Trunfo — Python (Novato/Aventureiro/Mestre)")
    while True:
        print("\n[1] Novato  [2] Aventureiro  [3] Mestre  [0] Sair")
        op = ler_int("Escolha: ")
        if op == 0: break
        A = ler_carta_guiada("A")
        B = ler_carta_guiada("B")
        if op == 1:
            atr = ler_int("ATRIBUTO (1-5) para o modo Novato: ")
            novato(A, B, atr if 1 <= atr <= 5 else 1)
        elif op == 2:
            aventureiro(A, B)
        elif op == 3:
            mestre(A, B)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
