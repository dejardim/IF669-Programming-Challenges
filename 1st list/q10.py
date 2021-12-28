"""21.1L1Q10 - Michael - O Retorno"""

song_name: str = input()
new_followers_michel: float = int(input())
new_followers_raffa: float = int(input())

setence_1: str = input()
setence_2: str = input()
setence_3: str = input()

expected_followers: int = int(new_followers_michel + new_followers_raffa)

if setence_1 == "Gang Gang Bro!":
    new_followers_raffa = new_followers_raffa * 1.25
elif setence_1 == "Hihiiiii UuHuu, 777 Bro!":
    new_followers_raffa = new_followers_raffa * 1.20
    new_followers_michel = new_followers_michel * 1.15
elif setence_1 == "Ayouwoki, ayouwoki, ayouwoki":
    new_followers_raffa = new_followers_raffa * 0.7
    new_followers_michel = new_followers_michel * 0.75

if setence_2 == "Gang Gang Bro!":
    new_followers_raffa = new_followers_raffa * 1.25
elif setence_2 == "Hihiiiii UuHuu, 777 Bro!":
    new_followers_raffa = new_followers_raffa * 1.20
    new_followers_michel = (new_followers_michel * 1.15)
elif setence_2 == "Ayouwoki, ayouwoki, ayouwoki":
    new_followers_raffa = (new_followers_raffa * 0.7)
    new_followers_michel = (new_followers_michel * 0.75)

if setence_3 == "Gang Gang Bro!":
    new_followers_raffa = new_followers_raffa * 1.25
elif setence_3 == "Hihiiiii UuHuu, 777 Bro!":
    new_followers_raffa = new_followers_raffa * 1.20
    new_followers_michel = new_followers_michel * 1.15
elif setence_3 == "Ayouwoki, ayouwoki, ayouwoki":
    new_followers_raffa = new_followers_raffa * 0.75
    new_followers_michel = new_followers_michel * 0.7

calculated_followers: int = int(new_followers_michel + new_followers_raffa)
percent: float = (calculated_followers * 100) / expected_followers

print(f"""Então Michael, eu trouxe os seguintes resultados da música...
Nome da Música: {song_name.upper()}
Número de Seguidores Esperados: {expected_followers}
Número de Seguidores Calculados: {calculated_followers}
Resultado: {percent:.2f}%
""")

if calculated_followers > expected_followers:
    print("E felizmente... BROOO! faz sol! Camisa do Rusbé vai vender!")
else:
    print("Rockstar e fé em Deus bro! Que vocês irão pensar em frases melhores...")
