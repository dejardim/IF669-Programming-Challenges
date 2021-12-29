'''O cara na cadeira!'''

def search_villain(enemy: str, enemies: dict) -> str:
    '''Search the villain in the dict, return a message.'''

    # Check if has enemy in the keys of enemies dict
    if enemy in enemies.keys():
        return f'Os atributos do {enemy} foram:\n' + \
               f'ataque: {enemies[enemy]["ataque"]}\n' + \
               f'defesa: {enemies[enemy]["defesa"]}\n' + \
               f'vida: {enemies[enemy]["vida"]}'

    # Else
    return 'Peter, foca nos viloes que tao ai agora! se liga, boy'


def search_attribute(enemy: str, enemies: dict, attribute: str) -> str:
    '''Search villain attribute in the dict structure. return a message.'''

    if enemy in enemies.keys():

        # Check if has attribute in the keys of enemies[enemy] dict
        if attribute in enemies[enemy].keys():
            msg: str = f'O(a) {attribute} do {enemy} e: {enemies[enemy][attribute]}\n'

            if attribute == 'vida' and enemies[enemy][attribute] <= 5:
                msg += f'{enemy} esta enfraquecido! va para cima dele, peter!!'
            elif attribute == 'vida' and enemies[enemy][attribute] >= 15:
                msg += f'Nao foque em {enemy} ainda! ele esta muito bem'

            if attribute == 'defesa' and enemies[enemy][attribute] <= 5:
                msg += f'Va agora! {enemy} nao se defende bem'
            elif attribute == 'defesa' and enemies[enemy][attribute] >= 15:
                msg += f'cara, voce nao vai conseguir machuca-lo, {enemy} e uma muralha!'

            if attribute == 'ataque' and enemies[enemy][attribute] >= 15:
                msg += f'{enemy} vai destruir a cidade, chama o Dr. estranho!'

            return msg

        # Else
        return 'Ta viajando, peter? nao existe esse atributo'
    return 'Peter, foca nos viloes que tao ai agora! se liga, boy'


def compare_attribute(enemy_1: str, enemy_2: str, enemies: dict, attribute: str) -> str:
    '''Given two villain, the dict and one atribute to compare the attributes.'''

    msg: str = 'Aqui esta a comparacao, peter!\n' + \
               f'{enemy_1}: {enemies[enemy_1][attribute]} X {enemy_2}: {enemies[enemy_2][attribute]}\n'

    if enemies[enemy_1][attribute] > enemies[enemy_2][attribute]:
        msg += f'O vilao com menos {attribute} e o {enemy_2}, pra cima dele!'
    else:
        msg += f'O vilao com menos {attribute} e o {enemy_1}, pra cima dele!'

    return msg


# Initial input
villains_amount: int = int(input())

# Initialization of varible
villains: dict = {}

# Villains Input and build Villains dict
for _ in range(villains_amount):
    villain_name = input()
    villain_attributes = input().split(" - ")

    villains[villain_name] = {
        'ataque': int(villain_attributes[0].split(", ")[1]),
        'defesa': int(villain_attributes[1].split(", ")[1]),
        'vida': int(villain_attributes[2].split(", ")[1]),
    }

# Input how much interactions
actions_amount: int = int(input())

# Initialization of varible
actions: dict = {
    'pesquisar vilao': search_villain,
    'pesquisar atributo': search_attribute,
    'comparar atributo': compare_attribute,
}

# Output ways in range of interactions
for _ in range(actions_amount):
    choice: str = input()

    result: str = ''

    if choice == 'pesquisar vilao':
        name: str = input()
        result = actions[choice](name, villains)
    elif choice == 'pesquisar atributo':
        name: str = input()
        attribute_type: str = input()
        result = actions[choice](name, villains, attribute_type)
    elif choice == 'comparar atributo':
        name_1: str = input()
        name_2: str = input()
        attribute_type: str = input()
        result = actions[choice](name_1, name_2, villains, attribute_type)

    print(result)
