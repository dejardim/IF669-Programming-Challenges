"""21.1L2Q9 - Truques e Giros"""

competitors_amount: int = int(input())

player_1st: str = ""
score_1st: int = 0

player_2nd: str = ""
score_2nd: int = 0

player_3rd: str = ""
score_3rd: int = 0

EOM: str = ""  # End Of Maneuvers
score: int = 0

for i in range(competitors_amount):
    player: str = input()

    while EOM != "Fim":
        maneuver: str = input()

        if maneuver == "Gap":
            score += 10
        elif maneuver == "Barspin":
            score += 30
        elif maneuver == "Superhomem":
            score += 100
        elif maneuver == "Rotacao de 360":
            score += 50
        elif maneuver == "Rotacao de 720":
            score += 150
        elif maneuver == "Rotacao de 1080":
            score += 400
        elif maneuver == "Backflip":
            score += 250
        elif maneuver == "Frontflip":
            score += 500
        elif maneuver == "Fim":
            EOM = "Fim"

    if score > score_1st:
        # (Another way?) player_1st, player_2nd, player_3rd = player, player_2nd, player_3rd
        player_3rd = player_2nd
        player_2nd = player_1st
        player_1st = player
        #  (REASON): it's more readable that p1, p2, p3 = to, p1, p2
        score_3rd = score_2nd
        score_2nd = score_1st
        score_1st = score
    elif score > score_2nd:
        player_3rd = player_2nd
        player_2nd = player
        score_3rd = score_2nd
        score_2nd = score
    elif score > score_3rd:
        player_3rd = player
        score_3rd = score

    score = 0
    EOM = ""

print(player_1st)
print(score_1st)

print(player_2nd)
print(score_2nd)

print(player_3rd)
print(score_3rd)
