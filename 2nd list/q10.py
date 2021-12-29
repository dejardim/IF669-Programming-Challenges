"""21.1L2Q10 - Jogo de vôlei"""

matches_amount: int = int(input())

on_volleyball_match: bool = False

for i in range(matches_amount):
    s: int = int(input())
    l: int = int(input())
    attacker: str = input()
    server: str = input()

    calc_s = s ** 3
    calc_l = int(l ** (1 / 3))

    if calc_s % 3 == 0:
        print(f"AAAAACE! ELE MESMO, {server}! UMA FERA! UMA BESTA ENJAULADA!")
        on_volleyball_match = False
    elif calc_s % 2 == 0:
        print(f"Saque pra fora do {server}, que desperdicio de uma bela oportunidade!!!")
        on_volleyball_match = False
    elif calc_s % 2 == 1:
        print(f"Bom saque do {server}, bola em jogo!")
        on_volleyball_match = True

    while on_volleyball_match:
        if calc_l % 2 == 1:
            print(f"Levantamento rápido com maestria no meio para o {attacker} finalizar")
        else:
            print(f"Levantamento longo na lateral para o {attacker} finalizar")

        if s >= l:
            print("NÃO! NÃO É ASSIM...")
            break
        else:
            print(f"Bom ataque do {attacker}! momento decisivo!")

        if (s + l) % 2 == 0:
            print("A bola volta para o campo do Brasil, recomeça o lance!")
        else:
            print("É DO BRASIL!!!!")
            on_volleyball_match = False

        if on_volleyball_match:
            s: int = int(input())
            l: int = int(input())
            attacker: str = input()

            calc_s = s ** 3
            calc_l = int(l ** (1 / 3))
