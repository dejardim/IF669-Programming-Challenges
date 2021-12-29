'''As ferramentas do Batman'''

# Initial input
battles_amount: int = int(input())

# Setup variables
damages: dict = {
    'Batrangue': 270,
    'Bat-Minas': 255,
    'Tasers': 185,
    'Soqueiras': 150,
    'Granada Sonica': 300,
    'Gel Explosivo': 400,
    'Faca Tatica': 345,
}

reports: dict = {
    'Mortos': 0,
    'Fugas': 0,
    'Incapacitados': 0,
}

# Setup Battle in range of Battles, wait battle result and update the report in reports
for _ in range(battles_amount):
    tools_amount: int = int(input())
    initial_life: float = int(input())
    enemy_life: float = initial_life

    # Start Battle
    for __ in range(tools_amount):
        tool: str = input()

        if tool not in damages.keys():
            print(f'{tool}? Infelizmente esta ferramenta não está disponível.')
        else:
            if enemy_life >= (initial_life * 0.4):
                enemy_life -= damages[tool]
            else:
                if 100 <= damages[tool] < 200:
                    enemy_life -= damages[tool] * 0.5
                elif 200 <= damages[tool] < 300:
                    enemy_life -= damages[tool] * 0.25
                elif damages[tool] >= 300:
                    enemy_life -= damages[tool] * 0.15

    if enemy_life > initial_life * 0.15:
        reports['Fugas'] += 1
    elif enemy_life <= 0:
        reports['Mortos'] += 1
    elif enemy_life <= initial_life * 0.15:
        reports['Incapacitados'] += 1

# Show the result of reports
print(f'''Mortos: {reports['Mortos']}
Fugas: {reports['Fugas']}
Incapacitados: {reports['Incapacitados']}''')

# Making my life easier
successful_missions: int = reports['Incapacitados']
failed_missions: int = reports['Mortos'] + reports['Fugas']

# Show feedback message
if failed_missions > 0 and successful_missions > failed_missions:
    print('Batman conseguiu capturar a maioria dos criminosos, nosso herói está no caminho certo.')
elif failed_missions == 0 and successful_missions > failed_missions:
    print('Batman conseguiu capturar todos os criminosos e garantiu uma noite segura em Gotham City.')
elif successful_missions > 0 and failed_missions > successful_missions:
    print('Muitas missões fracassadas.. Pelo visto, o nosso herói precisa treinar mais.')
elif successful_missions == 0 and failed_missions > successful_missions:
    print('Muitas missões fracassadas... Tem certeza de que o seu programa passou as ferramentas corretas?')
elif successful_missions == failed_missions:
    print('Uma noite caótica em Gotham City, talvez o nosso herói precise mudar as ferramentas...')
