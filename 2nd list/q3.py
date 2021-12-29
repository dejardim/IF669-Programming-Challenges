"""21.1L2Q3 - Skate street"""

laps_amount: int = int(input())

total_score: int = 0
best_score: int = 0

for i in range(laps_amount):
    score_1 = int(input())
    score_2 = int(input())
    score_3 = int(input())
    score_4 = int(input())
    score_5 = int(input())

    total_score += score_1 + score_2 + score_3 + score_4 + score_5

    if i == 0:  # (REASON): In first moment the first total_score is the best_score
        best_score = total_score

    if total_score > best_score:
        best_score = total_score

    print(f"A pontuacao na volta {i + 1} foi de {total_score} pontos!")

    total_score = 0  # (REASON): Reset the value to the next loop iteration 

print(f"A pontuacao final de Rayssa foi de {best_score} pontos!")
