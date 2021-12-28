"""21.1L1Q2 - Quiz musical"""

song_1: str = input()
song_2: str = input()
song_3: str = input()
song_4: str = input()
song_5: str = input()

# (WHAT_IS): variable to save the correct amount of songs
correct_songs_amount: int = 0

# (WHAT_IS): conditional structure of the possibilities of song_5
if song_5 == "pelados em santos":
    correct_songs_amount += 1
elif song_5 == "mundo animal":
    correct_songs_amount += 1
elif song_5 == "robocop gay":
    correct_songs_amount += 1
elif song_5 == "vira-vira":
    correct_songs_amount += 1
elif song_5 == "1406":
    correct_songs_amount += 1

# (WHAT_IS): conditional structure of the possibilities of song_4
if song_4 == "pelados em santos":
    correct_songs_amount += 1
elif song_4 == "mundo animal":
    correct_songs_amount += 1
elif song_4 == "robocop gay":
    correct_songs_amount += 1
elif song_4 == "vira-vira":
    correct_songs_amount += 1
elif song_4 == "1406":
    correct_songs_amount += 1

# (WHAT_IS): conditional structure of the possibilities of song_3
if song_3 == "pelados em santos":
    correct_songs_amount += 1
elif song_3 == "mundo animal":
    correct_songs_amount += 1
elif song_3 == "robocop gay":
    correct_songs_amount += 1
elif song_3 == "vira-vira":
    correct_songs_amount += 1
elif song_3 == "1406":
    correct_songs_amount += 1

# (WHAT_IS): conditional structure of the possibilities of song_2
if song_2 == "pelados em santos":
    correct_songs_amount += 1
elif song_2 == "mundo animal":
    correct_songs_amount += 1
elif song_2 == "robocop gay":
    correct_songs_amount += 1
elif song_2 == "vira-vira":
    correct_songs_amount += 1
elif song_2 == "1406":
    correct_songs_amount += 1

# (WHAT_IS): conditional structure of the possibilities of song_1
if song_1 == "pelados em santos":
    correct_songs_amount += 1
elif song_1 == "mundo animal":
    correct_songs_amount += 1
elif song_1 == "robocop gay":
    correct_songs_amount += 1
elif song_1 == "vira-vira":
    correct_songs_amount += 1
elif song_1 == "1406":
    correct_songs_amount += 1

# (WHAT_IS): conditional structure to output the result
if correct_songs_amount < 2:
    print("Errou feio, errou rude: 0 pontos")
elif 2 <= correct_songs_amount <= 3:
    print("Ate que tu foi bem mas nao chegou la: 1 ponto")
elif correct_songs_amount == 4:
    print("Quase perfeito mano: 3 pontos")
elif correct_songs_amount == 5:
    print("Parabens voce e um genio conhecedor da musica brasileira, voce merece 5 pontos")
