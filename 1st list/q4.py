"""21.1L1Q4 - Calegario cantor"""

sentence_1: str = input(); sentence_2: str = input()
sentence_3: str = input(); sentence_4: str = input()

# (WHAT_IS): variable to count performance score
score: int = 0

# (WHAT_IS): conditional structure to check if sentence_1 is an expected sentence
if sentence_1 == "Voce errou algumas notas, mas tem potencial":
    score += score ** 0.5
elif sentence_1 == "Sua performance me deu dor de cabeca!":
    if score - 100 < 0:
        score = 0
    else:
        score -= 100
elif sentence_1 == "Sua apresentacao foi incrivel!":
    score += 200

# (WHAT_IS): conditional structure to check if sentence_2 is an expected sentence
if sentence_2 == "Voce errou algumas notas, mas tem potencial":
    score += score ** 0.5
elif sentence_2 == "Sua performance me deu dor de cabeca!":
    if score - 100 < 0:
        score = 0
    else:
        score -= 100
elif sentence_2 == "Sua apresentacao foi incrivel!":
    score += 200

# (WHAT_IS): conditional structure to check if sentence_3 is an expected sentence
if sentence_3 == "Voce errou algumas notas, mas tem potencial":
    score += score ** 0.5
elif sentence_3 == "Sua performance me deu dor de cabeca!":
    if score - 100 < 0:
        score = 0
    else:
        score -= 100
elif sentence_3 == "Sua apresentacao foi incrivel!":
    score += 200

# (WHAT_IS): conditional structure to check if sentence_4 is an expected sentence
if sentence_4 == "Voce errou algumas notas, mas tem potencial":
    score += score ** 0.5
elif sentence_4 == "Sua performance me deu dor de cabeca!":
    if score - 100 < 0:
        score = 0
    else:
        score -= 100
elif sentence_4 == "Sua apresentacao foi incrivel!":
    score += 200

# (WHAT_IS): conditional structure to output the result
if score > 150:
    print(f"Parabens! Voce atingiu a pontuacao de {score:.2f} e passou para a proxima fase!")
elif 100 <= score <= 150:
    print("Foi por pouco! Voce tem que ajustar algumas notas para alcancar a pontuacao necessaria")
elif 0 <= score < 100:
    print("A area musical nao foi feita para voce!")
