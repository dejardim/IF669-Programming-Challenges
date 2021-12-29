"""21.1L2Q2 - Campeonato de Surf"""

first_surfer: str = input()
second_surfer: str = input()
third_surfer: str = input()

first_nationality: str = input()
second_nationality: str = input()
third_nationality: str = input()

phases_amount: int = int(input())

first_score: float = 0
second_score: float = 0
third_score: float = 0

msg: str = ""

for i in range(phases_amount):
    first_score += float(input())
    second_score += float(input())
    third_score += float(input())

if first_score == second_score and second_score == third_score:
    if first_nationality == "Brasil":
        msg = f"O vencedor da medalha de ouro de surf e {first_surfer}! E do Brasil!"
    else:
        msg = f"O vencedor da medalha de ouro de surf e {first_surfer}!"
elif first_score == second_score and first_score > third_score:
    if first_nationality == "Brasil":
        msg = f"O vencedor da medalha de ouro de surf e {first_surfer}! E do Brasil!"
    else:
        msg = f"O vencedor da medalha de ouro de surf e {first_surfer}!"
elif first_score == third_score and first_score > second_score:
    if first_nationality == "Brasil":
        msg = f"O vencedor da medalha de ouro de surf e {first_surfer}! E do Brasil!"
    else:
        msg = f"O vencedor da medalha de ouro de surf e {first_surfer}!"
elif first_score == third_score and first_score < second_score:
    if second_nationality == "Brasil":
        msg = f"O vencedor da medalha de ouro de surf e {second_surfer}! E do Brasil!"
    else:
        msg = f"O vencedor da medalha de ouro de surf e {second_surfer}!"
elif second_score == third_score and second_score > first_score:
    if second_nationality == "Brasil":
        msg = f"O vencedor da medalha de ouro de surf e {second_surfer}! E do Brasil!"
    else:
        msg = f"O vencedor da medalha de ouro de surf e {second_surfer}!"
else:
    if third_score > second_score and third_score > first_score:
        if third_nationality == "Brasil":
            msg = f"O vencedor da medalha de ouro de surf e {third_surfer}! E do Brasil!"
        else:
            msg = f"O vencedor da medalha de ouro de surf e {third_surfer}!"
    if second_score > third_score and second_score > first_score:
        if second_nationality == "Brasil":
            msg = f"O vencedor da medalha de ouro de surf e {second_surfer}! E do Brasil!"
        else:
            msg = f"O vencedor da medalha de ouro de surf e {second_surfer}!"
    if first_score > second_score and first_score > third_score:
        if first_nationality == "Brasil":
            msg = f"O vencedor da medalha de ouro de surf e {first_surfer}! E do Brasil!"
        else:
            msg = f"O vencedor da medalha de ouro de surf e {first_surfer}!"

print(msg)
