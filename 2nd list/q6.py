"""21.1L2Q6 - 100m Rasos"""

race_amount: int = int(input())

best_athlete: float = 0
tag: int = 0

total_at1: float = 0.0
total_at2: float = 0.0
total_at3: float = 0.0
total_at4: float = 0.0
total_at5: float = 0.0

for i in range(race_amount):
    athlete_1: float = float(input())
    athlete_2: float = float(input())
    athlete_3: float = float(input())
    athlete_4: float = float(input())
    athlete_5: float = float(input())

    total_at1 += athlete_1
    total_at2 += athlete_2
    total_at3 += athlete_3
    total_at4 += athlete_4
    total_at5 += athlete_5

    if athlete_1 < 9.58:
        print(f"O atleta 1 bateu o recorde mundial com o tempo: {athlete_1}")

    if athlete_2 < 9.58:
        print(f"O atleta 2 bateu o recorde mundial com o tempo: {athlete_2}")

    if athlete_3 < 9.58:
        print(f"O atleta 3 bateu o recorde mundial com o tempo: {athlete_3}")

    if athlete_4 < 9.58:
        print(f"O atleta 4 bateu o recorde mundial com o tempo: {athlete_4}")

    if athlete_5 < 9.58:
        print(f"O atleta 5 bateu o recorde mundial com o tempo: {athlete_5}")

best_athlete = total_at5

if total_at1 < best_athlete:
    best_athlete = total_at1
    tag = 1

if total_at2 < best_athlete:
    best_athlete = total_at2
    tag = 2

if total_at3 < best_athlete:
    best_athlete = total_at3
    tag = 3

if total_at4 < best_athlete:
    best_athlete = total_at4
    tag = 4

if total_at5 <= best_athlete:
    tag = 5

print(f"Vencedor com o menor tempo somando todas as baterias foi: Atleta {tag}")
