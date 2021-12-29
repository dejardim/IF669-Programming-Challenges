"""21.1L4Q3 - ONDA DE HACKER L***"""

def anticheat_check(id_numbers: str) -> bool:
    """
    Given a string (like:21897324), return bool expression if player is cheat or not

    :param id_numbers: a numeric string
    :return: boolean result if player is cheater (False) or not (True)
    """

    # characters: list = list(id_numbers)[::-1] -> readbility is not good
    # characters: list = [list(id_numbers)[n] for n in range(len(list(id_numbers)) - 1, -1, -1)] -> is not good too
    id_numbers: list = list(id_numbers)
    characters: list = []
    for i in range(len(id_numbers)-1, -1, -1):
        characters.append(id_numbers[i])

    id_sum: int = 0
    for i in range(len(characters)):
        characters[i] = int(characters[i])

        if (i+1) % 2 == 0:
            characters[i] = characters[i] * 2

        if characters[i] > 9:
            numbers = list(str(characters[i]))
            characters[i] = int(numbers[0]) + int(numbers[1])

        id_sum += characters[i]

    if id_sum % 10 == 0:
        return True
    return False


player_id: str = input()
player_id = player_id[:-2]

is_clean: bool = anticheat_check(player_id)
message: str = ""

if is_clean:  # isn't cheater
    message = f"Analisando ID: {player_id}" + "\n" + "Situacao: Jogador limpo"
else:
    message = f"Analisando ID: {player_id}" + "\n" + "Situacao: XITADO ATE OS DENTES"

print(message)
