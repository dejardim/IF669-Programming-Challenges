"""21.1L1Q9 - Caio's Rhythm Game"""

#
invalid_move: int = 0
invalid_input: int = 0
valid_move: int = 0

#
move_1: str = input()

if move_1 == "baixo":
    valid_move += 1
elif move_1 == "cima":
    valid_move += 1
elif move_1 == "esquerda":
    valid_move += 1
elif move_1 == "direita":
    valid_move += 1
else:
    invalid_input += 1

#
if not invalid_input:
    move_2 = input()

    if move_1 == move_2:
        invalid_move += 1
    elif (move_1 == "baixo" and move_2 == "cima") or (move_1 == "cima" and move_2 == "baixo"):
        invalid_move += 1
    elif (move_1 == "esquerda" and move_2 == "direita") or (move_1 == "direita" and move_2 == "esquerda"):
        invalid_move += 1
    elif (move_2 == "baixo" or move_2 == "cima" or move_2 == "esquerda" or move_2 == "direita") and not invalid_move:
        if not invalid_input:
            valid_move += 1
    else:
        invalid_input += 1

#
if not invalid_input and not invalid_move:
    move_3 = input()

    if move_2 == move_3:
        invalid_move += 1
    elif (move_2 == "baixo" and move_3 == "cima") or (move_2 == "cima" and move_3 == "baixo"):
        invalid_move += 1
    elif (move_2 == "esquerda" and move_3 == "direita") or (move_2 == "direita" and move_3 == "esquerda"):
        invalid_move += 1
    elif (move_3 == "baixo" or move_3 == "cima" or move_3 == "esquerda" or move_3 == "direita") and not invalid_move:
        if not invalid_input:
            valid_move += 1
    else:
        invalid_input += 1

#
if not invalid_input and not invalid_move:
    move_4 = input()

    if move_3 == move_4:
        invalid_move += 1
    elif (move_3 == "baixo" and move_4 == "cima") or (move_3 == "cima" and move_4 == "baixo") :
        invalid_move += 1
    elif (move_3 == "esquerda" and move_4 == "direita") or (move_3 == "direita" and move_4 == "esquerda"):
        invalid_move += 1
    elif (move_4 == "baixo" or move_4 == "cima" or move_4 == "esquerda" or move_4 == "direita") and not invalid_move:
        if not invalid_input:
            valid_move += 1
    else:
        invalid_input += 1

#
if not invalid_input and not invalid_move:
    move_5 = input()

    if move_4 == move_5:
        invalid_move += 1
    elif (move_4 == "baixo" and move_5 == "cima") or (move_4 == "cima" and move_5 == "baixo"):
        invalid_move += 1
    elif (move_4 == "esquerda" and move_5 == "direita") or (move_4 == "direita" and move_5 == "esquerda"):
        invalid_move += 1
    elif (move_5 == "baixo" or move_5 == "cima" or move_5 == "esquerda" or move_5 == "direita") and not invalid_move:
        if not invalid_input:
            valid_move += 1
    else:
        invalid_input += 1

#
if not valid_move and (invalid_move or invalid_input):
    print("O jogador nao fez nenhuma entrada valida")
elif invalid_input and valid_move:
    print(f"O jogador fez {valid_move} movimento(s) e tentou uma entrada invalida")
elif valid_move and invalid_move:
    print(f"O jogador fez somente {valid_move} movimento(s)")
elif valid_move and not invalid_move:
    print("O jogador conseguiu fazer todos 5 movimentos com sucesso!")
