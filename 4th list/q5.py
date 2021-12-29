"""21.1L4Q5 - Age of Criptonacci"""

def fib(x: int) -> int:
    """
    Given a N term of fib series, return the fib number in this position

    :param x: N term position
    :return: fib number
    """
    
    if x < 2:
        return 1

    fib_series: list = [0, 1, 1]
    for _ in range(2, x):
        next_number = fib_series[-2] + fib_series[-1]
        fib_series.append(next_number)
    return fib_series[-1]


sentences_amount: int = int(input())
ALPHABET: list = list("abcdefghijklmnopqrstuvwxyz")

for i in range(sentences_amount):
    keyN: int = int(input())
    sentenceN: str = input()

    sentenceN = sentenceN.lower().replace(" ", "")  # Remove spaces and set in lowercase
    words: list = list(sentenceN)

    new_words: list = []
    for j in range(len(words)):
        index: int = ALPHABET.index(words[j])
        new_index: int = index + fib(keyN + j)

        if new_index > 25:
            new_words.append(ALPHABET[new_index % 26])
        else:
            new_words.append(ALPHABET[new_index])

    crypt_sentence: str = "".join(new_words)
    print(crypt_sentence)
