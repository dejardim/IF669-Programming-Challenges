"""21.1L1Q8 - OS REIS DO PISEIRO"""

details_1: list = input().split(" - ")
details_2: list = input().split(" - ")
details_3: list = input().split(" - ")
details_4: list = input().split(" - ")
details_5: list = input().split(" - ")

# (WHAT_IS): Unpacking the variable "details" and convert the durations to float
song_1, singer_1, duration_1 = details_1; duration_1 = float(duration_1)
song_2, singer_2, duration_2 = details_2; duration_2 = float(duration_2)
song_3, singer_3, duration_3 = details_3; duration_3 = float(duration_3)
song_4, singer_4, duration_4 = details_4; duration_4 = float(duration_4)
song_5, singer_5, duration_5 = details_5; duration_5 = float(duration_5)

# (WHAT_IS): variables to store the total durations over all songs of these singers
ze_vaqueiro_total: float = 0.0
joao_gomes_total: float = 0.0

# (WHAT IS): conditional structure to check the singer's songs and accumulate the durations of each song
if singer_1 == "Ze vaqueiro":
    ze_vaqueiro_total += duration_1
elif singer_2 == "Ze vaqueiro":
    ze_vaqueiro_total += duration_2
elif singer_3 == "Ze vaqueiro":
    ze_vaqueiro_total += duration_3
elif singer_4 == "Ze vaqueiro":
    ze_vaqueiro_total += duration_4
elif singer_5 == "Ze vaqueiro":
    ze_vaqueiro_total += duration_5

if singer_1 == "Joao gomes":
    joao_gomes_total += duration_1
elif singer_2 == "Joao gomes":
    joao_gomes_total += duration_2
elif singer_3 == "Joao gomes":
    joao_gomes_total += duration_3
elif singer_4 == "Joao gomes":
    joao_gomes_total += duration_4
elif singer_5 == "Joao gomes":
    joao_gomes_total += duration_5

# (WHAT_IS): calculation of mean
mean_ze_vaqueiro: float = ze_vaqueiro_total / 5
mean_joao_gomes: float = joao_gomes_total / 5

# (WHAT_IS): conditional structure to output the result
if not ze_vaqueiro_total or not joao_gomes_total:
    print("Nao tivemos dados suficientes para chegar uma conclusao.")
elif mean_ze_vaqueiro == mean_joao_gomes:
    print("Tivemos um empate tecnico.")
elif mean_ze_vaqueiro > mean_joao_gomes:
    print("De acordo com estes dados temos um forte indicativo de que as musicas de Ze vaqueiro sao mais longas que "
          "as de Joao gomes.")
elif mean_ze_vaqueiro < mean_joao_gomes:
    print("De acordo com estes dados temos um forte indicativo de que as musicas de Joao gomes sao mais longas que as "
          "de Ze vaqueiro.")
