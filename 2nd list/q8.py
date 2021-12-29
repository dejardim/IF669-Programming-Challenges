"""21.1L2Q8 - Partida de Tênis"""

on_game_match: bool = True

djoko_score: int = 0
federer_score: int = 0

while on_game_match:
    player: str = input()

    if player == "djoko":
        djoko_score += 1

    if player == "federer":
        federer_score += 1

    if djoko_score >= 3 and federer_score >= 3:
        if djoko_score - federer_score == 2:
            print(f"Djokovic ganhou o game com a pontuacao de {djoko_score} a {federer_score}!")
            on_game_match = False

        if federer_score - djoko_score == 2:
            print(f"Roger federer ganhou o game com a pontuacao de {federer_score} a {djoko_score}!")
            on_game_match = False
    else:
        if djoko_score > 0 and djoko_score % 4 == 0:
            print(f"Djokovic ganhou o game com a pontuacao de {djoko_score} a {federer_score}!")
            on_game_match = False

        if federer_score > 0 and federer_score % 4 == 0:
            print(f"Roger federer ganhou o game com a pontuacao de {federer_score} a {djoko_score}!")
            on_game_match = False
