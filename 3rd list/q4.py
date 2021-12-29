"""21.1L3Q4 - Fim do Bobby Axelrold"""

witnesses: str = input()
swap_amount: int = int(input())

names: list = witnesses.split()

for i in range(swap_amount):
    index = int(input())

    if index == 0:
        aux1: str = names[index]
        aux2: str = names[-1]

        names[0] = aux2
        names[-1] = aux1

        print(f"A testemunha {aux1} trocou de ordem com a testemunha {aux2}")
    else:
        aux1: str = names[index]
        aux2: str = names[-(index+1)]

        if aux1 == aux2:
            print("Nenhuma troca foi feita")
        else:
            i1 = names.index(aux1)
            i2 = names.index(aux2)

            names[i1] = aux2
            names[i2] = aux1

            print(f"A testemunha {aux1} trocou de ordem com a testemunha {aux2}")

for i in range(len(names)):
    if i == len(names) - 1:
        print(names[i], end="")
    else:
        print(names[i], end=" ")
