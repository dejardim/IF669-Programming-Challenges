"""21.1L2Q1 - Os treinos de Richarlison"""

player: str = input()
workouts_per_day: int = int(input()) - 1  # (REASON): in line 4, the computer catch one of values

workout_score: int = int(input())

# (WHAT_IS): at first, there is no better or worse score, because they have the same value
best_score: int = workout_score
worst_score: int = workout_score

for i in range(workouts_per_day):
    workout_score: int = int(input())

    if best_score < workout_score:
        best_score = workout_score
    elif worst_score > workout_score:
        worst_score = workout_score

print(f"Belo dia de treinos, {player}! Hoje o seu melhor desempenho foi de {best_score} gols e o pior foi de {worst_score} gols. Rumo ao Ouro!")
