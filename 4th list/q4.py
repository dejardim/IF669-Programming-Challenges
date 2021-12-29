"""21.1L4Q4 - Circuito Pinguim"""

def surfe_na_cacamba():
    """
    modify global variables and set the new coin balance.
    :return: None
    """

    global coin_balance
    global play_duration
    coin_balance += int((play_duration + coin_balance) / 2)


def pescaria_no_gelo():
    """
    set the new coin balance considering the parity of the old coin balance.
    :return: None
    """

    global coin_balance
    if coin_balance % 2 == 0:
        coin_balance += (coin_balance % 7) * 6
    else:
        coin_balance += (coin_balance % 7)**2


def concurso_de_danca():
    """
    set the new coin balance considering the old coin balance is multiply of 10.
    :return: None
    """

    global coin_balance
    if coin_balance % 10 == 0:
        coin_balance += 5
    else:
        while coin_balance % 10 != 0:
            coin_balance += 1


def aquagrabber():
    """
    set the new coin balance considering the old coin balance.
    :return: None
    """

    global coin_balance
    coin_balance_str: str = list(str(coin_balance))
    for value in coin_balance_str:
        coin_balance += int(value)


# Global variables
play_duration: int = 0
games_amount: int = 0
coin_balance: int = 10

while play_duration < 120:
    game_name: str = input()

    if game_name == "Surfe":
        surfe_na_cacamba()
        play_duration += 20
        games_amount += 1
        print(f"O pinguim acabou de concluir o jogo Surfe na Caçamba e agora possui {coin_balance} moedas.")
    elif game_name == "Pescaria":
        pescaria_no_gelo()
        play_duration += 30
        games_amount += 1
        print(f"O pinguim acabou de concluir o jogo Pescaria no Gelo e agora possui {coin_balance} moedas.")
    elif game_name == "Danca":
        concurso_de_danca()
        play_duration += 15
        games_amount += 1
        print(f"O pinguim acabou de concluir o jogo Concurso de Dança e agora possui {coin_balance} moedas.")
    elif game_name == "Aqua":
        aquagrabber()
        play_duration += 50
        games_amount += 1
        print(f"O pinguim acabou de concluir o jogo Aquagrabber e agora possui {coin_balance} moedas.")

print(f"\nParabens! Você terminou o Circuito Pinguim, participando de {games_amount} jogos e acumulando a " +
      f"quantia de {coin_balance} moedas.")
