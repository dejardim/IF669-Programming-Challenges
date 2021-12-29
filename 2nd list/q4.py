"""21.1L1Q4 - A Luta Final"""

player: int = 100
logan_paul: int = 100

on_fight_cycle: bool = True
cycle: int = 1

attack = int(input())
defense = int(input())

while on_fight_cycle:

    if cycle % 2 == 1:
        if 0 < (attack - defense) <= 20:
            player = player - (attack - defense)
        elif (attack - defense) > 20:
            player = player - int(1.5 * (attack - defense))
        elif (defense - attack) > 20:
            logan_paul = logan_paul - (defense - attack)
    else:
        if 0 < (attack - defense) <= 20:
            logan_paul = logan_paul - (attack - defense)
        elif (attack - defense) > 20:
            logan_paul = logan_paul - int(1.5 * (attack - defense))
        elif (defense - attack) > 20:
            player = player - (defense - attack)

    cycle += 1

    if player <= 0 or logan_paul <= 0:
        on_fight_cycle = False
    else:
        attack = int(input())
        defense = int(input())

if player > 0:
    print("Apos longos anos de esforco voce finalmente conseguiu, e ouro pro Brasil!")
elif logan_paul >0:
    print("Infelizmente nao foi dessa vez, Logan Paul leva a vitoria.")
