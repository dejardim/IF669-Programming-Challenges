'''A Senha da Casa de Tony'''

def count_letters(word: str) -> dict:
    '''Count each letter in word, return a dict with results.'''

    # Initialization of Dict varible
    letters: dict = {}

    for letter in word:

        '''
        letters.get(letter, 0) + 1 do the same of:

        if letter not in letters.keys():
            letters[letter] = 0
        letters[letter] += 1

        because .get() first param wait the key, if this key not exist
        the second param is a default value to create the key value.
        '''
        letters[letter] = letters.get(letter, 0) + 1

    return letters


# Input words and convert to lowercase
passkey: str = input().lower()
password: str = input().lower()

# Variables with the pattern of letters of each word as value
pattern_A = count_letters(passkey)
pattern_B = count_letters(password)

# Check if Pattern A is equal Pattern B and output the result
if pattern_A == pattern_B:
    print('Acesso liberado. Bem vindo Senhor Stark.')
else:
    print('Acesso negado.')
