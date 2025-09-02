from super_trunfo import *

def ler_int(msg):
    while True:
        try: return int(input(msg))
        except: print("Inválido")

def ler_float(msg):
    while True:
        try: return float(input(msg).replace(",", "."))
        except: print("Inválido")

def ler_str(msg,maxlen):
    while True:
        s=input(msg).strip()
        if 0<len(s)<=maxlen: return s
        print("Inválido")

def ler_carta(t):
    print(f"\n=== Carta {t} ===")
    return Carta(
        estado=ler_str("UF: ",2),
        codigo=ler_str("Código: ",7),
        cidade=ler_str("Cidade: ",63),
        populacao=ler_int("População: "),
        area=ler_float("Área: "),
        pib=ler_float("PIB: "),
        pontos=ler_int("Pontos turísticos: ")
    )

def main():
    print("Super Trunfo — Python")
    A=ler_carta("A")
    B=ler_carta("B")
    print("\n1=População 2=Área 3=PIB 4=Pontos 5=Densidade")
    atr=ler_int("Escolha atributo: ")
    v=vencedor_por(atr,A,B)
    if v==0: print("Empate!")
    elif v==-1: print(f"Vencedora: A ({A.cidade})")
    else: print(f"Vencedora: B ({B.cidade})")

if __name__=="__main__":
    main()
