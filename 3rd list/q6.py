"""21.1L3Q6 - WHAT IF.... ?"""

has_input: bool = True
numbers: list = []

while has_input:
    number: str = input()
    if number == "fim":
        has_input = False
    else:
        numbers.append(int(number))

for i in range(len(numbers) - 1):
    for n in range(len(numbers) - 1):
        if numbers[n] > numbers[n+1]:
            aux: int = numbers[n]
            numbers[n] = numbers[n+1]
            numbers[n+1] = aux

for n in range(len(numbers)):
    print(numbers[n])
        