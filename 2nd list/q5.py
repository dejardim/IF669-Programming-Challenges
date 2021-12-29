"""21.1L2Q5 - Levantamento de peso"""

competitor_energy_1: int = int(input())
competitor_weight_1: int = int(input())

competitor_energy_2: int = int(input())
competitor_weight_2: int = int(input())

competitor_energy_3: int = int(input())
competitor_weight_3: int = int(input())

for i in range(3):
    c1_weight: float = float(input())
    c2_weight: float = float(input())
    c3_weight: float = float(input())

    energy_spent: float = c1_weight / competitor_weight_1
    competitor_energy_1 -= energy_spent

    energy_spent: float = c2_weight / competitor_weight_2
    competitor_energy_2 -= energy_spent

    energy_spent: float = c3_weight / competitor_weight_3
    competitor_energy_3 -= energy_spent

passed_out: int = 0

c1_out: bool = False
c2_out: bool = False
c3_out: bool = False

if competitor_energy_1 < 0:
    print("O competidor 1, desmaiou")
    c1_out = True
    passed_out += 1

if competitor_energy_2 < 0:
    print("O competidor 2, desmaiou")
    c2_out = True
    passed_out += 1

if competitor_energy_3 < 0:
    print("O competidor 3, desmaiou")
    c3_out = True
    passed_out += 1

# (NOTE): after trying, trying and trying... i found a elegant way to code the conditionals of problem.
#         (!): it is important to remember that restricted expressions must be written first than others.

if competitor_energy_3 > competitor_energy_2 and competitor_energy_3 > competitor_energy_1:
    if competitor_energy_2 > competitor_energy_1 > 0:
        print("O vencedor foi o competidor 1")
    elif competitor_energy_1 > competitor_energy_2 > 0:
        print("O vencedor foi o competidor 2")
    elif c2_out and c1_out:  # (!) 
        print("O vencedor foi o competidor 3")
    elif c2_out:
        print("O vencedor foi o competidor 1")
    elif c1_out:
        print("O vencedor foi o competidor 2")

if competitor_energy_2 > competitor_energy_3 and competitor_energy_2 > competitor_energy_1:
    if competitor_energy_3 > competitor_energy_1 > 0:
        print("O vencedor foi o competidor 1")
    elif competitor_energy_1 > competitor_energy_3 > 0:
        print("O vencedor foi o competidor 3")
    elif c3_out and c1_out:  # (!)
        print("O vencedor foi o competidor 2")
    elif c3_out:
        print("O vencedor foi o competidor 1")
    elif c1_out:
        print("O vencedor foi o competidor 3")

if competitor_energy_1 > competitor_energy_2 and competitor_energy_1 > competitor_energy_3:
    if competitor_energy_3 > competitor_energy_2 > 0:
        print("O vencedor foi o competidor 2")
    elif competitor_energy_2 > competitor_energy_3 > 0:
        print("O vencedor foi o competidor 3")
    elif c3_out and c2_out:  # (!)
        print("O vencedor foi o competidor 1")
    elif c3_out:
        print("O vencedor foi o competidor 2")
    elif c2_out:
        print("O vencedor foi o competidor 3")

if passed_out == 3:
    print("Todos os competidores desmaiaram")
