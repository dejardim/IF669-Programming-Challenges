"""21.1L3Q10 - The Salvation"""

pre_selection: int = int(input())
bunker_storage: int = int(input())

names: list = []
roles: list = []

engineers_amount: int = 0
doctors_amount: int = 0
scientist_amount: int = 0
teachers_amount: int = 0

is_engineers_full: bool = False
is_doctors_full: bool = False
is_scientist_full: bool = False
is_teachers_full: bool = False

total_people: int = 0
has_person: bool = True

for i in range(pre_selection):
    line: str = input()
    name, role = line.split(": ")
    names.append(name)
    roles.append(role)

    if role == "Engenheiro(a)" and not is_engineers_full:
        engineers_amount += 1
    elif role == "Medico(a)" and not is_doctors_full:
        doctors_amount += 1
    elif role == "Cientista" and not is_scientist_full:
        scientist_amount += 1
    elif role == "Professor(a)" and not is_teachers_full:
        teachers_amount += 1

    total_people = engineers_amount + doctors_amount + scientist_amount + teachers_amount

    if engineers_amount == bunker_storage / 4 and not is_engineers_full:
        print("Conseguimos chegar a quantidade maxima de Engenheiros")
        is_engineers_full = True
    elif doctors_amount == bunker_storage / 4 and not is_doctors_full:
        print("Conseguimos chegar a quantidade maxima de Medicos")
        is_doctors_full = True
    elif scientist_amount == bunker_storage / 4 and not is_scientist_full:
        print("Conseguimos chegar a quantidade maxima de Cientistas")
        is_scientist_full = True
    elif teachers_amount == bunker_storage / 4 and not is_teachers_full:
        print("Conseguimos chegar a quantidade maxima de Professores")
        is_teachers_full = True

    if total_people == bunker_storage:
        has_person = False
        print("Chegamos a nossa capacidade maxima")

try:
    while has_person:
        command: str = input()

        if command == "buscar":
            person: str = input()
            if person in names:
                print(f"{person} ja esta no bunker")
            else:
                print(f"{person} ainda não chegou no bunker...")
        elif command == "adicionar":
            line: str = input()
            name, role = line.split(": ")
            names.append(name)
            roles.append(role)

            if role == "Engenheiro(a)" and not is_engineers_full:
                engineers_amount += 1
            elif role == "Medico(a)" and not is_doctors_full:
                doctors_amount += 1
            elif role == "Cientista" and not is_scientist_full:
                scientist_amount += 1
            elif role == "Professor(a)" and not is_teachers_full:
                teachers_amount += 1

            total_people = engineers_amount + doctors_amount + scientist_amount + teachers_amount

            if engineers_amount == bunker_storage / 4 and not is_engineers_full:
                print("Conseguimos chegar a quantidade maxima de Engenheiros")
                is_engineers_full = True
            elif doctors_amount == bunker_storage / 4 and not is_doctors_full:
                print("Conseguimos chegar a quantidade maxima de Medicos")
                is_doctors_full = True
            elif scientist_amount == bunker_storage / 4 and not is_scientist_full:
                print("Conseguimos chegar a quantidade maxima de Cientistas")
                is_scientist_full = True
            elif teachers_amount == bunker_storage / 4 and not is_teachers_full:
                print("Conseguimos chegar a quantidade maxima de Professores")
                is_teachers_full = True

            if total_people == bunker_storage:
                has_person = False
                print("Chegamos a nossa capacidade maxima")
        else:
            print("**COMANDO INVALIDO**")
except EOFError:
    pass

if engineers_amount < bunker_storage / 4 or doctors_amount < bunker_storage / 4 or \
        scientist_amount < bunker_storage / 4 or teachers_amount < bunker_storage / 4:
    print("Na nossa busca no banco de dados, nao achamos pessoas suficientes com os parametros de selecao")
        
print(f"""
Relatorio:
Medicos: {doctors_amount}
Engenheiros: {engineers_amount}
Cientistas: {scientist_amount}
Professores: {teachers_amount}""")
