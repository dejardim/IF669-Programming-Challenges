"""21.1L3Q2 - Ajude o Klaus"""

supernaturals: list = [
    "Damon Salvatore", "Stefan Salvatore", "Caroline Forbes",
    "Elena Gilbert", "Bonnie Bennett", "Kai Parker", "Katherine Pierce",
]

found_names: list = []

has_input = True

try:
    while has_input:
        supernatural: str = input()
        if supernatural in supernaturals:
            if supernatural not in found_names:
                found_names.append(supernatural)
except EOFError:
    if not found_names:
        print("Nenhum sobrenatural foi encontrado :/")
    else:
        print("Os sobrenaturais encontrados foram:\n")
        for i in range(len(found_names)):
            print(found_names[i])
        print("\nAgora Klaus, Rebekah, Elijah, Kol e toda a família " +
              "original sabem bem em quem podem confiar e quem devem matar.")
