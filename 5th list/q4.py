"""21.1L5Q4 - fladnaG ed soçitieF"""

def recursive_reverse(string: str) -> str:
    """Reverse the string and return the result."""

    # Base case
    if len(string) - 1 == 0:
        return string[0]

    # string=HEY -> Y(last word) + fn(HE) -> Y + E(last word) + fn(H) -> Y + E + H(base case) -> YEH
    return string[len(string) - 1] + recursive_reverse(string[:len(string) - 1])


def recursive_lower(string: str) -> str:
    """Convert the string to lowercase and return the result."""

    # Base case
    if string == "":
        return ""

    # Convert char in index 0 to own value in ascii
    ascii_char = ord(string[0])

    # Check if character is uppercase by ASCII values
    if ascii_char in range(65, 91):

        # Convert to lowercase just add 32 (ASCII relation)
        ascii_char += 32

        return chr(ascii_char) + recursive_lower(string[1:])
    return chr(ascii_char) + recursive_lower(string[1:])


# Gandalf Word Input
gandalf_word: str = input()

# Conversion the word and process
word = recursive_lower(gandalf_word)
word = recursive_reverse(word)


# Output ways
print(word)
if word == "amigo" or word == "ogima" or \
   word == "mellon" or word == "nollem":
    print("Desvendamos o misterio e a porta se abriu!")
else:
    print("Acho que ainda nao acertamos, Gandalf, o que faremos agora?")
