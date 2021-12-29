"""21.1L4Q1 - YOU ROCK!"""

def calculate_score(chords: list) -> int:
    """
    Given a chords, list of chord, return the performance result
    
    :param chords: a list with len=5 that 0s and Xs as chord
    :return: performance result
    """

    score: int = 0
    memo: str = ""
    for chord in chords:
        if chord == "X":
            if memo == "X":
                score += 10
            else:
                score += 5
            memo = "X"
        else:
            memo = "0"
    return score


def make_report(score: int) -> str:
    """
    Given a score, total result of performance, return the message report
    
    :param score: int number
    :return: str message
    """

    message: str = ""
    if score < 15:
        message = "Song failed!"
    elif score <= 49:
        message = "Nada bom, amigo..."
    elif score <= 69:
        message = "Wow, rock and roll na veia!"
    elif score <= 100:
        message = "YOU ROCK!!!"
    elif score > 100:
        message = "TEMOS UMA NOVA LENDA DO ROCK!"
    return message + "\n" + f"Sua pontuação foi de {score} pontos"


line: str = input()
total_score: int = 0

while line != "0 0 0 0 0":
    if line == "X X X X X":
        total_score += 20
        print("Note streak!")

    line: list = line.split()
    total_score += calculate_score(line)

    line: str = input()

print(make_report(total_score))
