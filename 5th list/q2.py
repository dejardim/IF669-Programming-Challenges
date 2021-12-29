"""21.1L5Q2 - A equação de Gandalf"""

def bubble_sort(arr: list) -> list:
    """Sort a list array (int/float) and return sorted list."""

    # Create new list to be more safe
    new_arr: list = arr.copy()

    # Sort process
    for i in range(len(new_arr) - 1):
        for j in range(len(new_arr) - 1):
            if new_arr[j] > new_arr[j+1]:
                new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]
    return new_arr


def int2str(arr: list) -> list:
    """Convert a list with int type (numbers) in str type (string numbers)."""

    # Create new list to be more safe
    new_arr: list = []

    # Convert int in str
    for element in arr:
        new_arr.append(str(element))
    return new_arr


def invaluable_equation(n: str) -> str:
    """Invaluable equation, capable of transforming the number of warriors."""

    # List var storage ints of: str(count(digit)) + digit -> '10' -> 10 ...
    results: list = []

    # Process to count digits concatenate and append result in list
    digits: list = list(n)
    for digit in digits:
        result = str(digits.count(digit)) + digit
        if int(result) not in results:
            results.append(int(result))

    # Convert items to str after sort list
    results = int2str(bubble_sort(results))

    # Base case
    if len(results) >= 4:
        return "".join(results)

    # Based on list make a new number
    new_number = "".join(results)

    return invaluable_equation(new_number)


# First Number Input
number: str = input()

# Output result
print(invaluable_equation(number))
