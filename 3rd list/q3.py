"""21.1L3Q3 - Legen...Wait for it...Dary"""

has_input: bool = True
names: list = []

while has_input:
    command: str = input()

    if command == "adicionar":
        name: str = input()
        names.append(name)
        print(f"{name} foi adicionada ao final da lista")
    elif command == "remover":
        name: str = input()
        names.remove(name)
        print(f"{name} foi removida da lista")
    elif command == "atualizar posiçao":
        name: str = input()
        index: int = int(input())

        if name == names[index]:
            print(f"Nada mudou, {name} ja esta na posiçao certa")
        else:
            names.remove(name)
            names.insert(index, name)
            print(f"{name} foi inserida na posição {index} da lista")
    elif command == "fim":
        has_input = False

if not names:
    print("Não sobraram pretendentes para voce, Ted")
else:
    for i in range(len(names)):
        if i == len(names) - 1:
            print(names[i], end="")
        else:
            print(names[i], end=" ")
            