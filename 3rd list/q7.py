"""21.1L3Q7 - Fsociety"""

key: str = input()
key_protocol: str = input()
seed: str = input()

key: list = key.split()
key_protocol: list = key_protocol.split()

start: int = key.index(seed)
index = start

letters: list = []

for char in key_protocol:
    if char == "/":
        letters.append(" ")
    elif char == "R":
        letters.append(key[index])
    else:
        index += int(char)
        if index >= 26:
            index = index % 26
            letters.append(key[index])
        else:
            letters.append(key[index])

message: str = "".join(letters)
print(message)
