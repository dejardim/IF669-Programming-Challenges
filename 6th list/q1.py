"""Cálculo Ciborgue"""

def flash(villains_number: int) -> str:
  """The function estimate if Flash won the battle and return a win or defeat message."""
  
  if 0 <= villains_number <= 15:
    return "A velocidade cuida dos nossos problemas"
  return "Flash cansou de correr"


def batman(villains_number: int) -> str:
  """The function estimate if Batman won the battle and return a win or defeat message. """
  
  if 0 <= villains_number <= 25:
    return "Morcego rei da noite"
  return "Volte para a batcaverna"


def aquaman(villains_number: int) -> str:
  """The function estimate if Aquaman won the battle and return a win or defeat message. """
  
  if 0 <= villains_number <= 20:
    return "O tridente brandiu"
  return "Sushi de heroi"


def wonderwoman(villains_number: int) -> str:
  """The function estimate if Wonderwoman won the battle and return a win or defeat message. """
  
  if 0 <= villains_number <= 50:
    return "O laco da verdade vai estralar"
  return "Volte para casa princesa Diana"


def show_report(msg: str):
  """Like a print, ok is the same of print function lol."""
  
  print(msg)


# Initial input
battles_amount: int = int(input())

# Dict with heroes function object references
heroes: dict = {
  'flash': flash,
  'batman': batman,
  'aquaman': aquaman,
  'maravilha': wonderwoman,
}

# Processing inputs and output results
for _ in range(battles_amount):
  line = input()
  hero, villains_amount = line.split()
  
  message = heroes[hero](int(villains_amount))
  show_report(message)
  
