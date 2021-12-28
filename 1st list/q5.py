"""21.1L1Q5 - Gênero Musical"""

choice_genre: int = int(input()); choice_song: int = int(input())

# (REASON): for (a, b, c) their positions are respectively 0, 1, 2
choice_genre -= 1
choice_song -= 1

# (WHAT_IS): variable containing the song to be played and the musical genre selected
played_song: str = ""
musical_genre: str = ""

# (WHAT_IS): collections with information about available music genres and songs
if choice_genre == 0:
    musical_genre = "Rock"
    if choice_song == 0:
        played_song = "In the end - Linkin Park"
    elif choice_song == 1:
        played_song = "Californication - Red Hot Chilli Peppers"
    elif choice_song == 2:
        played_song = "Yellow - Coldplay"
elif choice_genre == 1:
    musical_genre = "Eletronica"
    if choice_song == 0:
        played_song = "Big Jet Plane - Alok & Mathieu"
    elif choice_song == 1:
        played_song = "Everyday - Marshmello & Logic"
    elif choice_song == 2:
        played_song = "On & On - Cartoon"
elif choice_genre == 2:
    musical_genre = "Hip-hop/Rap"
    if choice_song == 0:
        played_song = "Congratulations - Post Malone"
    elif choice_song == 1:
        played_song = "HIGHEST IN THE ROOM - Travis Scott"
    elif choice_song == 2:
        played_song = "Devil Eyes - Hippie Sabotage"

# (WHAT_IS): The output of results
print(f"""Você escolheu o genero: {musical_genre}
Escolha a musica
Tocando: {played_song}""")
