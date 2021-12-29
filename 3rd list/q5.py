was_not_hacked: bool = True

committed_crimes: list = []
criminal_names: list = []

murders: list = []
thieves: list = []

while was_not_hacked:
    line: str = input()
    pack: list = line.split(": ")

    if "Doug Judy" in pack:
        was_not_hacked = False
    else:
        crime, criminal = pack

        committed_crimes.append(crime)
        criminal_names.append(criminal)

        if crime == "Assassinato":
            if not criminal in murders:
                murders.append(criminal)
        elif crime == "Roubo" or crime == "Furto":
            if not criminal in thieves:
                thieves.append(criminal)

operations_amount: int = int(input())

for i in range(operations_amount):
    operation: str = input()
    count: int = 0

    if operation == "1":
        look_for: str = input()
        for name in criminal_names:
            if look_for == name:
                count += 1
        print(f"Na ficha de {look_for} constam {count} infrações este mês.")
    elif operation == "2":
        look_for: str = input()
        for crime in committed_crimes:
            if look_for == crime:
                count += 1
        print(f"Neste mês foram cometidos {count} {look_for}")
    elif operation == "3":
        print("Boletim de Ocorrências:")

        if not murders:
            print("Assassinos: ")
        elif len(murders) == 1:
            print(f"Assassinos: {murders[0]}")
        else:
            print("Assassinos: ", end="")
            for j in range(len(murders)):
                if j == len(murders) - 1:
                    print(f"{murders[j]}")
                else:
                    print(f"{murders[j]}, ", end="")

        if not thieves:
            print("Ladroes: ")
        elif len(thieves) == 1:
            print(f"Ladroes: {thieves[0]}")
        else:
            print("Ladroes: ", end="")
            for j in range(len(thieves)):
                if j == len(thieves) - 1:
                    print(f"{thieves[j]}")
                else:
                    print(f"{thieves[j]}, ", end="")
