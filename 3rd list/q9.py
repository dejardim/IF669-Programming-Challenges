"""21.1L3Q9 - Vista de Nova Iorque"""

incidents_amount: int = int(input())

mike_incidents: list = []; mike_score: int = 0; mmax_score: int = 0
louis_incidents: list = []; louis_score: int = 0; lmax_score: int = 0
harvey_incidents: list = []; harvey_score: int = 0; hmax_score: int = 0

for i in range(incidents_amount):
    line: str = input()
    name, incident_type, score = line.split()
    if name == "Mike":
        mike_incidents.append(incident_type)
        mike_score += int(score)
        if int(score) > mmax_score:
            mmax_score = int(score)
    elif name == "Louis":
        louis_incidents.append(incident_type)
        louis_score += int(score)
        if int(score) > lmax_score:
            lmax_score = int(score)
    elif name == "Harvey":
        harvey_incidents.append(incident_type)
        harvey_score += int(score)
        if int(score) > hmax_score:
            hmax_score = int(score)

mike_mean: float = mike_score / len(mike_incidents)
louis_mean: float = louis_score / len(louis_incidents)
harvey_mean: float = harvey_score / len(harvey_incidents)

means = [[mike_mean, "Mike", mike_incidents.count('pro-bono'), mmax_score],
         [louis_mean, "Louis", louis_incidents.count('pro-bono'), lmax_score],
         [harvey_mean, "Harvey", harvey_incidents.count('pro-bono'), hmax_score]]

sorted_means = [[mike_mean, "Mike", mike_incidents.count('pro-bono'), mmax_score],
                [louis_mean, "Louis", louis_incidents.count('pro-bono'), lmax_score],
                [harvey_mean, "Harvey", harvey_incidents.count('pro-bono'), hmax_score]]

for i in range(len(sorted_means) - 1):
    for j in range(len(sorted_means) - 1):
        if sorted_means[j][0] < sorted_means[j + 1][0]:
            sorted_means[j], sorted_means[j + 1] = sorted_means[j + 1], sorted_means[j]

for i in range(3):
    print(f"{means[i][1]};\nMédia: {means[i][0]:.2f}\nQuantidade de Pró-bonos: {means[i][2]}\nMáximo: {means[i][3]}\n")

message: str = ""

if sorted_means[0][0] > sorted_means[2][0]:
    if sorted_means[0][0] == sorted_means[1][0] and sorted_means[1][0] > sorted_means[2][0]:
        if sorted_means[0][2] > sorted_means[1][2]:
            message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                      f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
        elif sorted_means[0][2] < sorted_means[1][2]:
            message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                      f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
        elif sorted_means[0][2] == sorted_means[1][2]:
            if sorted_means[0][3] > sorted_means[1][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
            elif sorted_means[0][3] > sorted_means[1][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
            elif sorted_means[0][3] == sorted_means[1][3]:
                if sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
    elif sorted_means[1][0] > sorted_means[2][0]:
        message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                  f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
    elif sorted_means[1][0] == sorted_means[2][0]:
        if sorted_means[1][2] > sorted_means[2][2]:
            message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                      f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
        elif sorted_means[1][2] < sorted_means[2][2]:
            message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                      f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
        elif sorted_means[1][2] == sorted_means[2][2]:
            if sorted_means[1][3] > sorted_means[2][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
            elif sorted_means[1][3] < sorted_means[2][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
            elif sorted_means[1][3] == sorted_means[2][3]:
                if sorted_means[1][1] == "Mike" and sorted_means[2][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[1][1] == "Mike" and sorted_means[2][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[1][1] == "Louis" and sorted_means[2][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[1][1] == "Louis" and sorted_means[2][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[1][1] == "Harvey" and sorted_means[2][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[1][1] == "Harvey" and sorted_means[2][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
else:

    for i in range(len(sorted_means) - 1):
        for j in range(len(sorted_means) - 1):
            if sorted_means[j][2] < sorted_means[j+1][2]:
                sorted_means[j], sorted_means[j+1] = sorted_means[j+1], sorted_means[j]

    if sorted_means[0][2] > sorted_means[2][2]:
        if sorted_means[0][2] == sorted_means[1][2] and sorted_means[1][2] > sorted_means[2][2]:
            if sorted_means[0][3] > sorted_means[1][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
            elif sorted_means[0][3] < sorted_means[1][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
            elif sorted_means[0][3] == sorted_means[1][3]:
                if sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
        elif sorted_means[1][2] > sorted_means[2][2]:
            message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                      f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
        elif sorted_means[1][2] < sorted_means[2][2]:
            message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                      f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
        elif sorted_means[1][2] == sorted_means[2][2]:
            if sorted_means[1][3] > sorted_means[2][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
            elif sorted_means[1][3] < sorted_means[2][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
            elif sorted_means[1][3] == sorted_means[2][3]:
                if sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
    else:

        for i in range(len(sorted_means) - 1):
            for j in range(len(sorted_means) - 1):
                if sorted_means[j][3] < sorted_means[j+1][3]:
                    sorted_means[j], sorted_means[j+1] = sorted_means[j+1], sorted_means[j]

        if sorted_means[0][3] > sorted_means[2][3]:
            if sorted_means[0][3] == sorted_means[1][3] and sorted_means[1][3] > sorted_means[2][3]:
                if sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
            elif sorted_means[1][3] > sorted_means[2][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
            elif sorted_means[1][3] < sorted_means[2][3]:
                message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                          f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
            elif sorted_means[1][3] == sorted_means[2][3]:
                if sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Mike" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Louis" and sorted_means[1][1] == "Harvey":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[0][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[2][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Mike":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
                elif sorted_means[0][1] == "Harvey" and sorted_means[1][1] == "Louis":
                    message = f"Quem ganhou a competição e vai ficar com a sala nova foi o {sorted_means[1][1]}!!! " + \
                              f"E o coitado que vai ter que comprar os móveis vai ser o {sorted_means[1][1]}."
        else:
            message = f"Quem ganhou a competição e vai ficar com a sala nova foi o Mike!!! " + \
                      f"E o coitado que vai ter que comprar os móveis vai ser o Harvey."

print(message)
