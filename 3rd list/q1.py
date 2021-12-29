"""21.1L3Q1 - My name is Barry Allen and..."""

speedters: list = []
positions: list = []

for i in range(5):
    line: str = input()
    speedter, rank = line.split(" - ")

    speedters.append(speedter)
    positions.append(int(rank))

for i in range(4):
    for j in range(4):
        if positions[j] > positions[j + 1]:
            aux: int = positions[j]
            positions[j] = positions[j + 1]
            positions[j + 1] = aux

            aux: str = speedters[j]
            speedters[j] = speedters[j + 1]
            speedters[j + 1] = aux

print("Velocista - Posicao\n")
for i in range(5):
    print(f"{speedters[i]} - {positions[i]}")
