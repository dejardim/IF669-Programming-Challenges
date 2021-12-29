"""21.1L2Q7 - Corrida com Obstáculos"""

laps_amount: int = int(input())

success_amount: int = 0
failure_amount: int = 0

historic: str = ""
cache: str = ""

failure_alert: int = 0
failure_sequence: int = 0

limit_time: int = 72 * laps_amount  # 60 segs + 12 segs
spent_time: int = 0

for i in range(laps_amount * 10):
    obstacle: str = input()

    if obstacle == "acerto":
        spent_time += 5
        success_amount += 1
        failure_sequence = 0
        failure_alert = 0

    if obstacle == "erro":
        spent_time += 9
        failure_amount += 1
        if historic == "erro":
            if cache == "erro":
                failure_alert += 2
            failure_sequence += 2

    historic = obstacle
    cache = obstacle

    if failure_sequence == 8:
        print("O treino de hoje nao esta rendendo Carlinhos, vamos tentar de novo amanha")
        break

    if failure_alert > 0 and failure_alert % 2 == 0:
        print("Voce precisa melhorar, Carlinhos")
        cache = ""
        failure_alert = 0

    if spent_time > limit_time:
        print("Temos que trabalhar urgentemente na sua velocidade, voce precisa errar menos")
        break

if not failure_amount:
    print("Que desempenho excelente, Carlinhos, melhor impossivel")
else:
    print("Seu desempenho esta bom, mas poderia ter sido muito melhor")
