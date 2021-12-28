"""21.1L1Q6 - Qual a Música?"""

song_genre: str = input()
is_national: str = input()
which_decade: str = input()

# (WHAT_IS): variable to store the name of found song
song: str = ""

# (WHAT_IS): conditional structure to try finding the correct song
if song_genre == "Rock":
    if is_national == "Sim":
        if which_decade == "70":
            song = "O Pirata"
        elif which_decade == "80":
            song = "Indios"
    elif is_national == "Nao":
        if which_decade == "70":
            song = "Bohemian Rapsody"
elif song_genre == "Samba":
    if is_national == "Sim":
        if which_decade == "60":
            song = "Mas que Nada"
        elif which_decade == "70":
            song = "Apesar de Voce"
        elif which_decade == "80":
            song = "Conselho"
elif song_genre == "Pop":
    if is_national == "Sim":
        if which_decade == "90":
            song = "Anna Julia"
    elif is_national == "Nao":
        if which_decade == "80":
            song = "Take On Me"
        elif which_decade == "90":
            song = "Candle in the Wind 1997"

# (WHAT_IS): conditional structure to output the result
if song:
    print(f"A musica que voce esta procurando eh: {song}")
else:
    print("Musica nao encontrada")
