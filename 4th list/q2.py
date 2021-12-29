"""21.1L4Q2 - Crash, nos Proteja!"""

def set_life(arglist: list) -> float:
    """
    Given a list, in format [mask, life], return new life float number.

    :param arglist: a list that coin the name of mask in [0] and life in [1]
    :return: new value of life
    """

    mask, life = arglist
    life = float(life)
    if mask == "Aku-Aku":
        life *= 2
    elif mask == "Velo":
        life *= 1.25
    elif mask == "Apo-Apo":
        life *= 1.5
    return life


def set_damage(damage: int, t_fruit: int) -> int:
    """
    Given values of damage and total fruit, return new villain damage int number

    :param damage: value of villain damage
    :param t_fruit: amount of Crash's collected fruits
    :return: new villain damage
    """

    if t_fruit <= 20:
        damage = damage ** 2
    elif t_fruit <= 30:
        damage = damage + damage
    return damage


villain_amount: int = int(input())
victory_amount: int = 0

for i in range(villain_amount):
    line: str = input()
    crash_life: float = set_life(line.split())
    line: str = input()
    villain_name, dmg = line.split()

    total_fruit: int = 0
    while True:
        fruit_collection: int = int(input())
        total_fruit += fruit_collection
        if fruit_collection == 0:
            break

    villain_damage = set_damage(int(dmg), total_fruit)

    if total_fruit < 10:
        print(f"Infelizmente o Crash só conseguiu pegar {total_fruit} frutas," +
              f" então, não é hoje que ele vai derrotar o {villain_name} =(")
    elif crash_life - villain_damage <= 0:
        print("Aku-Aku estamos precisando de você!")
    else:
        print(f"O nosso herói conseguiu mais uma vez! Pisou no {villain_name}.")
        victory_amount += 1

if villain_amount == 0:
    print("Nenhum vilão teve coragem de encarar o Crash hoje!")
elif villain_amount - victory_amount >= victory_amount:
    print("Não é possível, o Crash não conseguiu vencer?")
else:
    print("O Crash conseguiu livrar as Ilhas Wumpa das mãos dos vilões!!!")
