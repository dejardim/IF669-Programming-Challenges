"""21.1L5Q1 - Palavras preciosas de Fibonacci"""

def mypreciousnacci(n: int) -> str:
    """'My' and 'Precious' sequence (Fibonacci based function)."""

    # Base case
    if n == 0:
        return "Precious"

    # Base case
    if n == 1:
        return "My"
    
    return mypreciousnacci(n - 1) + mypreciousnacci(n - 2)


# Sequence term position Input
term_position: int = int(input())

# Search what term in position
term: str = mypreciousnacci(term_position)

# Output result
print(term)
