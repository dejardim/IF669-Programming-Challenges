"""21.1L3Q8 - Gente nova no Comando?"""

present_people: int = int(input())

voters: list = []
delegates: list = []
selections: list = []

for i in range(present_people):
    line: str = input()
    voter, delegate = line.split(": ")

    if voter not in voters:
        voters.append(voter)
        selections.append(delegate)
    if delegate not in delegates:
        delegates.append(delegate)

results: list = []
shelby_amount: int = 0

for delegate in delegates:
    count: int = 0
    is_shelby: bool = False
    percent: float = 0
    for selection in selections:
        if delegate == selection:
            count += 1
    if "Shelby" in delegate:
        is_shelby = True
        shelby_amount += 1
    percent = (count / len(selections)) * 100
    result: list = [percent, delegate, is_shelby]
    results.append(result)

for i in range(len(results) - 1):
    for j in range(len(results) - 1):
        if results[j][0] < results[j+1][0]:
            aux: list = results[j]
            results[j] = results[j+1]
            results[j+1] = aux

has_not_winner: bool = True

if results[0][2]:
    if results[0][0] > 50:
        if results[0][1] == "Thomas Shelby":
            print(f"{results[0][1]} ganhou a eleição com {results[0][0]:.2f}% dos votos e " +
                  "continuara sendo o líder dos Peaky Blinders!!!")
            has_not_winner = False
        else:
            print(f"Assumindo o lugar de Tommy, {results[0][1]} agora é o novo líder da gangue " +
                  f"vencendo a eleição com {results[0][0]:.2f}% dos votos!")
            has_not_winner = False

if shelby_amount > 1 and has_not_winner:
    second_round_delegates: list = []

    for person in results:
        if len(second_round_delegates) == 2:
            break
        elif person[2]:
            second_round_delegates.append(person)

    if "Thomas Shelby" == second_round_delegates[0][1] or "Thomas Shelby" == second_round_delegates[1][1]:
        print(f"Precisaremos ter uma segunda rodada entre os membros {second_round_delegates[0][1]} e " +
              f"{second_round_delegates[1][1]}, que tiveram respectivamente " +
              f"{second_round_delegates[0][0]:.2f}% e {second_round_delegates[1][0]:.2f}% dos votos, " +
              "Tommy ainda está na disputa.")
    else:
        print(f"Precisaremos ter uma segunda rodada entre os membros {second_round_delegates[0][1]} e " +
              f"{second_round_delegates[1][1]}, que tiveram respectivamente " +
              f"{second_round_delegates[0][0]:.2f}% e {second_round_delegates[1][0]:.2f}% dos votos, " +
              "teremos um novo líder!")
elif has_not_winner:
    print("Algo histórico aconteceu aqui hoje, é uma revolta contra os Shelby!")
