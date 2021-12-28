"""21.1L1Q1 - Reprodutor de música"""

key_word: str = input()

# (REASON): pattern to conditional boolean expressions
str_equal_amor: bool = key_word == "amor"
str_equal_volta: bool = key_word == "volta"
str_equal_ficha: bool = key_word == "ficha"
str_equal_chega: bool = key_word == "chega"
str_equal_arranhao: bool = key_word == "arranhao"

# (REASON): important variables to print the result
is_valid_input: bool = False
song: str = ""

# (WHAT_IS): conditional structure
if str_equal_amor:
    song = "SE FOR AMOR - Joao Gomes e Vitor"
    is_valid_input = True
elif str_equal_volta:
    song = "VOLTA COMIGO BB - Ze Vaqueiro"
    is_valid_input = True
elif str_equal_ficha:
    song = "FICHA LIMPA - Gusttavo Lima"
    is_valid_input = True
elif str_equal_chega:
    song = "CHEGA E SENTA - John"
    is_valid_input = True
elif str_equal_arranhao:
    song = "ARRANHAO - Henrique e Juliano"
    is_valid_input = True

# (WHAT_IS): output result
if is_valid_input:
    print(f"Voce selecionou a musica: {song}")
